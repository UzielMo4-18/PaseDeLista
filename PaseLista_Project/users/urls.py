#users/urls.py
from django.urls import path

from .views import *

urlpatterns=[
    path('',UsersSc.as_view(),name="UsersScr"),
    path('alumno/registrar',AlumnoAdd.as_view(),name="Alumno_add"),
    path('alumno/<int:id>/',AlumnoUpdate.as_view(),name="Alumno_update"),
    path('alumno/delete/<int:id>/',AlumnoDelete.as_view(),name="Alumno_delete"),
    path('profesor/registrar',ProfesorAdd.as_view(),name="Profesor_add"),
    path('profesor/<int:id>/',ProfesorUpdate.as_view(),name="Profesor_update"),
    path('profesor/delete/<int:id>/',ProfesorDelete.as_view(),name="Profesor_delete"),
]