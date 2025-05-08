from django.apps import AppConfig


class UserAuthsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user_auths'

    def ready(self):
        import user_auths.signals
