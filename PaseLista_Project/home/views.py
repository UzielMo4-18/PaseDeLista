from django.shortcuts import render
from django.views import View
from .models import Asistencia

# Create your views here.

class homeSc(View):
    def get(self,request):
        asistencias=Asistencia.objects.all()
        contexto={'asistencias':asistencias}
        return render(request,'homescreen.html',contexto)