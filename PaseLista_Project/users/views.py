from django.shortcuts import render
from django.views import View

# Create your views here.

class UsersSc(View):
    def get(self,request):
        return render(request,'users.html',{'palabra':'hola'})