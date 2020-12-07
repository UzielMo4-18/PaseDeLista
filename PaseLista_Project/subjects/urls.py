#subjects/urls.py
from django.urls import path

from .views import *

urlpatterns=[
    path('',SubjectsSc.as_view(),name="SubjectsScr"),
    path('materia/registrar',MateriaAdd.as_view(),name="Materia_add"),
    path('materia/<int:id>/',MateriaUpdate.as_view(),name="Materia_update"),
    path('clase/registrar',ClaseAdd.as_view(),name="Clase_add"),
    path('clase/<int:id>/',ClaseUpdate.as_view(),name="Clase_update"),
]