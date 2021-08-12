from django.shortcuts import render, redirect
from django.http import HttpResponse
from nba_api.stats.static import players

# Create your views here.

def index(request):
    return render(request, 'index.html')