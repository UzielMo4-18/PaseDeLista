#subjects/urls.py
from django.urls import path

from .views import *

urlpatterns=[
    path('',SubjectsSc.as_view(),name="SubjectsScr")
]