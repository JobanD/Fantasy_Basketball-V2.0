from django.shortcuts import render, redirect
from django.http import HttpResponse

from main.models import nba_players_21
#from forms import *

from . import fantasy_math as fm

import pandas as pd
import numpy as np
import scipy.stats as stats

def players(request):
    players21 = nba_players_21.objects.all().values_list()      # fetch all instances of this db as values
    df21 = pd.DataFrame.from_records(players21)                 # Turn django queryset into pandas dataframe for data manipulation
    
    # Add column names to model data
    df21.columns = [
        'Index', 'Name', 'Team', 'Position', 'Age', 
        'GP', 'MPG', 'MIN%', 'Usage', 'TO Rate', 
        'FTA', 'FT%', '2PA', '2P%', '3PA', 
        '3P%', 'EFG', 'TS', 'PPG', 'RPG', 
        'TRB%', 'APG', 'AST%', 'SPG', 'BPG', 
        'TOPG', 'VIV', 'ORTG', 'DRTG'
    ]

    fm.per_game(df21)               # From fantasy_math.py
    fm.create_z_scores(df21)
    fm.create_fantasy_value(df21)

    # Calc fantasy value based on z scores and selected categories
    if request.method == 'POST':
        cats = request.POST.getlist('categories')
        for i in cats:
            df21['Punting Value'] += df21[i]
        df21['Punting Value'] = round(df21['Punting Value'], 2)

    df21['Punt Difference'] = df21['Punting Value'] - df21['9 Cat Value']

    df21_Zscores = df21.to_html(index=False, justify='center', columns = [
        'Name', 'Team', 'Position', 'GP', 'MPG', 'pointZ', 'assistZ', 'reboundZ', 'stealZ', 'blockZ', 'turnoverZ', 'threeZ',
        'ftZ', 'fgZ'
    ])
    df21final = df21.to_html(index=False, justify='center', columns = [
        'Name', 'Team', 'Position', 'GP', 'MPG', 'PPG', 'APG', 'RPG', 'SPG', 'BPG', '3PG', 'FG%', 'FT%', 'TOPG', '9 Cat Value',
        'Punting Value', 'Punt Difference'
    ])

    context = {'players21': players21, 'df21final': df21final, 'df21_Zscores': df21_Zscores}
    return render(request, 'players/players.html', context)