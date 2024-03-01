from django.shortcuts import render
from app.models import *
from app.forms import *
from django.http import HttpResponse

# Create your views here.
def insert_topic(request):
    ETFO=Topic_nameForm()
    d={'ETFO':ETFO}
    if request.method=='POST':
        ETFO=Topic_nameForm(request.POST)
        if ETFO .is_valid():
            tn=ETFO.cleaned_data['topic_name']
            To=Topic.objects.get_or_create(topic_name=tn)[0]
            To.save()
            return HttpResponse('Data is successFully....')
        else:
            return HttpResponse('invalid data....!')        
    return render(request,'insert_topic.html',d)

def Webpages_forms(request):
    EFDO=Webpagesforms()
    d={'EFDO':EFDO}
    if request.method =='POST':
        EFDO=Webpagesforms(request.POST)
        if EFDO.is_valid():
            tn=EFDO.cleaned_data['topic_name']
            To=Topic.objects.get(Topic_name=tn)
            na=EFDO.cleaned_data['name']
            u=EFDO.cleaned_data['url']
            WO=Webpage.objects.get_or_create(topic_name=To,name=na,url=u)[0]
            WO.save()
            return HttpResponse('Data is done.....')
        else:
            return HttpResponse('invalid data....')  

    return render(request,'Webpages_forms.html',d)

def Access_Record(request):
    AFDO=AccessRecordForm()
    d={'AFDO':AFDO}
    if request.method == 'POST':
        AFDO=AccessRecordForm(request.POST)
        if AFDO.is_valid():
            na=AFDO.cleaned_data['name']
            da=AFDO.cleaned_data['date']
            au=AFDO.cleaned_data['author']
            AC=AccessRecord.objects.get_or_create(name=na,date=da,author=au)[0]
            AC.save()
            return HttpResponse('Data is successfully....')
        else:
            return HttpResponse('invalid Data Records....')
    return render(request,'Access_Record.html',d)
