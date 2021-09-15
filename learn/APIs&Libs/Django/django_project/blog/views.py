from django.shortcuts import render
# added code here ep 2 Apps and Routes
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Blog Home</h1>')