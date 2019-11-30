from player_manager import PlayerManager
from start_screen import StartScreen
from game_screen import GameScreen
from location_screen import LocationScreen

modules = [
    [ PlayerManager, { 'maxPlayers': 4 } ],
    [ StartScreen, {  } ],
    [ GameScreen, { 'playerCount': 4, 'direction': True } ],
    [ LocationScreen, {  } ]
]
