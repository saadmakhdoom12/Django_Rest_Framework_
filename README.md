# Django REST Framework Project

A Django REST Framework project with Poetry dependency management.

## Prerequisites

- Python 3.8 or higher
- Poetry package manager

## Setup

1. Clone the repository:

```bash
git clone git@github.com:saadmakhdoom12/Django_Rest_Framework_.git
cd jango_restframework
```

2. Install dependencies using Poetry:

```bash
poetry install
```

3. Activate the virtual environment:

```bash
poetry shell
```

4. Apply migrations:

```bash
python manage.py migrate
```

5. Run the development server:

```bash
python manage.py runserver
```

## Project Structure

```bash
jango_restframework/
├── poetry.lock
├── pyproject.toml
├── manage.py
└── ...
```

## Development

To add new dependencies:
```bash
poetry add package-name
```

To update dependencies:
```bash
poetry update
```

## API Documentation

The API documentation is available at:
- Swagger UI: `/api/docs/`
- ReDoc: `/api/redoc/`

## License

[MIT License](LICENSE)
