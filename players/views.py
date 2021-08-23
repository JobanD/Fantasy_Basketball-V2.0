from django.shortcuts import render, redirect
from django.http import HttpResponse

from main.models import nba_players_21

# Create your views here.

def players(request):
    players21 = nba_players_21.objects.all()       # fetch all instances of this db
    context = {'players21': players21}
    return render(request, 'players/players.html', context)