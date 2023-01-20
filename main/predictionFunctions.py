from os import error
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
    
    # If player doesn't exist return
    if (((df['Season_ID'] == season_id) & (df['Name'] == player_name)).any() == False):
        return
        
    # Where distance vectors will be stored
    player_dist = []
    
    # Use list if different stats should have different weights
    # IMPORTANT: Keep list as long as list of stats being counted
    weighted_nums = [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    
    # Create vector for current players normalized stats
    current_player_vector = np.array([
        #(df.loc[(df['Name'] == player_name) & (df['Season_ID'] == season_id), 'MPG_norm']),
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
            #row.MPG_norm,
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
        
        # Vectorize euclidean distance so we can work with it, calc Percent Error and store player name/season
        vfunc = np.vectorize(calc_distance)
        distance_vect = vfunc(current_player_vector, compared_player_vector)
        weighted_dist = distance_vect * weighted_nums                               # USE if using weighted stats
        num = np.sum(np.abs(distance_vect)) / len(distance_vect)
        weighted_num = np.sum(np.abs(weighted_dist)) / len(distance_vect)
        percent_error = round((1-num),1)
        
        player = row.Name
        season = row.Season_ID
        player_compare_info = [str(player), str(season), num, percent_error]
        player_dist.append(weighted_num)
        
    df['Distance'] = player_dist
    
    # Rank by shortest distance to find most similar players
    ranked_df = df.sort_values('Distance')
        
    return ranked_df

def project_stats(player_name, season_id, df):
    
    # If player doesn't exist return
    if (((df['Season_ID'] == season_id) & (df['Name'] == player_name)).any() == False):
        return
    
    ranked_df = compare(player_name, season_id, df)
    
    seasons = [
        '2017-18',
        '2018-19',
        '2019-20',
        '2020-21',
        '2021-22'
    ]
    
    stats = [
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
    
    projected_stats = {}
    
    for col in stats:
        sum_stat = 0
        sum_weight = 0
        # Loop through top 10 most similar players
        for index, row in ranked_df.iloc[1:11].iterrows():
            # Skip if season is 2020-21 because then the player has no next season
            if row.Season_ID == '2020-21':
                continue
            # Get next season
            weight = (1/row.Distance)
            next_season = seasons[(seasons.index(row.Season_ID) + 1)]
            # Find players next season, skip if doesn't exist
            next_player = find_player(row.Name, next_season, ranked_df)
            if next_player == None:
                continue
            sum_stat += getattr(next_player, col) * weight
            sum_weight += weight
        projected_stats['Name'] = player_name
        projected_stats['Projected Season'] = seasons[(seasons.index(season_id) +1 )]
        projected_stats['Projected_' + col] = (sum_stat / sum_weight)
    
    df_projected_stats = pd.DataFrame([projected_stats])
    return df_projected_stats
            
        
        