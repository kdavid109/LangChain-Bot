import numpy as np
import pandas as pd
import nba_api
from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.endpoints import commonplayerinfo
import requests

def getPlayerID(playersName):
    playerList = players.get_active_players()
    print(playerList)
    for player in playerList:
        if player['full_name'] == playersName:
            return player['id']
    print("No player Found!")
    return
        
def get_player_gamelog(playersName, season):
    player_id = getPlayerID(playersName= playersName)
    if not player_id:
        print(f"No player found with the name {playersName}")
        return None
    player_info = commonplayerinfo.CommonPlayerInfo(player_id= player_id)
    game_log = player_info.PlayerGameLog(player_id=player_id, season=season)
def playersTeam(fullName):
    #fix it
    user_input = input(f"What team does {fullName} play for: ")
    return user_input
s = get_player_gamelog("LeBron James", 5)
print(s)
listOfLastNameJames = pd.DataFrame(players.find_players_by_full_name('james'))