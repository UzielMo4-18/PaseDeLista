from django.shortcuts import render
from django.views import View
from home.models import Materia,Clase

# Create your views here.

class SubjectsSc(View):
    def get(self,request):
        materias=Materia.objects.all()
        clases=Clase.objects.all()
        contexto={'materias':materias,'clases':clases}
        return render(request,'subjects.html',contexto)