from django.shortcuts import render
from django.views import View
from home.models import Alumno,Profesor,Materia

# Create your views here.

class UsersSc(View):
    def get(self,request):
        alumnos=Alumno.objects.all()
        profesores=Profesor.objects.all()
        materias_profesor=Materia.objects.all()
        auxpr=[]
        for pr in profesores: auxpr.append(pr.id)
        print(auxpr)
        contexto={'alumnos':alumnos,'profesores':profesores,'materias_profesor':materias_profesor,'auxpr':auxpr}
        return render(request,'users.html',contexto)