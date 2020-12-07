from django import forms
from home.models import Alumno,Profesor

class RegistroAlumno(forms.ModelForm):
    class Meta:
        model=Alumno
        fields='__all__'