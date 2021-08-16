from nba_api.stats.static import players

# To get player id example
player_dict = players.get_players()
bron = [player for player in player_dict if player['full_name'] == 'LeBron James'][0]
bron_id = bron['id']

# To get team id example
from nba_api.stats.static import teams
team_dict = teams.get_teams()

print(bron)