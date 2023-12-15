from django.shortcuts import render
from django.http import HttpResponse

# VIEW HELLO   
def hello(request):
    return HttpResponse('<h1>Hello App django in live.</h1>')

# VIEW HOME
def home(request):
    return HttpResponse('<h1> Home page. </h1>')