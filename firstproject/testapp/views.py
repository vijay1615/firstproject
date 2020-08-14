from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def welcome(request):
    s='<h1>welcome to djangoproject</h1>'
    return HttpResponse(s)
