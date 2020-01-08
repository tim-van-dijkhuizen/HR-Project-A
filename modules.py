from image_loader import ImageLoader
from player_manager import PlayerManager
from start_screen import StartScreen
from game_screen import GameScreen
from location_screen import LocationScreen
from card_screen import CardScreen
from win_screen import WinScreen

modules = [
           
    # General modules
    [ ImageLoader, {  } ],
    [ PlayerManager, {  } ],
    
    # Screens
    [ StartScreen, {  } ],
    [ GameScreen, {  } ],
    [ LocationScreen, {  } ],
    [ CardScreen, {  } ],
    [ WinScreen, {  } ]

]
