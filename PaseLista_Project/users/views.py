from django.shortcuts import render
from django.views import View
from home.models import Alumno,Profesor

# Create your views here.

class UsersSc(View):
    def get(self,request):
        alumnos=Alumno.objects.all()
        profesores=Profesor.objects.all()
        contexto={'alumnos':alumnos,'profesores':profesores}
        return render(request,'users.html',contexto)