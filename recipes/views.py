from django.shortcuts import render
from django.http import HttpResponse

# VIEW HELLO   
def hello(request):
    return render(request, 'temp/hello.html')

# VIEW HOME
def home(request):
    return render(request, 'temp/home.html')