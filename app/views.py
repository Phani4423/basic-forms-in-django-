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