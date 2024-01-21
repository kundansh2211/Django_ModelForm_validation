from django.apps import AppConfig


class CustomValidatorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'custom_clean_method_validator'
