import os
import sys
from pathlib import Path

import dj_database_url
from decouple import config, Csv
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

# BASE
BASE_DIR = Path(__file__).resolve().parent.parent

# Segurança
SECRET_KEY = config("SECRET_KEY")
DEBUG = config("DEBUG", default=False, cast=bool)
ALLOWED_HOSTS = config("ALLOWED_HOSTS", default="*", cast=Csv())
ENV = config("ENV", default="localhost")

# --- APLICATIVOS ---
INSTALLED_APPS = [
    # Painel administrativo
    "jazzmin",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Apps do projeto
    "fitapp.core",
    "fitapp.profile.apps.ProfileConfig",
]

# --- AUTENTICAÇÃO ---
LOGIN_URL = "profile:login"
LOGIN_REDIRECT_URL = "profile:dashboard"
LOGOUT_REDIRECT_URL = "profile:login"

# --- MIDDLEWARE ---
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# --- URL ROOT ---
ROOT_URLCONF = "fitapp.urls"

# --- TEMPLATES ---
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "fitapp" / "core" / "templates",  # base_adminlte.html e includes
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# --- ARQUIVOS ESTÁTICOS ---
STATIC_URL = "/static/"
STATICFILES_DIRS = [
    BASE_DIR / "fitapp" / "core" / "static",  # onde ficarão adminlte/ e css/
]
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# --- WSGI ---
WSGI_APPLICATION = "fitapp.wsgi.application"

# --- BANCO DE DADOS ---
DATABASES = {"default": dj_database_url.parse(config("DATABASE_URL"))}

# --- VALIDAÇÃO DE SENHA ---
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# --- INTERNACIONALIZAÇÃO ---
LANGUAGE_CODE = "pt-br"
TIME_ZONE = "America/Sao_Paulo"
USE_I18N = True
USE_TZ = True

# --- DEFAULTS ---
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# --- SENTRY ---
sentry_sdk.init(
    environment=ENV,
    dsn=config("SENTRY_DSN", default=""),
    integrations=[DjangoIntegration()],
    traces_sample_rate=1.0,
    send_default_pii=True,
)

# --- NOMIGRATIONS (para testes) ---
if os.environ.get("NO_MIGRATIONS") == "1":
    MIGRATION_MODULES = {
        "core": None,
        "profile": None,
        "catalog": None,
        "training": None,
        "nutrition": None,
        "social": None,
        "running": None,
    }

# --- JAZZMIN SETTINGS ---
# --- JAZZMIN SETTINGS (Padrão) ---
JAZZMIN_SETTINGS = {
    "site_title": "Django Admin",
    "site_header": "Administração",
    "welcome_sign": "Bem-vindo ao painel administrativo",
}

# --- JAZZMIN UI TWEAKS (Padrão) ---
JAZZMIN_UI_TWEAKS = {}
