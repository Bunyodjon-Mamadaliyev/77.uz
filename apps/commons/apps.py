from django.apps import AppConfig


class CommonsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.commons"

    def ready(self):
        pass
