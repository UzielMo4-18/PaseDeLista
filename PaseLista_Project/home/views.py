from django.shortcuts import render,redirect
from django.views import View
from .models import Asistencia
from .forms import RegistroAsistencia

# Create your views here.

class homeSc(View):
    def get(self,request):
        asistencias=Asistencia.objects.all()
        contexto={'asistencias':asistencias}
        return render(request,'homescreen.html',contexto)

class AsistenciaAdd(View):
    def get(self,request):
        form=RegistroAsistencia()
        context={'form':form}
        return render(request,'asistencia.html',context)

    def post(self,request):
        form=RegistroAsistencia(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homeScr')
        else:
            form=RegistroAsistencia()
            context={'form':form}
            return render(request,'asistencia.html',context)

class AsistenciaUpdate(View):
    def get(self,request,id):
        asistencia_=Asistencia.objects.get(id=id)
        form=RegistroAsistencia(instance=asistencia_)
        context={'form':form}
        return render(request,'asistencia.html',context)

    def post(self,request,id):
        asistencia_=Asistencia.objects.get(id=id)
        form=RegistroAsistencia(request.POST,instance=asistencia_)
        if form.is_valid():
            form.save()
            return redirect('homeScr')
        else:
            context={'form':form}
            return render(request,'asistencia.html',context)