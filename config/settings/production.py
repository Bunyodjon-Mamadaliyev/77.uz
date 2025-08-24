from .base import *  # noqa
from .base import REST_FRAMEWORK as BASE_REST_FRAMEWORK

ALLOWED_HOSTS = [
    "bonx.uz",
    "www.bonx.uz",
    "localhost",
    "127.0.0.1",
]

CSRF_TRUSTED_ORIGINS = [
    "https://bonx.uz",
    "https://www.bonx.uz",
]

CORS_ALLOWED_ORIGINS = [
    "https://bonx.uz",
    "https://www.bonx.uz",
]

DEBUG = False

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 60 * 60 * 24 * 7 * 52
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

CORS_ALLOW_ALL_ORIGINS = False
CORS_ALLOW_CREDENTIALS = False
CORS_ORIGIN_ALLOW_ALL = False

REST_FRAMEWORK = {
    **BASE_REST_FRAMEWORK,  # base.py dagi sozlamalar meros bo‘ladi
    "DEFAULT_RENDERER_CLASSES": ("rest_framework.renderers.JSONRenderer",),
}
