from django.db.models.indexes import Index
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Models
from main.models import nba_players_21
from main.models import nba_players_20
from main.models import nba_players_19
from main.models import nba_players_18

# Imports
import pandas as pd
import numpy as np
import scipy.stats as stats
#import matplotlib.pyplot as plt

from . import predictionFunctions as pfunc      # functions for ease of use

# Create your views here.

def index(request):
    players21 = nba_players_21.objects.all().values_list()      # fetch all instances of this db as values
    df21 = pd.DataFrame.from_records(players21)                 # Turn django queryset into pandas dataframe for data manipulation
    
    players20 = nba_players_20.objects.all().values_list()   
    df20 = pd.DataFrame.from_records(players20)     

    players19 = nba_players_19.objects.all().values_list()  
    df19 = pd.DataFrame.from_records(players19)          

    players18 = nba_players_18.objects.all().values_list()
    df18 = pd.DataFrame.from_records(players18)
    
    # Give each dataframe header columns
    df21.columns = [
        'Index', 'Name', 'Team', 'Position', 'Age', 
        'GP', 'MPG', 'MINp', 'Usage', 'TO Rate', 
        'FTA', 'FTp', 'FGA2', 'FG2p', 'FGA3', 
        'FG3p', 'EFG', 'TS', 'PPG', 'RPG', 
        'TRBp', 'APG', 'ASTp', 'SPG', 'BPG', 
        'TOPG', 'VIV', 'ORTG', 'DRTG'
    ]
    df20.columns = [
        'Index', 'Name', 'Team', 'Position', 'Age', 
        'GP', 'MPG', 'MINp', 'Usage', 'TO Rate', 
        'FTA', 'FTp', 'FGA2', 'FG2p', 'FGA3', 
        'FG3p', 'EFG', 'TS', 'PPG', 'RPG', 
        'TRBp', 'APG', 'ASTp', 'SPG', 'BPG', 
        'TOPG', 'VIV', 'ORTG', 'DRTG'
    ]
    df19.columns = [
        'Index', 'Name', 'Team', 'Position', 'Age', 
        'GP', 'MPG', 'MINp', 'Usage', 'TO Rate', 
        'FTA', 'FTp', 'FGA2', 'FG2p', 'FGA3', 
        'FG3p', 'EFG', 'TS', 'PPG', 'RPG', 
        'TRBp', 'APG', 'ASTp', 'SPG', 'BPG', 
        'TOPG', 'VIV', 'ORTG', 'DRTG'
    ]
    df18.columns = [
        'Index', 'Name', 'Team', 'Position', 'Age', 
        'GP', 'MPG', 'MINp', 'Usage', 'TO Rate', 
        'FTA', 'FTp', 'FGA2', 'FG2p', 'FGA3', 
        'FG3p', 'EFG', 'TS', 'PPG', 'RPG', 
        'TRBp', 'APG', 'ASTp', 'SPG', 'BPG', 
        'TOPG', 'VIV', 'ORTG', 'DRTG'
    ]
    
    # Normalize dataframes and give season id columns for future merging
    # Normalizing is important because pace and other factors play a role in nba statistics across seasons and the discrepancy should be accounted for
    df21_norm = pfunc.normalize_df(df21)
    df21_norm.insert(1,"Season_ID", "2020-21")
    
    df20_norm = pfunc.normalize_df(df20)
    df20_norm.insert(1,"Season_ID", "2019-20")
    
    df19_norm = pfunc.normalize_df(df19)
    df19_norm.insert(1,"Season_ID", "2018-19")
    
    df18_norm = pfunc.normalize_df(df18)
    df18_norm.insert(1,"Season_ID", "2017-18")
    
    
    # Create html table(s) for displaying
    df21finalNorm = df21_norm.to_html(index=False, justify='center', columns = [
        'Index','Season_ID', 'Name', 'Team', 'Position', 'GP', 'MPG', 'PPG', 'APG', 'RPG', 'SPG', 'BPG', 'FTp', 'TOPG', 'PPG_norm'
    ])
    df20finalNorm = df20_norm.to_html(index=False, justify='center', columns = [
        'Index', 'Season_ID', 'Name', 'Team', 'Position', 'GP', 'MPG', 'PPG', 'APG', 'RPG', 'SPG', 'BPG', 'FTp', 'TOPG', 'PPG_norm'
    ])
    
    
    test = pfunc.compare("Bradley Beal", "2020-21", df21_norm)
    
    numpy_compare = np.array(test)
    df_compare = pd.DataFrame(numpy_compare, columns=["Name", "Season", "Difference", "Percent Error"])
    
    df_compare_final = df_compare.to_html(index=False, justify='center', columns = [
        "Name", "Season", "Difference", "Percent Error"
    ])
    
    
    context = {'df21': df21, 'df21_norm': df21_norm, 'df21finalNorm': df21finalNorm, 'df20finalNorm': df20finalNorm, 'df_compare_final': df_compare_final}
    return render(request, 'main/index.html', context)       # Path is relative from templates directory
