from django.shortcuts import render, redirect
from django.http import HttpResponse

from main.models import nba_players_21
#from forms import *

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

    # Create new columns to hold PER GAME STATS for categories which don't already have to simplify z score calc and display consistency
    df21['3PG'] = round((df21['3PA']*df21['3P%'])/df21['GP'], 2)
    df21['FTM'] = df21['FTA'] * df21['FT%']
    df21['FGA'] = (df21['2PA'] + df21['3PA']) / df21['GP']
    df21['FGM'] = ((df21['2PA'] * df21['2P%']) + (df21['3PA'] * df21['3P%'])) / df21['GP']
    df21['FG%'] = round(df21['FGM']/df21['FGA'],3)

    # Calculate total fantasy value based on 9-cat traditionally used
    # Formula based on z scores - adjust as needed
    # FUTURE ------------------------------------------------------------ Adjust formula to only consider checked categories
    df21['pointZ'] = stats.zscore(df21['PPG'])
    df21['assistZ'] = stats.zscore(df21['APG'])
    df21['reboundZ'] = stats.zscore(df21['RPG'])
    df21['stealZ'] = stats.zscore(df21['SPG'])
    df21['blockZ'] = stats.zscore(df21['BPG'])
    df21['turnoverZ'] = (-1)*stats.zscore(df21['TOPG'])             # negative stat so multiply by -1
    df21['threeZ'] = stats.zscore(df21['3PG'])
    # The ft% and fg% categories require a little more math to accurately portray their z scores/impact
    avgFT = np.average(df21['FT%'])  
    avgFG = np.average(df21['FG%'])  
    df21['ftImpact'] = (df21['FT%'] - avgFT) * (df21['FTA']/df21['GP'])
    df21['fgImpact'] = (df21['FG%'] - avgFG) * df21['FGA']                  # FGA is already per game as calc above
    df21['ftZ'] = stats.zscore(df21['ftImpact'])
    df21['fgZ'] = stats.zscore(df21['fgImpact'])
    zlist = ['pointZ', 'assistZ','reboundZ', 'stealZ', 'blockZ', 'turnoverZ', 'threeZ', 'ftZ', 'fgZ']
    df21['9 Cat Value'] = round(df21[zlist].sum(axis=1),2)
    df21['Punting Value'] = 0

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