"""Module for litereview views"""
from django.shortcuts import render


def index(request):
    """View for index page (AKA homepage)"""

    # Copied from Lab 2 (NEEDS TO BE CHANGED)
    posts = [{"author": "Jimmy", "contents": "I am the coolest!"},
             {"author": "Samiha", "contents": "I am even cooler!"}]
    return render(request, 'index.html', {"blog_posts": posts})


def signup_login(request):
    """View for Sign up/Login page"""
    return render(request, 'signup-login.html')


def userpage(request):
    """View for userpage"""
    return render(request, 'userpage.html')


def temp_review_modal(request):
    """Temporary view for rendering Create Review modal form"""
    return render(request, 'temp_review_modal.html')

