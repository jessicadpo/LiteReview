"""Module for litereview views"""
from django.shortcuts import render


def homepage(request):
    """View for index page (AKA homepage)"""
    return render(request, 'homepage.html')


def signup_login(request):
    """View for Sign up/Login page"""
    return render(request, 'signup-login.html')


def userpage(request):
    """View for userpage"""
    return render(request, 'userpage.html')


def temp_review_modal(request):
    """Temporary view for rendering Create Review modal form"""
    return render(request, 'temp_review_modal.html')

def temp_account_modal(request):
    """Temporary view for rendering Create Review modal form"""
    return render(request, 'temp_account_modal.html')
