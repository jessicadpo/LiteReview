"""Module for litereview views"""
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Review  # import all models

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
        full_record = {"username": username, "review": review}
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


def temp_review_modal(request):
    """Temporary view for rendering Create Review modal form"""
    return render(request, 'temp_review_modal.html')

def temp_account_modal(request):
    """Temporary view for rendering Create Review modal form"""
    return render(request, 'temp_account_modal.html')
