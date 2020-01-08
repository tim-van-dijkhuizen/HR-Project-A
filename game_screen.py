import ui
import player_manager
from screen import Screen
from button import Button
from selectable_button import SelectableButton
from location_button  import LocationButton
from player_button import PlayerButton
from location import Location
from game_manager import GameManager
from turn_manager import TurnManager
from bot_manager import BotManager

class GameScreen(Screen):

    # Button offset
    buttonOffset = 165
    buttonOffset2 = 25
    
    boardWidth = 794
    boardHeight = 500
    
    fromScreen = None
    player = None

    def getHandle(self):
        return 'game'
    
    def setup(self):
        self.boardX = width - (self.boardWidth + ui.SPACING_SM)
        self.boardY = height / 2 - self.boardHeight / 2

    def draw(self):
        imageLoader = self.app.getModule('imageLoader')
        playerManager = self.app.getModule('playerManager')

        # Set styling
        fill(ui.COLOR_TEXT)
        textSize(ui.TEXT_SIZE_XL)
        textAlign(LEFT)
        
        # Players title
        text('Spelers', ui.SPACING_SM, ui.SPACING_MD + ui.SPACING_SM + 50 + ui.SPACING_MD)

        # Board image
        boardImage = imageLoader.get('board-players' + str(playerManager.maxPlayers))
        image(boardImage, self.boardX, self.boardY, self.boardWidth, self.boardHeight)

    def afterShow(self):
        playerManager = self.app.getModule('playerManager')
        buttons = [ i for i in self.app.getModulesByType(PlayerButton) if i.getTopLevelParent() is self ]
        
        # Select the correct bot button
        for button in buttons:
            if button.player is playerManager.botPlayer:
                botButtons = button.getSubModulesByType(SelectableButton)
                botButton = botButtons[0] if len(botButtons) > 0 else None
                
                if botButton != None:
                    botButton.select()

    def getSubModules(self):
        playerManager = self.app.getModule('playerManager')
        
        modules = [            
            [ GameManager, {  } ],
            [ TurnManager, {  } ],
            [ BotManager, {  } ],
        
            [ LocationButton, { 'x': 735 + self.buttonOffset2, 'y': 275 , 'maxPlayers': 4, 'location': Location(1, 1), 'readOnly': True } ],
            [ LocationButton, { 'x': 705 + self.buttonOffset2, 'y': 250 , 'maxPlayers': 4, 'location': Location(1, 2), 'readOnly': True } ],
            [ LocationButton, { 'x': 678 + self.buttonOffset2, 'y': 236 , 'maxPlayers': 4, 'location': Location(1, 3), 'readOnly': True } ],
            [ LocationButton, { 'x': 657 + self.buttonOffset2, 'y': 210 , 'maxPlayers': 4, 'location': Location(1, 4), 'readOnly': True } ],
            [ LocationButton, { 'x': 635 + self.buttonOffset2, 'y': 189 , 'maxPlayers': 4, 'location': Location(1, 5), 'readOnly': True } ],
            [ LocationButton, { 'x': 615 + self.buttonOffset2, 'y': 166 , 'maxPlayers': 4, 'location': Location(1, 6), 'readOnly': True } ],
            [ LocationButton, { 'x': 615 + self.buttonOffset2, 'y': 134 , 'maxPlayers': 4, 'location': Location(1, 7), 'readOnly': True } ],
            [ LocationButton, { 'x': 628 + self.buttonOffset2, 'y': 105 , 'maxPlayers': 4, 'location': Location(1, 8), 'readOnly': True } ],
            [ LocationButton, { 'x': 658 + self.buttonOffset2, 'y': 93 , 'maxPlayers': 4, 'location': Location(1, 9), 'readOnly': True } ],
            [ LocationButton, { 'x': 688 + self.buttonOffset2, 'y': 82 , 'maxPlayers': 4, 'location': Location(1, 10), 'readOnly': True } ],
            [ LocationButton, { 'x': 715 + self.buttonOffset2, 'y': 93 , 'maxPlayers': 4, 'location': Location(1, 11), 'readOnly': True } ],
            [ LocationButton, { 'x': 735 + self.buttonOffset2, 'y': 120 , 'maxPlayers': 4, 'location': Location(1, 12), 'readOnly': True } ],
            [ LocationButton, { 'x': 750 + self.buttonOffset2, 'y': 93 , 'maxPlayers': 4, 'location': Location(1, 13), 'readOnly': True } ],
            [ LocationButton, { 'x': 780 + self.buttonOffset2, 'y': 82 , 'maxPlayers': 4, 'location': Location(1, 14), 'readOnly': True } ],
            [ LocationButton, { 'x': 810 + self.buttonOffset2, 'y': 93 , 'maxPlayers': 4, 'location': Location(1, 15), 'readOnly': True } ],
            [ LocationButton, { 'x': 838 + self.buttonOffset2, 'y': 108 , 'maxPlayers': 4, 'location': Location(1, 16), 'readOnly': True } ],
            [ LocationButton, { 'x': 852 + self.buttonOffset2, 'y': 137 , 'maxPlayers': 4, 'location': Location(1, 17), 'readOnly': True } ],
            [ LocationButton, { 'x': 852 + self.buttonOffset2, 'y': 166 , 'maxPlayers': 4, 'location': Location(1, 18), 'readOnly': True } ],
            [ LocationButton, { 'x': 830 + self.buttonOffset2, 'y': 189 , 'maxPlayers': 4, 'location': Location(1, 19), 'readOnly': True } ],
            [ LocationButton, { 'x': 810 + self.buttonOffset2, 'y': 212 , 'maxPlayers': 4, 'location': Location(1, 20), 'readOnly': True } ],
            [ LocationButton, { 'x': 791 + self.buttonOffset2, 'y': 236 , 'maxPlayers': 4, 'location': Location(1, 21), 'readOnly': True } ],
            [ LocationButton, { 'x': 765 + self.buttonOffset2, 'y': 250 , 'maxPlayers': 4, 'location': Location(1, 22), 'readOnly': True } ],
            
            [ LocationButton, { 'x': 779 + self.buttonOffset2, 'y': 312 , 'maxPlayers': 4, 'location': Location(2, 1), 'readOnly': True } ],
            [ LocationButton, { 'x': 803 + self.buttonOffset2, 'y': 282 , 'maxPlayers': 4, 'location': Location(2, 2), 'readOnly': True } ],
            [ LocationButton, { 'x': 818 + self.buttonOffset2, 'y': 255 , 'maxPlayers': 4, 'location': Location(2, 3), 'readOnly': True } ], 
            [ LocationButton, { 'x': 840 + self.buttonOffset2, 'y': 235 , 'maxPlayers': 4, 'location': Location(2, 4), 'readOnly': True } ],
            [ LocationButton, { 'x': 863 + self.buttonOffset2, 'y': 213 , 'maxPlayers': 4, 'location': Location(2, 5), 'readOnly': True } ], 
            [ LocationButton, { 'x': 888 + self.buttonOffset2, 'y': 192 , 'maxPlayers': 4, 'location': Location(2, 6), 'readOnly': True } ],
            [ LocationButton, { 'x': 918 + self.buttonOffset2, 'y': 192 , 'maxPlayers': 4, 'location': Location(2, 7), 'readOnly': True } ],
            [ LocationButton, { 'x': 948 + self.buttonOffset2, 'y': 204 , 'maxPlayers': 4, 'location': Location(2, 8), 'readOnly': True } ],
            [ LocationButton, { 'x': 960 + self.buttonOffset2, 'y': 235 , 'maxPlayers': 4, 'location': Location(2, 9), 'readOnly': True } ],
            [ LocationButton, { 'x': 970 + self.buttonOffset2, 'y': 265 , 'maxPlayers': 4, 'location': Location(2, 10), 'readOnly': True } ],
            [ LocationButton, { 'x': 957 + self.buttonOffset2, 'y': 295 , 'maxPlayers': 4, 'location': Location(2, 11), 'readOnly': True } ],
            [ LocationButton, { 'x': 930 + self.buttonOffset2, 'y': 310 , 'maxPlayers': 4, 'location': Location(2, 12), 'readOnly': True } ],
            [ LocationButton, { 'x': 957 + self.buttonOffset2, 'y': 328 , 'maxPlayers': 4, 'location': Location(2, 13), 'readOnly': True } ],
            [ LocationButton, { 'x': 970 + self.buttonOffset2, 'y': 357 , 'maxPlayers': 4, 'location': Location(2, 14), 'readOnly': True } ],
            [ LocationButton, { 'x': 960 + self.buttonOffset2, 'y': 387 , 'maxPlayers': 4, 'location': Location(2, 15), 'readOnly': True } ],
            [ LocationButton, { 'x': 945 + self.buttonOffset2, 'y': 415 , 'maxPlayers': 4, 'location': Location(2, 16), 'readOnly': True } ],
            [ LocationButton, { 'x': 915 + self.buttonOffset2, 'y': 432 , 'maxPlayers': 4, 'location': Location(2, 17), 'readOnly': True } ],
            [ LocationButton, { 'x': 885 + self.buttonOffset2, 'y': 432 , 'maxPlayers': 4, 'location': Location(2, 18), 'readOnly': True } ],
            [ LocationButton, { 'x': 863 + self.buttonOffset2, 'y': 410 , 'maxPlayers': 4, 'location': Location(2, 19), 'readOnly': True } ],
            [ LocationButton, { 'x': 840 + self.buttonOffset2, 'y': 389 , 'maxPlayers': 4, 'location': Location(2, 20), 'readOnly': True } ],
            [ LocationButton, { 'x': 818 + self.buttonOffset2, 'y': 368 , 'maxPlayers': 4, 'location': Location(2, 21), 'readOnly': True } ],
            [ LocationButton, { 'x': 802 + self.buttonOffset2, 'y': 342 , 'maxPlayers': 4, 'location': Location(2, 22), 'readOnly': True } ],
            
            [ LocationButton, { 'x': 735 + self.buttonOffset2, 'y': 353 , 'maxPlayers': 4, 'location': Location(3, 1), 'readOnly': True } ],
            [ LocationButton, { 'x': 765 + self.buttonOffset2, 'y': 378 , 'maxPlayers': 4, 'location': Location(3, 2), 'readOnly': True } ],
            [ LocationButton, { 'x': 791 + self.buttonOffset2, 'y': 393 , 'maxPlayers': 4, 'location': Location(3, 3), 'readOnly': True } ],
            [ LocationButton, { 'x': 812 + self.buttonOffset2, 'y': 415 , 'maxPlayers': 4, 'location': Location(3, 4), 'readOnly': True } ],
            [ LocationButton, { 'x': 832 + self.buttonOffset2, 'y': 438 , 'maxPlayers': 4, 'location': Location(3, 5), 'readOnly': True } ],
            [ LocationButton, { 'x': 852 + self.buttonOffset2, 'y': 466 , 'maxPlayers': 4, 'location': Location(3, 6), 'readOnly': True } ],
            [ LocationButton, { 'x': 852 + self.buttonOffset2, 'y': 496 , 'maxPlayers': 4, 'location': Location(3, 7), 'readOnly': True } ],
            [ LocationButton, { 'x': 840 + self.buttonOffset2, 'y': 524 , 'maxPlayers': 4, 'location': Location(3, 8), 'readOnly': True } ],
            [ LocationButton, { 'x': 810 + self.buttonOffset2, 'y': 538 , 'maxPlayers': 4, 'location': Location(3, 9), 'readOnly': True } ],
            [ LocationButton, { 'x': 780 + self.buttonOffset2, 'y': 548 , 'maxPlayers': 4, 'location': Location(3, 10), 'readOnly': True } ],
            [ LocationButton, { 'x': 753 + self.buttonOffset2, 'y': 536 , 'maxPlayers': 4, 'location': Location(3, 11), 'readOnly': True } ],
            [ LocationButton, { 'x': 735 + self.buttonOffset2, 'y': 510 , 'maxPlayers': 4, 'location': Location(3, 12), 'readOnly': True } ],
            [ LocationButton, { 'x': 719 + self.buttonOffset2, 'y': 536 , 'maxPlayers': 4, 'location': Location(3, 13), 'readOnly': True } ],
            [ LocationButton, { 'x': 688 + self.buttonOffset2, 'y': 548 , 'maxPlayers': 4, 'location': Location(3, 14), 'readOnly': True } ],
            [ LocationButton, { 'x': 660 + self.buttonOffset2, 'y': 534 , 'maxPlayers': 4, 'location': Location(3, 15), 'readOnly': True } ],
            [ LocationButton, { 'x': 630 + self.buttonOffset2, 'y': 521 , 'maxPlayers': 4, 'location': Location(3, 16), 'readOnly': True } ],
            [ LocationButton, { 'x': 616 + self.buttonOffset2, 'y': 494 , 'maxPlayers': 4, 'location': Location(3, 17), 'readOnly': True } ],
            [ LocationButton, { 'x': 616 + self.buttonOffset2, 'y': 462 , 'maxPlayers': 4, 'location': Location(3, 18), 'readOnly': True } ],
            [ LocationButton, { 'x': 638 + self.buttonOffset2, 'y': 440 , 'maxPlayers': 4, 'location': Location(3, 19), 'readOnly': True } ],
            [ LocationButton, { 'x': 657 + self.buttonOffset2, 'y': 415 , 'maxPlayers': 4, 'location': Location(3, 20), 'readOnly': True } ],
            [ LocationButton, { 'x': 678 + self.buttonOffset2, 'y': 393 , 'maxPlayers': 4, 'location': Location(3, 21), 'readOnly': True } ],
            [ LocationButton, { 'x': 705 + self.buttonOffset2, 'y': 378 , 'maxPlayers': 4, 'location': Location(3, 22), 'readOnly': True } ],
            
            [ LocationButton, { 'x': 692 + self.buttonOffset2, 'y': 312 , 'maxPlayers': 4, 'location': Location(4, 1), 'readOnly': True } ],
            [ LocationButton, { 'x': 669 + self.buttonOffset2, 'y': 342 , 'maxPlayers': 4, 'location': Location(4, 2), 'readOnly': True } ],
            [ LocationButton, { 'x': 655 + self.buttonOffset2, 'y': 368 , 'maxPlayers': 4, 'location': Location(4, 3), 'readOnly': True } ],
            [ LocationButton, { 'x': 630 + self.buttonOffset2, 'y': 389 , 'maxPlayers': 4, 'location': Location(4, 4), 'readOnly': True } ],
            [ LocationButton, { 'x': 606 + self.buttonOffset2, 'y': 410 , 'maxPlayers': 4, 'location': Location(4, 5), 'readOnly': True } ],
            [ LocationButton, { 'x': 583 + self.buttonOffset2, 'y': 432 , 'maxPlayers': 4, 'location': Location(4, 6), 'readOnly': True } ],
            [ LocationButton, { 'x': 553 + self.buttonOffset2, 'y': 432 , 'maxPlayers': 4, 'location': Location(4, 7), 'readOnly': True } ],
            [ LocationButton, { 'x': 525 + self.buttonOffset2, 'y': 420 , 'maxPlayers': 4, 'location': Location(4, 8), 'readOnly': True } ],
            [ LocationButton, { 'x': 510 + self.buttonOffset2, 'y': 390 , 'maxPlayers': 4, 'location': Location(4, 9), 'readOnly': True } ],
            [ LocationButton, { 'x': 497 + self.buttonOffset2, 'y': 360 , 'maxPlayers': 4, 'location': Location(4, 10), 'readOnly': True } ],
            [ LocationButton, { 'x': 512 + self.buttonOffset2, 'y': 330 , 'maxPlayers': 4, 'location': Location(4, 11), 'readOnly': True } ],
            [ LocationButton, { 'x': 542 + self.buttonOffset2, 'y': 314 , 'maxPlayers': 4, 'location': Location(4, 12), 'readOnly': True } ],
            [ LocationButton, { 'x': 512 + self.buttonOffset2, 'y': 298 , 'maxPlayers': 4, 'location': Location(4, 13), 'readOnly': True } ],
            [ LocationButton, { 'x': 500 + self.buttonOffset2, 'y': 267 , 'maxPlayers': 4, 'location': Location(4, 14), 'readOnly': True } ],
            [ LocationButton, { 'x': 512 + self.buttonOffset2, 'y': 238 , 'maxPlayers': 4, 'location': Location(4, 15), 'readOnly': True } ],
            [ LocationButton, { 'x': 525 + self.buttonOffset2, 'y': 208 , 'maxPlayers': 4, 'location': Location(4, 16), 'readOnly': True } ],
            [ LocationButton, { 'x': 553 + self.buttonOffset2, 'y': 195 , 'maxPlayers': 4, 'location': Location(4, 17), 'readOnly': True } ],
            [ LocationButton, { 'x': 583 + self.buttonOffset2, 'y': 195 , 'maxPlayers': 4, 'location': Location(4, 18), 'readOnly': True } ],
            [ LocationButton, { 'x': 606 + self.buttonOffset2, 'y': 215 , 'maxPlayers': 4, 'location': Location(4, 19), 'readOnly': True } ],
            [ LocationButton, { 'x': 630 + self.buttonOffset2, 'y': 235 , 'maxPlayers': 4, 'location': Location(4, 20), 'readOnly': True } ],
            [ LocationButton, { 'x': 655 + self.buttonOffset2, 'y': 256 , 'maxPlayers': 4, 'location': Location(4, 21), 'readOnly': True } ],
            [ LocationButton, { 'x': 669 + self.buttonOffset2, 'y': 282, 'maxPlayers': 4, 'location': Location(4, 22), 'readOnly': True } ],
            
            [ LocationButton, { 'x': 735 - 125, 'y': 295 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(1, 1), 'readOnly': True } ],
            [ LocationButton, { 'x': 705 - 125, 'y': 270 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(1, 2), 'readOnly': True } ],
            [ LocationButton, { 'x': 678 - 125, 'y': 256 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(1, 3), 'readOnly': True } ],
            [ LocationButton, { 'x': 655 - 125, 'y': 235 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(1, 4), 'readOnly': True } ],
            [ LocationButton, { 'x': 635 - 125, 'y': 209 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(1, 5), 'readOnly': True } ],
            [ LocationButton, { 'x': 615 - 125, 'y': 183 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(1, 6), 'readOnly': True } ],
            [ LocationButton, { 'x': 615 - 125, 'y': 151 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(1, 7), 'readOnly': True } ],
            [ LocationButton, { 'x': 628 - 125, 'y': 125 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(1, 8), 'readOnly': True } ],
            [ LocationButton, { 'x': 658 - 125, 'y': 110 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(1, 9), 'readOnly': True } ],
            [ LocationButton, { 'x': 688 - 125, 'y': 99 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(1, 10), 'readOnly': True } ],
            [ LocationButton, { 'x': 716 - 125, 'y': 110 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(1, 11), 'readOnly': True } ],
            [ LocationButton, { 'x': 735 - 125, 'y': 140 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(1, 12), 'readOnly': True } ],
            [ LocationButton, { 'x': 750 - 125, 'y': 110 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(1, 13), 'readOnly': True } ],
            [ LocationButton, { 'x': 780 - 125, 'y': 99 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(1, 14), 'readOnly': True } ],
            [ LocationButton, { 'x': 812 - 125, 'y': 110 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(1, 15), 'readOnly': True } ],
            [ LocationButton, { 'x': 840 - 125, 'y': 126 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(1, 16), 'readOnly': True } ],
            [ LocationButton, { 'x': 854 - 125, 'y': 157 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(1, 17), 'readOnly': True } ],
            [ LocationButton, { 'x': 854 - 125, 'y': 186 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(1, 18), 'readOnly': True } ],
            [ LocationButton, { 'x': 833 - 125, 'y': 203 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(1, 19), 'readOnly': True } ],
            [ LocationButton, { 'x': 812 - 125, 'y': 230 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(1, 20), 'readOnly': True } ],
            [ LocationButton, { 'x': 791 - 125, 'y': 256 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(1, 21), 'readOnly': True } ],
            [ LocationButton, { 'x': 765 - 125, 'y': 270 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(1, 22), 'readOnly': True } ],
            
            [ LocationButton, { 'x': 735 + 164, 'y': 295 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(2, 1), 'readOnly': True } ],
            [ LocationButton, { 'x': 705 + 164, 'y': 279 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(2, 2), 'readOnly': True } ],
            [ LocationButton, { 'x': 676 + 164, 'y': 252 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(2, 3), 'readOnly': True } ],
            [ LocationButton, { 'x': 655 + 164, 'y': 230 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(2, 4), 'readOnly': True } ],
            [ LocationButton, { 'x': 632 + 164, 'y': 209 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(2, 5), 'readOnly': True } ],
            [ LocationButton, { 'x': 612 + 164, 'y': 180 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(2, 6), 'readOnly': True } ],
            [ LocationButton, { 'x': 612 + 164, 'y': 152 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(2, 7), 'readOnly': True } ],
            [ LocationButton, { 'x': 625 + 164, 'y': 119 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(2, 8), 'readOnly': True } ],
            [ LocationButton, { 'x': 655 + 164, 'y': 111 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(2, 9), 'readOnly': True } ],
            [ LocationButton, { 'x': 688 + 164, 'y': 99 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(2, 10), 'readOnly': True } ],
            [ LocationButton, { 'x': 715 + 164, 'y': 111 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(2, 11), 'readOnly': True } ],
            [ LocationButton, { 'x': 733 + 164, 'y': 138 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(2, 12), 'readOnly': True } ],
            [ LocationButton, { 'x': 750 + 164, 'y': 111 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(2, 13), 'readOnly': True } ],
            [ LocationButton, { 'x': 780 + 164, 'y': 99 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(2, 14), 'readOnly': True } ],
            [ LocationButton, { 'x': 810 + 164, 'y': 116 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(2, 15), 'readOnly': True } ],
            [ LocationButton, { 'x': 838 + 164, 'y': 136 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(2, 16), 'readOnly': True } ],
            [ LocationButton, { 'x': 852 + 164, 'y': 157 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(2, 17), 'readOnly': True } ],
            [ LocationButton, { 'x': 852 + 164, 'y': 186 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(2, 18), 'readOnly': True } ],
            [ LocationButton, { 'x': 830 + 164, 'y': 209 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(2, 19), 'readOnly': True } ],
            [ LocationButton, { 'x': 810 + 164, 'y': 232 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(2, 20), 'readOnly': True } ],
            [ LocationButton, { 'x': 791 + 164, 'y': 256 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(2, 21), 'readOnly': True } ],
            [ LocationButton, { 'x': 765 + 164, 'y': 270 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(2, 22), 'readOnly': True } ], 
            
            [ LocationButton, { 'x': 781 + self.buttonOffset, 'y': 312, 'maxPlayers': 6, 'location': Location(3, 1), 'readOnly': True } ],
            [ LocationButton, { 'x': 802 + self.buttonOffset, 'y': 282, 'maxPlayers': 6, 'location': Location(3, 2), 'readOnly': True } ],
            [ LocationButton, { 'x': 818 + self.buttonOffset, 'y': 255, 'maxPlayers': 6, 'location': Location(3, 3), 'readOnly': True } ], 
            [ LocationButton, { 'x': 842 + self.buttonOffset, 'y': 235, 'maxPlayers': 6, 'location': Location(3, 4), 'readOnly': True } ],
            [ LocationButton, { 'x': 865 + self.buttonOffset, 'y': 215, 'maxPlayers': 6, 'location': Location(3, 5), 'readOnly': True } ], 
            [ LocationButton, { 'x': 890 + self.buttonOffset, 'y': 192, 'maxPlayers': 6, 'location': Location(3, 6), 'readOnly': True } ],
            [ LocationButton, { 'x': 920 + self.buttonOffset, 'y': 192, 'maxPlayers': 6, 'location': Location(3, 7), 'readOnly': True } ],
            [ LocationButton, { 'x': 950 + self.buttonOffset, 'y': 204, 'maxPlayers': 6, 'location': Location(3, 8), 'readOnly': True } ],
            [ LocationButton, { 'x': 962 + self.buttonOffset, 'y': 235, 'maxPlayers': 6, 'location': Location(3, 9), 'readOnly': True } ],
            [ LocationButton, { 'x': 975 + self.buttonOffset, 'y': 265, 'maxPlayers': 6, 'location': Location(3, 10), 'readOnly': True } ],
            [ LocationButton, { 'x': 959 + self.buttonOffset, 'y': 295, 'maxPlayers': 6, 'location': Location(3, 11), 'readOnly': True } ],
            [ LocationButton, { 'x': 932 + self.buttonOffset, 'y': 312, 'maxPlayers': 6, 'location': Location(3, 12), 'readOnly': True } ],
            [ LocationButton, { 'x': 959 + self.buttonOffset, 'y': 327, 'maxPlayers': 6, 'location': Location(3, 13), 'readOnly': True } ],
            [ LocationButton, { 'x': 972 + self.buttonOffset, 'y': 357, 'maxPlayers': 6, 'location': Location(3, 14), 'readOnly': True } ],
            [ LocationButton, { 'x': 962 + self.buttonOffset, 'y': 387, 'maxPlayers': 6, 'location': Location(3, 15), 'readOnly': True } ],
            [ LocationButton, { 'x': 947 + self.buttonOffset, 'y': 415, 'maxPlayers': 6, 'location': Location(3, 16), 'readOnly': True } ],
            [ LocationButton, { 'x': 917 + self.buttonOffset, 'y': 432, 'maxPlayers': 6, 'location': Location(3, 17), 'readOnly': True } ],
            [ LocationButton, { 'x': 887 + self.buttonOffset, 'y': 432, 'maxPlayers': 6, 'location': Location(3, 18), 'readOnly': True } ],
            [ LocationButton, { 'x': 865 + self.buttonOffset, 'y': 410, 'maxPlayers': 6, 'location': Location(3, 19), 'readOnly': True } ],
            [ LocationButton, { 'x': 842 + self.buttonOffset, 'y': 389, 'maxPlayers': 6, 'location': Location(3, 20), 'readOnly': True } ],
            [ LocationButton, { 'x': 818 + self.buttonOffset, 'y': 368, 'maxPlayers': 6, 'location': Location(3, 21), 'readOnly': True } ],
            [ LocationButton, { 'x': 802 + self.buttonOffset, 'y': 342, 'maxPlayers': 6, 'location': Location(3, 22), 'readOnly': True } ],
            
            [ LocationButton, { 'x': 736 + 169, 'y': 375 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(4, 1), 'readOnly': True } ],
            [ LocationButton, { 'x': 706 + 169, 'y': 402 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(4, 2), 'readOnly': True } ],
            [ LocationButton, { 'x': 681 + 169, 'y': 417 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(4, 3), 'readOnly': True } ],
            [ LocationButton, { 'x': 657 + 169, 'y': 440 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(4, 4), 'readOnly': True } ],
            [ LocationButton, { 'x': 637 + 169, 'y': 465 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(4, 5), 'readOnly': True } ],
            [ LocationButton, { 'x': 617 + 169, 'y': 486 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(4, 6), 'readOnly': True } ],
            [ LocationButton, { 'x': 617 + 169, 'y': 514 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(4, 7), 'readOnly': True } ],
            [ LocationButton, { 'x': 633 + 169, 'y': 543 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(4, 8), 'readOnly': True } ],
            [ LocationButton, { 'x': 658 + 169, 'y': 560 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(4, 9), 'readOnly': True } ],
            [ LocationButton, { 'x': 688 + 169, 'y': 570 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(4, 10), 'readOnly': True } ],
            [ LocationButton, { 'x': 717 + 169, 'y': 555 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(4, 11), 'readOnly': True } ],
            [ LocationButton, { 'x': 736 + 169, 'y': 530 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(4, 12), 'readOnly': True } ],
            [ LocationButton, { 'x': 754 + 169, 'y': 555 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(4, 13), 'readOnly': True } ],
            [ LocationButton, { 'x': 780 + 169, 'y': 570 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(4, 14), 'readOnly': True } ],
            [ LocationButton, { 'x': 811 + 169, 'y': 560 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(4, 15), 'readOnly': True } ],
            [ LocationButton, { 'x': 840 + 169, 'y': 545 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(4, 16), 'readOnly': True } ],
            [ LocationButton, { 'x': 854 + 169, 'y': 514 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(4, 17), 'readOnly': True } ],
            [ LocationButton, { 'x': 854 + 169, 'y': 486 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(4, 18), 'readOnly': True } ],
            [ LocationButton, { 'x': 832 + 169, 'y': 465 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(4, 19), 'readOnly': True } ],
            [ LocationButton, { 'x': 812 + 169, 'y': 440 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(4, 20), 'readOnly': True } ],
            [ LocationButton, { 'x': 791 + 169, 'y': 417 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(4, 21), 'readOnly': True } ],
            [ LocationButton, { 'x': 765 + 169, 'y': 402 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(4, 22), 'readOnly': True } ],
            
            [ LocationButton, { 'x': 735 - 118, 'y': 377 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(5, 1), 'readOnly': True } ],
            [ LocationButton, { 'x': 705 - 118, 'y': 398- self.buttonOffset2, 'maxPlayers': 6, 'location': Location(5, 2), 'readOnly': True } ],
            [ LocationButton, { 'x': 678 - 118, 'y': 415 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(5, 3), 'readOnly': True } ],
            [ LocationButton, { 'x': 656 - 118, 'y': 440 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(5, 4), 'readOnly': True } ],
            [ LocationButton, { 'x': 637 - 118, 'y': 460 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(5, 5), 'readOnly': True } ],
            [ LocationButton, { 'x': 617 - 118, 'y': 486 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(5, 6), 'readOnly': True } ],
            [ LocationButton, { 'x': 617 - 118, 'y': 514 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(5, 7), 'readOnly': True } ],
            [ LocationButton, { 'x': 628 - 118, 'y': 545 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(5, 8), 'readOnly': True } ],
            [ LocationButton, { 'x': 658 - 118, 'y': 560 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(5, 9), 'readOnly': True } ],
            [ LocationButton, { 'x': 688 - 118, 'y': 570 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(5, 10), 'readOnly': True } ],
            [ LocationButton, { 'x': 720 - 118, 'y': 555 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(5, 11), 'readOnly': True } ],
            [ LocationButton, { 'x': 740 - 118, 'y': 530 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(5, 12), 'readOnly': True } ],
            [ LocationButton, { 'x': 755 - 118, 'y': 555 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(5, 13), 'readOnly': True } ],
            [ LocationButton, { 'x': 785 - 118, 'y': 570 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(5, 14), 'readOnly': True } ],
            [ LocationButton, { 'x': 814 - 118, 'y': 560 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(5, 15), 'readOnly': True } ],
            [ LocationButton, { 'x': 849 - 118, 'y': 548 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(5, 16), 'readOnly': True } ],
            [ LocationButton, { 'x': 859 - 118, 'y': 514 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(5, 17), 'readOnly': True } ],
            [ LocationButton, { 'x': 859 - 118, 'y': 486 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(5, 18), 'readOnly': True } ],
            [ LocationButton, { 'x': 837 - 118, 'y': 458 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(5, 19), 'readOnly': True } ],
            [ LocationButton, { 'x': 821 - 118, 'y': 440 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(5, 20), 'readOnly': True } ],
            [ LocationButton, { 'x': 795 - 118, 'y': 415 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(5, 21), 'readOnly': True } ],
            [ LocationButton, { 'x': 765 - 118, 'y': 398 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(5, 22), 'readOnly': True } ],
            
            [ LocationButton, { 'x': 737 - self.buttonOffset, 'y': 317 , 'maxPlayers': 6, 'location': Location(6, 1), 'readOnly': True } ],
            [ LocationButton, { 'x': 713 - self.buttonOffset, 'y': 347 , 'maxPlayers': 6, 'location': Location(6, 2), 'readOnly': True } ],
            [ LocationButton, { 'x': 697 - self.buttonOffset, 'y': 375 , 'maxPlayers': 6, 'location': Location(6, 3), 'readOnly': True } ],
            [ LocationButton, { 'x': 675 - self.buttonOffset, 'y': 396 , 'maxPlayers': 6, 'location': Location(6, 4), 'readOnly': True } ],
            [ LocationButton, { 'x': 651 - self.buttonOffset, 'y': 416 , 'maxPlayers': 6, 'location': Location(6, 5), 'readOnly': True } ],
            [ LocationButton, { 'x': 627 - self.buttonOffset, 'y': 437 , 'maxPlayers': 6, 'location': Location(6, 6), 'readOnly': True } ],
            [ LocationButton, { 'x': 598 - self.buttonOffset, 'y': 437 , 'maxPlayers': 6, 'location': Location(6, 7), 'readOnly': True } ],
            [ LocationButton, { 'x': 570 - self.buttonOffset, 'y': 423 , 'maxPlayers': 6, 'location': Location(6, 8), 'readOnly': True } ],
            [ LocationButton, { 'x': 555 - self.buttonOffset, 'y': 393 , 'maxPlayers': 6, 'location': Location(6, 9), 'readOnly': True } ],
            [ LocationButton, { 'x': 545 - self.buttonOffset, 'y': 363 , 'maxPlayers': 6, 'location': Location(6, 10), 'readOnly': True } ],
            [ LocationButton, { 'x': 562 - self.buttonOffset, 'y': 333 , 'maxPlayers': 6, 'location': Location(6, 11), 'readOnly': True } ],
            [ LocationButton, { 'x': 586 - self.buttonOffset, 'y': 318 , 'maxPlayers': 6, 'location': Location(6, 12), 'readOnly': True } ],
            [ LocationButton, { 'x': 562 - self.buttonOffset, 'y': 300 , 'maxPlayers': 6, 'location': Location(6, 13), 'readOnly': True } ],
            [ LocationButton, { 'x': 545 - self.buttonOffset, 'y': 270 , 'maxPlayers': 6, 'location': Location(6, 14), 'readOnly': True } ],
            [ LocationButton, { 'x': 547 - self.buttonOffset, 'y': 240 , 'maxPlayers': 6, 'location': Location(6, 15), 'readOnly': True } ],
            [ LocationButton, { 'x': 570 - self.buttonOffset, 'y': 208 , 'maxPlayers': 6, 'location': Location(6, 16), 'readOnly': True } ],
            [ LocationButton, { 'x': 597 - self.buttonOffset, 'y': 196 , 'maxPlayers': 6, 'location': Location(6, 17), 'readOnly': True } ],
            [ LocationButton, { 'x': 627 - self.buttonOffset, 'y': 196 , 'maxPlayers': 6, 'location': Location(6, 18), 'readOnly': True } ],
            [ LocationButton, { 'x': 651 - self.buttonOffset, 'y': 217 , 'maxPlayers': 6, 'location': Location(6, 19), 'readOnly': True } ],
            [ LocationButton, { 'x': 675 - self.buttonOffset, 'y': 237 , 'maxPlayers': 6, 'location': Location(6, 20), 'readOnly': True } ],
            [ LocationButton, { 'x': 700 - self.buttonOffset, 'y': 258 , 'maxPlayers': 6, 'location': Location(6, 21), 'readOnly': True } ],
            [ LocationButton, { 'x': 715 - self.buttonOffset, 'y': 287 , 'maxPlayers': 6, 'location': Location(6, 22), 'readOnly': True } ],
        ]
        
        playerButtonX = ui.SPACING_SM
        playerButtonY = ui.SPACING_MD + ui.SPACING_SM + 50 + ui.SPACING_MD + ui.SPACING_SM
        
        # Create PlayerButton modules
        players = playerManager.getAllPlayers()
        for i in range(1, len(players) + 1):
            modules.append([ PlayerButton, {
                'x': playerButtonX,
                'y': playerButtonY,
                'player': players[i - 1],
                'reverseAlignment': i % 2 != 0,
                'readOnly': True
            } ])
            
            playerButtonX += 160 + ui.SPACING_XS
            
            if i % 2 == 0:
                playerButtonX = ui.SPACING_SM
                playerButtonY += 80 + ui.SPACING_XS
            
        return modules
