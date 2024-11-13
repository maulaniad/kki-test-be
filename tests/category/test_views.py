from tests import APITestCase, APIClient
from tests.category.fixtures import CATEGORY_FIXTURES
from tests.category.endpoints import CategoryEndpoints


class TestCategoryViews(APITestCase):
    fixtures = CATEGORY_FIXTURES

    def setUp(self) -> None:
        self.client = APIClient()
        self.endpoints = CategoryEndpoints()
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()
