Smolib (Small Library) Digital REST API

# How to setup for Development
## Requirements
- Python 3.12+
- Django 5+
- Django REST Framework 3.15+
- Postgres
- Poetry or Pip

## Steps
1. Setup Postgres dan buat database baru
2. Install dependency project
    - Menggunakan Poetry
        - Masuk environment `poetry shell`
        - Install packages `poetry install`
    - Menggunakan Pip
        - Buat environment `python -m venv venv`
        - Masuk environment (Windows) `source venv/Scripts/activate`
        - atau (Linux) `source venv/bin/active`
        - Install packages `pip install -r requirements.txt`
3. Jalankan project setelah masuk virtual environment `python manage.py runserver`

## Catatan:

Pastikan `.env` file telah dibuat berdasarkan format pada `.env.example` dan field-fieldnya terisi.

Untuk secret key dapat generate [di sini](https://djecrety.ir/)

File `collection.json` adalah hasil export Postman Collections v2.1, bisa diimport untuk test API.
