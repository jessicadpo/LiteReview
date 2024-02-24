"""Module for defining models (i.e., SQLite3 database tables)"""
from django.db import models


class User(models.Model):
    """Class for User database table"""
    usr_id = models.IntegerField(primary_key=True)
    '''unique user id (auto-generated? look into)'''
    usr_name = models.CharField(max_length=64)
    '''user defined username'''
    password = models.CharField(max_length=64)
    '''user's password (hidden/encrypted? look into)'''
    email = models.EmailField(max_length=254)
    '''user's email, NEEDS CORRESPONDING EMAILVALIDATOR '''
    