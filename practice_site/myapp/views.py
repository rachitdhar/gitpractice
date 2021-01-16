from django.shortcuts import render

# Create your views here.

# code below is supposed to be written by myself
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world, this is the index page!")

    # after this we create file urls.py to call this view and map it to a URL