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
    
    # Merge tables into master table
    merged_df = pd.concat([df21_norm, df20_norm, df19_norm, df18_norm], axis=0)
    
    # merged_df = pfunc.clean(merged_df)
    merged_df = merged_df.dropna(how='any')
    min_gp = 10
    merged_df = merged_df[merged_df['GP'] > min_gp]
    
    
    # Create html table(s) for displaying
    df21finalNorm = df21_norm.to_html(index=False, justify='center', columns = [
        'Index','Season_ID', 'Name', 'Team', 'Position', 'GP', 'MPG', 'PPG', 'APG', 'RPG', 'SPG', 'BPG', 'FTp', 'TOPG', 'PPG_norm'
    ])
    df20finalNorm = df20_norm.to_html(index=False, justify='center', columns = [
        'Index', 'Season_ID', 'Name', 'Team', 'Position', 'GP', 'MPG', 'PPG', 'APG', 'RPG', 'SPG', 'BPG', 'FTp', 'TOPG', 'PPG_norm'
    ])
    
    testing_player = "Stephen Curry"
    
    test = pfunc.compare(testing_player, "2020-21", merged_df)
    
    projected_stats = pfunc.project_stats(testing_player, '2020-21', merged_df)
    
    # numpy_compare = np.array(test)
    # df_compare = pd.DataFrame(numpy_compare, columns=["Name", "Season", "Difference", "Percent Error"])
    
    df_compare_final = test.to_html(index=False, justify='center', columns = [
        "Name", "Season_ID", "Distance", 'PPG', 'APG', 'RPG', 'SPG', 'BPG', 'TOPG'
    ])
    
    df_projected_stats = projected_stats.to_html(index=False, justify='center', columns = [
        'Name', 'Projected Season', 'Projected_PPG', 'Projected_APG', 'Projected_RPG', 'Projected_SPG', 'Projected_BPG', 'Projected_TOPG'
    ])
    
    
    context = {
        'df21': df21,
        'df21_norm': df21_norm,
        'df21finalNorm': df21finalNorm,
        'df20finalNorm': df20finalNorm,
        'df_compare_final': df_compare_final,
        'df_projected_stats': df_projected_stats,
        'testing_player': testing_player}
    return render(request, 'main/index.html', context)       # Path is relative from templates directory
