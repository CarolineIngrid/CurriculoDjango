from django.shortcuts import render
from django.http import HttpResponse

def Info(request):
    return render(request, 'principal/index.html')
