from django.shortcuts import render
from django.views import View

from .models import *
class Home(View):
    def get(self,request):
        data={
            'data':Bolim.objects.all()
        }
        return render(request,'index.html',data)

class SozlarView(View):
    def get(self,request,pk):
        soz=Sozlar.objects.filter(bolim_fk__id=pk)
        data={
            'soz':soz
        }
        return render(request,'theme.html',data)

class OneSozView(View):
    def get(self,request,pk):
        one_soz=Sozlar.objects.get(id=pk)
        data={
            'one_soz':one_soz
        }
        return render(request,'workspace.html',data)

