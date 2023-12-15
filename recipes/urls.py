from django.urls import path
from recipes.views import *

urlpatterns = [
    path('hello/', hello),
    path('', home)
]
