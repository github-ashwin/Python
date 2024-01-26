from django.shortcuts import render
from django.http import HttpResponse #importing http module
# Create your views here.

def displayhello(request):
    return HttpResponse("hello django")

