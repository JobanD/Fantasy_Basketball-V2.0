import pandas as pd
import numpy as np
import scipy.stats as stats

# Functions used in predictive analysis
# Functions are called in the views file in the main directory

# Clean dataframe
def clean(df):
    df = df.dropna(how="all")   # Drop empty rows
    min_gp = 10                 # MIN games played to be taken into consideration
    df = df[df['GP'] > min_gp]

# Return normalized stats of any given column
def normalize(col):
    return (col - col.min()) / (col.max() - col.min())

# Return normalized columns for the stats listed in norm_stats in a given data frame
# CONSIDERATION: SHOULD % STATS BE NORMALIZED?
def normalize_df(df):
    norm_stats = [
        'MPG',
        'FTA',
        'FTp',
        'FGA2',
        'FG2p',
        'FGA3',
        'FG3p',
        'EFG',
        'PPG',
        'RPG',
        'APG',
        'SPG',
        'BPG',
        'TOPG'
    ]  

    for col in norm_stats:
        df['{}_norm'.format(col)] = normalize(df[col])
    
    return df

# Return euclidean distance between 2 points
# Used to find how similar two players are in given stats
# Use with vfunc function to return numpy aware function
def calc_distance(u,v):
    dist = np.sqrt(np.sum((u - v)**2))      # Calculate euclidean distance
    return dist

# use numpy vectorize to transform euclidean distance to be numpy aware (float input into float output)
# def vfunc(u,v):
#     return np.vectorize(calc_distance(u,v))

# Find player along with their associated stats given player name, player season, and the dataframe
def find_player(name, season, df):
    for row in df.itertuples():
        if season == row.Season_ID and name == row.Name:
            return row

# Return distance vectors for any given player to find most similar within given dataframe       
def compare(player_name, season_id, df):
    
    # Where distance vectors will be stored
    player_dist = []
    
    # Create vector for current players normalized stats
    current_player_vector = np.array([
        (df.loc[(df['Name'] == player_name) & (df['Season_ID'] == season_id), 'MPG_norm']),
        (df.loc[(df['Name'] == player_name) & (df['Season_ID'] == season_id), 'FTA_norm']),
        (df.loc[(df['Name'] == player_name) & (df['Season_ID'] == season_id), 'FTp_norm']),
        (df.loc[(df['Name'] == player_name) & (df['Season_ID'] == season_id), 'FGA2_norm']),
        (df.loc[(df['Name'] == player_name) & (df['Season_ID'] == season_id), 'FG2p_norm']),
        (df.loc[(df['Name'] == player_name) & (df['Season_ID'] == season_id), 'FGA3_norm']),
        (df.loc[(df['Name'] == player_name) & (df['Season_ID'] == season_id), 'FG3p_norm']),
        (df.loc[(df['Name'] == player_name) & (df['Season_ID'] == season_id), 'EFG_norm']),
        (df.loc[(df['Name'] == player_name) & (df['Season_ID'] == season_id), 'PPG_norm']),
        (df.loc[(df['Name'] == player_name) & (df['Season_ID'] == season_id), 'RPG_norm']),
        (df.loc[(df['Name'] == player_name) & (df['Season_ID'] == season_id), 'APG_norm']),
        (df.loc[(df['Name'] == player_name) & (df['Season_ID'] == season_id), 'SPG_norm']),
        (df.loc[(df['Name'] == player_name) & (df['Season_ID'] == season_id), 'BPG_norm']),
        (df.loc[(df['Name'] == player_name) & (df['Season_ID'] == season_id), 'TOPG_norm'])
    ])
    
    # iterate through other players and compare each players vector to our given player
    for row in df.itertuples():
        compared_player_vector = np.array([
            row.MPG_norm,
            row.FTA_norm,
            row.FTp_norm,
            row.FGA2_norm,
            row.FG2p_norm,
            row.FGA3_norm,
            row.FG3p,
            row.EFG_norm,
            row.PPG_norm,
            row.RPG_norm,
            row.APG_norm,
            row.SPG_norm,
            row.BPG_norm,
            row.TOPG_norm
        ])
        
        vfunc = np.vectorize(calc_distance)
        distance_vect = vfunc(current_player_vector, compared_player_vector)
        num = np.sum((distance_vect)) / len(distance_vect)
        percent_error = round((1-num),1)
        player = row.Name
        season = row.Season_ID
        player_compare_info = [str(player),str(season),num,percent_error]
        player_dist.append(player_compare_info)
        
    return player_dist
        
        