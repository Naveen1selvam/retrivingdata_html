from django.shortcuts import render

# Create your views here.
from app.models import *
def displaytopic(request):
    LOT=Topic.objects.all()
    d={'topic':LOT}
    return render(request,'displaytopic.html',d)
def displayweb(request):
    LOW=webpage.objects.all()
    d={'web':LOW}
    return render(request,'displayweb.html',d)
def displayacc(request):
    LOA=Accrec.objects.all()
    d={'access':LOA}
    return render(request,'displayacc.html',d)