"""Module for defining models (i.e., SQLite3 database tables)"""
from django.db import models


class User(models.Model):
    """Class for User database table"""
    username = models.CharField(max_length=64, blank=False, null=False)
    '''user defined username'''
    password = models.CharField(max_length=64, blank=False, null=False)
    '''user's password (hidden/encrypted? look into)'''
    email = models.EmailField(max_length=254, blank=False, null=False)
    '''user's email, NEEDS CORRESPONDING EMAILVALIDATOR'''

class Reveiw(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE, blank=False, null=False)

