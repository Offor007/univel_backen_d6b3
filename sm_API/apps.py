from django.apps import AppConfig


class SmApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sm_API'
    
    # def ready(self):
    #    from . import signals
