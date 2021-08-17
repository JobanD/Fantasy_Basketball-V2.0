from django.shortcuts import render, redirect
from django.http import HttpResponse

from main.models import nba_players_21

# Create your views here.

def players(request):
    players21 = nba_players_21.objects.all()
    return render(request, 'players/players.html', {
        'players21': players21
    })