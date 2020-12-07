from django.shortcuts import render,redirect
from django.views import View
from home.models import Materia,Clase
from .forms import RegistroMateria,RegistroClase

# Create your views here.

class SubjectsSc(View):
    def get(self,request):
        materias=Materia.objects.all()
        clases=Clase.objects.all()
        contexto={'materias':materias,'clases':clases}
        return render(request,'subjects.html',contexto)

class MateriaAdd(View):
    def get(self,request):
        form=RegistroMateria()
        context={'form':form}
        return render(request,'materia.html',context)
    
    def post(self,request):
        form=RegistroMateria(request.POST)
        if form.is_valid():
            form.save()
            return redirect('SubjectsScr')
        else:
            form=RegistroMateria()
            context={'form':form}
            return render(request,'materia.html',context)

class MateriaUpdate(View):
    def get(self,request,id):
        materia_=Materia.objects.get(id=id)
        form=RegistroMateria(instance=materia_)
        context={'form':form}
        return render(request,'materia.html',context)
    
    def post(self,request,id):
        materia_=Materia.objects.get(id=id)
        form=RegistroMateria(request.POST,instance=materia_)
        if form.is_valid():
            form.save()
            return redirect('SubjectsScr')
        else:
            context={'form':form}
            return render(request,'materia.html',context)

class ClaseAdd(View):
    def get(self,request):
        form=RegistroClase()
        context={'form':form}
        return render(request,'clase.html',context)
    
    def post(self,request):
        form=RegistroClase(request.POST)
        if form.is_valid():
            form.save()
            return redirect('SubjectsScr')
        else:
            form=RegistroClase()
            context={'form':form}
            return render(request,'clase.html',context)

class ClaseUpdate(View):
    def get(self,request,id):
        clase_=Clase.objects.get(id=id)
        form=RegistroClase(instance=clase_)
        context={'form':form}
        return render(request,'clase.html',context)
    
    def post(self,request,id):
        clase_=Clase.objects.get(id=id)
        form=RegistroClase(request.POST,instance=clase_)
        if form.is_valid():
            form.save()
            return redirect('SubjectsScr')
        else:
            context={'form':form}
            return render(request,'clase.html',context)