from django import forms
from home.models import Alumno,Profesor

class RegistroAlumno(forms.ModelForm):
    class Meta:
        model=Alumno
        fields='__all__'

class RegistroProfesor(forms.ModelForm):
    class Meta:
        model=Profesor
        fields='__all__'