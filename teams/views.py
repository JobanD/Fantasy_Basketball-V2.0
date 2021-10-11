from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def teams(request):
    return render(request, 'teams.html')       # Path is relative from templates directory
