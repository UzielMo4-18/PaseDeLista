from django.shortcuts import render,redirect
from django.views import View
from home.models import Alumno,Profesor,Materia
from .forms import RegistroAlumno,RegistroProfesor

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

class AlumnoAdd(View):
    def get(self,request):
        form=RegistroAlumno()
        context={'form':form}
        return render(request,'alumno.html',context)
    
    def post(self,request):
        form=RegistroAlumno(request.POST)
        if form.is_valid():
            form.save()
            return redirect('UsersScr')
        else:
            form=RegistroAlumno()
            context={'form':form}
            return render(request,'alumno.html',context)

class AlumnoUpdate(View):
    def get(self,request,id):
        alumno=Alumno.objects.get(id=id)
        form=RegistroAlumno(instance=alumno)
        context={'form':form}
        return render(request,'alumno.html',context)
    
    def post(self,request,id):
        alumno=Alumno.objects.get(id=id)
        form=RegistroAlumno(request.POST,instance=alumno)
        if form.is_valid():
            form.save()
            return redirect('UsersScr')
        else:
            context={'form':form}
            return render(request,'alumno.html',context)

class ProfesorAdd(View):
    def get(self,request):
        form=RegistroProfesor()
        context={'form':form}
        return render(request,'profesor.html',context)
    
    def post(self,request):
        form=RegistroProfesor(request.POST)
        if form.is_valid():
            form.save()
            return redirect('UsersScr')
        else:
            form=RegistroProfesor()
            context={'form':form}
            return render(request,'profesor.html',context)

class ProfesorUpdate(View):
    def get(self,request,id):
        profesor_=Profesor.objects.get(id=id)
        form=RegistroProfesor(instance=profesor_)
        context={'form':form}
        return render(request,'profesor.html',context)
    
    def post(self,request,id):
        profesor_=Profesor.objects.get(id=id)
        form=RegistroProfesor(request.POST,instance=profesor_)
        if form.is_valid():
            form.save()
            return redirect('UsersScr')
        else:
            context={'form':form}
            return render(request,'profesor.html',context)