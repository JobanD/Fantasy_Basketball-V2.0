# Handle all predictive analysis here to use throughout app

# Models
from main.models import nba_players_21
from main.models import nba_players_20
from main.models import nba_players_19
from main.models import nba_players_18

# Imports
import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

from . import predictionFunctions as pfunc      # functions for ease of use

players21 = nba_players_21.objects.all().values_list()      # fetch all instances of this db as values
df21 = pd.DataFrame.from_records(players21)                 # Turn django queryset into pandas dataframe for data manipulation
df21_norm = pfunc.normalize_df(df21)

players20 = nba_players_20.objects.all().values_list()   
df20 = pd.DataFrame.from_records(players20)              

players19 = nba_players_19.objects.all().values_list()  
df19 = pd.DataFrame.from_records(players19)                

players18 = nba_players_18.objects.all().values_list()
df18 = pd.DataFrame.from_records(players18)
