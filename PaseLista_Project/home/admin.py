from django.contrib import admin
from .models import Alumno,Profesor,Materia,Clase,Asistencia

# Register your models here.
admin.site.register(Alumno)
admin.site.register(Profesor)
admin.site.register(Materia)
admin.site.register(Clase)
admin.site.register(Asistencia)