"""Configuration file for Django app"""
from django.apps import AppConfig


class PostsConfig(AppConfig):
    """Class for implementing app configuration"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'litereview'
