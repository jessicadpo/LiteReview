"""Module for defining models (i.e., SQLite3 database tables)"""
from django.db import models
from django.utils.translation import gettext_lazy as _

class User(models.Model):
    """Class for User database table"""
    username = models.CharField(max_length=64, blank=False, null=False)
    '''user defined username'''
    password = models.CharField(max_length=64, blank=False, null=False)
    '''user's password (hidden/encrypted? look into)'''
    email = models.EmailField(max_length=254, blank=False, null=False)
    '''user's email, NEEDS CORRESPONDING EMAILVALIDATOR'''


class Review(models.Model):
    """Class for Review database table"""
    class MediaTypes(models.TextChoices):
        """List of valid media types, each self-explanatory"""
        MOVIE = "MOV", _("Movie")
        BOOK = "BOK", _("Book")
        MANGA = "MGA", _("Manga/Manwha/Manhua")
        TVSHOW = "TVS", _("TV")
        MUSIC = "MUS", _("Music")
        COMIC = "COM", _("Comic/Graphic Novel")

    user_id = models.ForeignKey(User,on_delete=models.CASCADE, blank=False, null=False)
    '''foreign key set to the user that made the review'''
    title = models.CharField(max_length=128, blank=False, null=False)
    '''title of the work'''
    author = models.CharField(max_length=128, blank=False, null=False)
    '''main/relevant author of the work'''
    datetime = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    '''date and time of the review, set at creation'''
    rating = models.IntegerField(blank=False, null=False)
    '''rating given with the review'''
    text = models.CharField(max_length=1024, blank=False, null=False)
    '''main text of the review'''
    media_type = models.CharField(
        max_length=3,
        choices=MediaTypes,
        default=MediaTypes.MOVIE,
        blank=False,
        null=False)
    '''type of the media - refer to class MediaTypes'''
