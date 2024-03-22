"""Module for litereview views"""
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Review
from .logger import Logger
from .forms import SignUpForm, LoginForm, CreateReviewForm

#########################################################################
# PLACEHOLDER RECORDS (DELETE BEFORE SUBMIT)

# pylint: disable=pointless-string-statement
# Will be deleted before submit anyway
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
    if request.method == 'POST':
        create_review(request)

    # Retrieve data from database
    # Disabling pylint check for Review.objects because this is how it works in Django
    all_reviews = Review.objects.all()  # pylint: disable=no-member
    all_users = User.objects.all()

    review_list = []
    twenty_most_recent_reviews = all_reviews.order_by('-id')[:20:1]
    for review in twenty_most_recent_reviews:
        user_id = review.user_id_id
        username = all_users.get(pk=user_id).username
        media_type = review.get_media_type_display()
        media_type_icon = Icon.get_media_icon(Icon(), review.media_type)
        full_record = {"username": username, "review": review, "media_type": media_type,
                       "media_type_icon": media_type_icon}
        review_list.append(full_record)

    review_form = CreateReviewForm()

    return render(request, 'homepage.html',
                  {"review_list": review_list, "review_form": review_form})


def signup_login(request):
    """View for Sign up/Login page"""
    # NOTE: USERNAMES MUST BE UNIQUE
    if request.method == 'POST':
        if 'signup-submit' in request.POST:
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password1')
                user = authenticate(request, username=username, password=password)
                login(request, user)
                return redirect("user-profile-page", username=username)
            forms = {"signup_form": form, "login_form": LoginForm()}
            return render(request, 'signup-login.html', {'forms': forms})

        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect("user-profile-page", username=username)
        forms = {"signup_form": SignUpForm(), "login_form": form}
        return render(request, 'signup-login.html', {'forms': forms})
    forms = {"signup_form": SignUpForm(), "login_form": LoginForm()}
    return render(request, 'signup-login.html', {'forms': forms})


def logout_view(request):
    """View for Logout Functionality"""
    logout(request)
    return redirect("homepage")


def userpage(request, username):
    """View for userpage"""
    if request.method == 'POST':
        create_review(request)

    curr_user_id = User.objects.get(username=username).id
    user_reviews = Review.objects.filter(user_id=curr_user_id).order_by('-datetime')  # pylint: disable=no-member
    review_list = []
    for review in user_reviews:
        username = username  # pylint: disable=self-assigning-variable
        media_type = review.get_media_type_display()
        media_type_icon = Icon.get_media_icon(Icon(), review.media_type)
        full_record = {"username": username, "review": review, "media_type": media_type,
                       "media_type_icon": media_type_icon}
        review_list.append(full_record)

    review_form = CreateReviewForm()
    return render(request, 'userpage.html',
                  {"review_list": review_list, "review_form": review_form})


def create_review(request):
    """Function (used by views) to create a review"""
    if 'create-review-submit' in request.POST:
        form = CreateReviewForm(request.POST)
        if form.is_valid():
            # Need: user_id, title, author, status, rating, text, media_type
            user_id = request.user.id
            title = form.cleaned_data['title']
            author = form.cleaned_data['creator']
            rating = form.cleaned_data['rating']
            text = form.cleaned_data['text']
            media_type = form.cleaned_data['media_type']
            status = form.cleaned_data['status']
            review = Review(user_id_id=user_id, title=title, author=author,
                            rating=rating, text=text, media_type=media_type, status=status)
            review.save()


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
            "MOV": "../static/icons/MOV.png",
            "BOK": "../static/icons/BOK.png",
            "MGA": "../static/icons/MGA.png",
            "TVS": "../static/icons/TVS.png",
            "MUS": "../static/icons/MUS.png",
            "COM": "../static/icons/COM.png"
        }
        if isinstance(media_name, str) is False:
            raise TypeError  # Function stops here if error occurs
        if media_name not in icon_paths:
            raise KeyError  # Function stops here if error occurs
        icon_path = icon_paths.get(media_name)
        self.logger.log_message(f"Retrieved link to icon for media type {media_name} = {icon_path}")
        return icon_path
