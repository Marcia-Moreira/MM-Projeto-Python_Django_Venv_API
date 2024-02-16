from django.apps import AppConfig


class BaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    verbose_name = 'Módulo Geral'
    # Vai trocar o nome base por módulo geral
    name = 'base'

