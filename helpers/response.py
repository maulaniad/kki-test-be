from typing import Any

from rest_framework.response import Response as _Res
from rest_framework.renderers import JSONRenderer


class Response(_Res):
    """
    Shortcut to rest_framework's Response, with a little customization.
    """

    def __init__(self, data: Any, status: int = 200, message: str = "OK"):
        """
        Sends a response provided by rest_framework's own class.
        - Pass a dict/object into `data` to send a single data.
        - Pass a list into `data` to send multiple data.
        """

        self.data = {
            'message': message,
            'data': data
        }

        super().__init__(data=self.data, status=status)


class ResponseRenderer(JSONRenderer):
    """
    Custom Response Renderer to follow the Standardized Response.
    """

    def render(self, data: dict[str, Any] | Any,
               accepted_media_type: str | Any = None,
               renderer_context: dict[str, Any] | Any = None):

        # If there is an exception, use the Stardandized Errors to format the response
        if renderer_context['response'].exception:
            return super().render(data, accepted_media_type, renderer_context)

        # If no data is provided, use the default response usually it's a 204 No Content
        if not data:
            return super().render(data, accepted_media_type, renderer_context)

        # Otherwise, use this customized response
        message = data.get('message', "OK")
        data = data.get('data', data)
        response_data = {
            'status': renderer_context['response'].status_code,
            'success': True,
            'message': message,
            'data': data
        }

        # These checks are verifying whether the data is from the pagination helper
        # If it is, correct the 'data' placement add the meta data to the response
        # No calculations are done here
        if 'pagination' in data and data.get('pagination'):
            response_data['data'] = data.get('paginated_data') or data['paginated_data']
            response_data['meta'] = data.get('meta') or data['meta']

        return super().render(response_data, accepted_media_type, renderer_context)
