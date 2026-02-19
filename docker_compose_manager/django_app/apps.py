"""Django app configuration."""

from django.apps import AppConfig


class DjangoAppConfig(AppConfig):
    """Configuration for Django app."""
    
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'docker_compose_manager.django_app'
    verbose_name = 'Docker Compose Manager'
