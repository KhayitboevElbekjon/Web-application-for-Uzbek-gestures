from django.http import HttpResponse, FileResponse
from django.shortcuts import render, get_object_or_404
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


def down(request):
    soz={'bolim':Bolim.objects.all()

         }
    return render(request,'down.html',soz)
def KopSozlar(request,pk):
    data={
        'data':Sozlar.objects.filter(bolim_fk__id=pk),
        'bolim':Sozlar.objects.filter(bolim_fk__id=pk).last()
    }
    return render(request,'Download.html',data)
def download(request, id):
    obj = Sozlar.objects.get(id=id)
    filename = obj.gif.path
    response = FileResponse(open(filename, 'rb'))
    return response