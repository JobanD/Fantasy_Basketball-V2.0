from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import nba_players_21

# Create your views here.

def index(request):
    return render(request, 'main/index.html')       # Path is relative from templates directory
