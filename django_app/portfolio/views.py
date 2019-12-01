from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request,  'home.html',{'name':'Keny Singh'})
def add(request):
    result = int(request.POST['num1'])+int(request.POST['num2'])
    return render(request,'result.html',{'result':result})