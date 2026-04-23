# py-nba-feed

Repozytorium **py-nba-feed**: pakiet konfiguracyjny Django ma nazwę **`app`** (`app.settings`, `app.urls`, widoki i API w tym samym pakiecie). Oprócz tego aplikacja **`user`** (własny model użytkownika). **DRF**, **PostgreSQL** (`DATABASE_URL`), **Docker Compose**, **Swagger** (drf-spectacular), django-environ, pytest, django-debug-toolbar.

## Stack

- Python **3.11+**
- Django **5.2**
- **DRF** + **drf-spectacular**
- **PostgreSQL 16** przy ustawionym `DATABASE_URL`; inaczej **SQLite**
- **django-environ**

## Lokalnie (bez Dockera)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -U pip
pip install -r requirements-dev.txt
copy .env.example .env
```

Bez `DATABASE_URL` w `.env` używany jest **SQLite**. Dla Postgresa na hoście odkomentuj `DATABASE_URL` w `.env`.

```powershell
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Docker Compose

```powershell
copy .env.example .env
docker compose up --build
docker compose exec web python manage.py migrate
```

W kontenerze katalog roboczy to **`/app`** (WORKDIR), a kod projektu leży w tym katalogu — pakiet Django **`app/`** to np. `/app/app/` wewnątrz obrazu.

## Ustawienia

| Moduł | Zastosowanie |
|--------|----------------|
| `app.settings.local` | Domyślnie w `manage.py` i w Compose |
| `app.settings.production` | Domyślnie w `app.wsgi` / `app.asgi`, jeśli nie ustawisz `DJANGO_SETTINGS_MODULE` |

## Endpointy

- http://127.0.0.1:8000/health/
- http://127.0.0.1:8000/api/v1/health/
- Swagger: http://127.0.0.1:8000/api/schema/swagger-ui/

Baza w Compose: **`py_nba_feed`** (nazwa bazy w Postgresie; to nie jest nazwa pakietu Pythona).

## Testy

```powershell
pytest
black .
flake8 .
```

## Układ katalogów

```
py-nba-feed/
├── app/                 # Konfiguracja Django: settings, urls, wsgi, asgi, views, api_urls
├── user/
├── docker-compose.yml
├── Dockerfile
├── templates/
├── static/
├── media/
├── tests/
├── manage.py
├── requirements.txt
└── requirements-dev.txt
```

## Git flow

```powershell
git flow init -d
```
