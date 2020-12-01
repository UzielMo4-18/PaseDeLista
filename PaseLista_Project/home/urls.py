#home/urls.py
from django.urls import path

from .views import *

urlpatterns=[
    path('',homeSc.as_view(),name="homeScr")
]