from django.shortcuts import render
from django.http import request, HttpResponse

# Create your views here.

def web(request):
    return render(request, 'index.html')