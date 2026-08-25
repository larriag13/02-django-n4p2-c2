from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def vista1(request):
    return HttpResponse("<h1>Vista 1 app2</h1>")

def vista2(request):
    return HttpResponse("<h1>Vista 2 app2</h1>")