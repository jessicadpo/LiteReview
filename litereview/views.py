"""Module for litereview views"""
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Review
from .logger import Logger

#########################################################################
# PLACEHOLDER RECORDS (DELETE BEFORE SUBMIT)

# pylint: disable=pointless-string-statement
# Will be deleted before submit anyways
'''
PLACEHOLDER RECORDS -- DO NOT UNCOMMENT (already created in database)
user1 = User(username='JSmith2000', password='password123',
             email='jsmith@gmail.com')
user1.save()

review1 = Review(user_id_id=1, title='Placeholder book', author='John Smith',
                 datetime='01/01/2024', rating=8, text='fdshklfsaldkfjsdalkfjsdalkfs',
                 media_type="BOK")
review1.save()
'''
#########################################################################


def homepage(request):
    """View for index page (AKA homepage)"""
    # Retrieve data from database
    # Disabling pylint check for Review.objects because this is how it works in Django
    all_reviews = Review.objects.all()  # pylint: disable=no-member
    all_users = User.objects.all()

    review_list = []
    twenty_most_recent_reviews = all_reviews.order_by('-id')[:20:-1]
    for review in twenty_most_recent_reviews:
        user_id = review.user_id_id
        username = all_users.get(pk=user_id).username
        media_type = review.get_media_type_display()
        media_type_icon = Icon.get_media_icon(Icon(), review.media_type)
        full_record = {"username": username, "review": review, "media_type": media_type,
                       "media_type_icon": media_type_icon}
        review_list.append(full_record)

    return render(request, 'homepage.html', {"review_list": review_list})


def signup_login(request):
    """View for Sign up/Login page"""

    # NOTE: USERNAMES MUST BE UNIQUE (dk how to modify Django's premade constraints
    # and I don't care to)
    return render(request, 'signup-login.html')


def userpage(request, username):
    """View for userpage"""
    print(username)
    # This is to make pylint shut up about unused username parameter for now
    # Replace with the code later
    return render(request, 'userpage.html')


class Icon:  # pylint: disable=too-few-public-methods
    """
    Needs to be a class for integration testing.
    Disabling pylint error since the only reason I'm making this a class
    is due to prof's requirements for automated tests
    """
    def __init__(self):
        self.logger = Logger()

    def get_media_icon(self, media_name):
        """media_name is a string with the values MOV, BOK, MGA, TVS, MUS, or COM"""
        icon_paths = {
            "MOV": "../static/icons/MOV.svg",
            "BOK": "../static/icons/BOK.svg",
            "MGA": "../static/icons/MGA.svg",
            "TVS": "../static/icons/TVS.svg",
            "MUS": "../static/icons/MUS.svg",
            "COM": "../static/icons/COM.svg"
        }
        if isinstance(media_name, str) is False:
            raise TypeError  # Function stops here if error occurs
        if media_name not in icon_paths:
            raise KeyError  # Function stops here if error occurs
        icon_path = icon_paths.get(media_name)
        self.logger.log_message(f"Retrieved link to icon for media type {media_name} = {icon_path}")
        return icon_path
