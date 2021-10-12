import pandas as pd
import numpy as np
import scipy.stats as stats

## Functions to create new column data, calc z scores, determine fantasy/punt values for players page

# Take dataframe as param, convert stats to per game and create a field goal percentage column
def per_game(df):
    # Create new columns to hold PER GAME STATS for categories which don't already have to simplify z score calc and display consistency
    df['3PG'] = round((df['3PA']*df['3P%'])/df['GP'], 2)
    df['FTM'] = df['FTA'] * df['FT%']
    df['FGA'] = (df['2PA'] + df['3PA']) / df['GP']
    df['FGM'] = ((df['2PA'] * df['2P%']) + (df['3PA'] * df['3P%'])) / df['GP']
    df['FG%'] = round(df['FGM']/df['FGA'],3)

# Calculate z scores for the standard 9 fantasy categories to be used to calc fantasy/punt values
def create_z_scores(df):
    # Calculate total fantasy value based on 9-cat traditionally used
    # Formula based on z scores - adjust as needed
    # FUTURE ------------------------------------------------------------ Adjust formula to only consider checked categories
    df['pointZ'] = stats.zscore(df['PPG'])
    df['assistZ'] = stats.zscore(df['APG'])
    df['reboundZ'] = stats.zscore(df['RPG'])
    df['stealZ'] = stats.zscore(df['SPG'])
    df['blockZ'] = stats.zscore(df['BPG'])
    df['turnoverZ'] = (-1)*stats.zscore(df['TOPG'])             # negative stat so multiply by -1
    df['threeZ'] = stats.zscore(df['3PG'])
    # The ft% and fg% categories require a little more math to accurately portray their z scores/impact
    avgFT = np.average(df['FT%'])  
    avgFG = np.average(df['FG%'])  
    df['ftImpact'] = (df['FT%'] - avgFT) * (df['FTA']/df['GP'])
    df['fgImpact'] = (df['FG%'] - avgFG) * df['FGA']                  # FGA is already per game as calc above
    df['ftZ'] = stats.zscore(df['ftImpact'])
    df['fgZ'] = stats.zscore(df['fgImpact'])

# Calculate standard 9 category fantasy value
def create_fantasy_value(df):
    zlist = ['pointZ', 'assistZ','reboundZ', 'stealZ', 'blockZ', 'turnoverZ', 'threeZ', 'ftZ', 'fgZ']
    df['9 Cat Value'] = round(df[zlist].sum(axis=1),2)
    df['Punting Value'] = 0

# def create_punt_value(df):
#     cats = request.POST.getlist('categories')
#     for i in cats:
#         df['Punting Value'] += df[i]
#     df['Punting Value'] = round(df['Punting Value'], 2)
#     df['Punt Difference'] = df['Punting Value'] - df['9 Cat Value']