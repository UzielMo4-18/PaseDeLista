from django import forms
from home.models import Materia,Clase

class RegistroMateria(forms.ModelForm):
    class Meta:
        model=Materia
        fields='__all__'

class RegistroClase(forms.ModelForm):
    class Meta:
        model=Clase
        fields='__all__'