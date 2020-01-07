from image_loader import ImageLoader
from player_manager import PlayerManager
from start_screen import StartScreen
from game_screen import GameScreen
from location_screen import LocationScreen
from card_screen import CardScreen

modules = [
           
    # General modules
    [ ImageLoader, {  } ],
    [ PlayerManager, { 'maxPlayers': 4 } ],
    
    # Screens
    [ StartScreen, {  } ],
    [ GameScreen, { 'playerCount': 4, 'direction': True } ],
    [ LocationScreen, {  } ],
    [ CardScreen, {  } ]

]
