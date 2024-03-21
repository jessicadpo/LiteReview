"""Module for defining models (i.e., SQLite3 database tables)"""
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


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

    class ProgressStatus(models.TextChoices):
        """List of valid completion statuses"""
        COMPLETE = "Complete"
        IN_PROGRESS = "In Progress"
        DROPPED = "Dropped"

    user_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    '''foreign key set to the user that made the review'''
    title = models.CharField(max_length=128, blank=False, null=False)
    '''title of the work'''
    author = models.CharField(max_length=128, blank=False, null=False)
    '''main/relevant author of the work'''
    datetime = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    '''progress status'''
    status = models.CharField(max_length=128, choices=ProgressStatus.choices,
                              default="In Progress", blank=False, null=False)
    '''date and time of the review, set at creation'''
    rating = models.IntegerField(null=True)
    '''rating given with the review'''
    text = models.CharField(max_length=9999, null=True)
    '''main text of the review'''
    media_type = models.CharField(
        max_length=3,
        choices=MediaTypes.choices,
        default=MediaTypes.MOVIE,
        blank=False,
        null=False)
    '''type of the media - refer to class MediaTypes'''
