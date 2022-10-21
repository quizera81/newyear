from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,"hello/index.html")
    

def kwizera(request):
    return HttpResponse("Hello Kwizera")

def david(request):
    return HttpResponse("Hello david")

def ghislain(request):
    return HttpResponse("Hello Ghislain")

def didier(request):
    return HttpResponse("Hello didier")

def manzi(request):
    return HttpResponse("hello Manzi")


def greet(request, name):
    return HttpResponse(f"Hello {name.capitalize()}")

