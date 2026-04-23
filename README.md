# py-nba-feed

Django project package **`py_nba_feed`**, dev-ready layout with split settings, custom user model, django-environ, pytest, and django-debug-toolbar.

## Stack

- Python **3.11+** (tested with 3.11)
- Django **5.2**
- SQLite locally; optional **`DATABASE_URL`** (e.g. Postgres) for production
- **django-environ** for configuration

## Setup

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -U pip
pip install -r requirements-dev.txt
copy .env.example .env
```

Edit `.env` if needed (at minimum set a unique `SECRET_KEY` before any shared deploy).

## Run

```powershell
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

- Admin: http://127.0.0.1:8000/admin/
- Health: http://127.0.0.1:8000/health/
- Debug toolbar: http://127.0.0.1:8000/__debug__/ (only when `DEBUG=True`)

## Settings modules

| Module | Use |
|--------|-----|
| `py_nba_feed.settings.local` | Local development (`manage.py` default) |
| `py_nba_feed.settings.production` | Production (`wsgi.py` / `asgi.py` default if `DJANGO_SETTINGS_MODULE` is unset) |

Override for ad-hoc commands:

```powershell
$env:DJANGO_SETTINGS_MODULE = "py_nba_feed.settings.production"
python manage.py check
```

## Tests and lint

```powershell
pytest
black .
flake8 .
```

## Layout

```
py-nba-feed/
├── app/                 # Main app (health route)
├── user/                # Custom user (`AUTH_USER_MODEL`)
├── py_nba_feed/         # Project config + settings package
├── templates/
├── static/
├── media/
├── tests/
├── manage.py
├── requirements.txt
└── requirements-dev.txt
```

## Git flow

Initial work should live on **`main`** with a clean first commit, then:

```powershell
git flow init -d
```

If [git-flow (AVH edition)](https://github.com/petervanderdoes/gitflow-avh/wiki/Windows) is not installed, install it first or use Git’s native branching; the defaults are production branch `main`, development branch `develop`, and prefixes `feature/`, `release/`, `hotfix/`.

## Production notes

- Set **`SECRET_KEY`**, **`ALLOWED_HOSTS`**, and **`DATABASE_URL`** (if not using the default SQLite file) via environment or `.env` as appropriate for your host.
- Configure HTTPS at the proxy; `production.py` enables secure cookie flags and `SECURE_PROXY_SSL_HEADER` for typical TLS termination.
