from django import forms
from .models import Asistencia

class RegistroAsistencia(forms.ModelForm):
    class Meta:
        model=Asistencia
        fields='__all__'