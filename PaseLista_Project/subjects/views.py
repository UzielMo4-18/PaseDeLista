from django.shortcuts import render
from django.views import View

# Create your views here.

class SubjectsSc(View):
    def get(self,request):
        variable=True
        return render(request,'subjects.html',{'valor':variable})