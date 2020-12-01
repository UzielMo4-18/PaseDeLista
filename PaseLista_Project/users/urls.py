#users/urls.py
from django.urls import path

from .views import *

urlpatterns=[
    path('',UsersSc.as_view(),name="UsersScr")
]