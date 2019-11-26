from config_manager import ConfigManager
from player_manager import PlayerManager
from start_screen import StartScreen
from game_screen import GameScreen

modules = [
    [ PlayerManager, { 'maxPlayers': 4 } ],
    [ StartScreen, {  } ],
    [ GameScreen, { 'playerCount': 4, 'direction': True } ]
]
