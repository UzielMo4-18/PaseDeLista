from django.shortcuts import render
from django.views import View

# Create your views here.

class homeSc(View):
    def get(self,request):
        return render(request,'homescreen.html',{'prueba':10})