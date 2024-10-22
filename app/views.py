from django.shortcuts import render
from django.http import HttpResponse
from app.models import *

# Create your views here.
def base(request):
    if request.method == 'POST':
        tn = request.POST['tn']
        TO = topic.objects.get_or_create(topic_name = tn)
        return HttpResponse('inserted')
    
    
def display(request):
    litn = topic.objects.all()
    d = {'litn':litn}
    return render(request,'display.html',d)
def insert_webpage(request):
    LTO = topic.objects.all()
    d = {'LTO':LTO}
    if request.method == 'POST':
        tn = request.POST['tn']
        name = request.POST['name']
        email= request.POST['email']
        url = request.POST['url']
        TO = topic.objects.get(topic_name = tn)
        wo = webpage.objects.get_or_create(topic_name = TO,name = name,email = email,url = url)
        return HttpResponse('webpage is created ')
    
    return render(request,'insert_webpage.html',d)
def select_multiple(request):
    LTO = topic.objects.all()
    d = {'LTO':LTO}
    if request.method == 'POST':
        MTN = request.POST.getlist('tn')
        EQST = webpage.objects.none()
        for topi in MTN:
            EQST = EQST|webpage.objects.filter(topic_name = topi)
        d1 = {'EQST':EQST}
        return render(request,'display_webpage.html',d1)
    return render(request,'select_multiple.html',d)