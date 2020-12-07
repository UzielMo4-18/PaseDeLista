#home/urls.py
from django.urls import path

from .views import *

urlpatterns=[
    path('',homeSc.as_view(),name="homeScr"),
    path('asistencia/registrar',AsistenciaAdd.as_view(),name="Asi_add"),
    path('asistencia/<int:id>/',AsistenciaUpdate.as_view(),name="Asi_update"),
]