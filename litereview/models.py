"""Module for defining models (i.e., SQLite3 database tables)"""
from django.db import models


class User(models.Model):
    """Class for User database table"""
    usr_id = models.IntegerField(primary_key=True)
    usr_name =
    full_name =
    password =
    email = 
