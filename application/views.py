from django.shortcuts import render


def index(request):
    # Copied from Lab 2 (NEEDS TO BE CHANGED)
    posts = [{"author": "Jimmy", "contents": "I am the coolest!"},
                  {"author": "Samiha", "contents": "I am even cooler!"}]
    return render(request, 'index.html', {"blog_posts": posts})

