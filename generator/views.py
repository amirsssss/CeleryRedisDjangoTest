from django.shortcuts import render
from .models import GeneratorModel
# Create your views here.



def LastData(request,*args,**kwargs):
    data=GeneratorModel.objects.all()
    # print(data)
    # if len(data)>1:
    #     lastdata=data[len(data)-1]
    # else:
    #     lastdata=-1
    return render(request,"generator/visu.html",context={'data':data})
