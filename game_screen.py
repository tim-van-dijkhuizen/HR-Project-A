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
    buttonOffset = 145
    buttonOffset2 = 35
    
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
        
            [ LocationButton, { 'x': 735, 'y': 275 - self.buttonOffset2, 'maxPlayers': 4, 'location': Location(1, 1), 'readOnly': True } ],
            [ LocationButton, { 'x': 705, 'y': 250 - self.buttonOffset2, 'maxPlayers': 4, 'location': Location(1, 2), 'readOnly': True } ],
            [ LocationButton, { 'x': 678, 'y': 236 - self.buttonOffset2, 'maxPlayers': 4, 'location': Location(1, 3), 'readOnly': True } ],
            [ LocationButton, { 'x': 657, 'y': 210 - self.buttonOffset2, 'maxPlayers': 4, 'location': Location(1, 4), 'readOnly': True } ],
            [ LocationButton, { 'x': 635, 'y': 189 - self.buttonOffset2, 'maxPlayers': 4, 'location': Location(1, 5), 'readOnly': True } ],
            [ LocationButton, { 'x': 615, 'y': 166 - self.buttonOffset2, 'maxPlayers': 4, 'location': Location(1, 6), 'readOnly': True } ],
            [ LocationButton, { 'x': 615, 'y': 134 - self.buttonOffset2, 'maxPlayers': 4, 'location': Location(1, 7), 'readOnly': True } ],
            [ LocationButton, { 'x': 628, 'y': 105 - self.buttonOffset2, 'maxPlayers': 4, 'location': Location(1, 8), 'readOnly': True } ],
            [ LocationButton, { 'x': 658, 'y': 93 - self.buttonOffset2, 'maxPlayers': 4, 'location': Location(1, 9), 'readOnly': True } ],
            [ LocationButton, { 'x': 688, 'y': 82 - self.buttonOffset2, 'maxPlayers': 4, 'location': Location(1, 10), 'readOnly': True } ],
            [ LocationButton, { 'x': 715, 'y': 93 - self.buttonOffset2, 'maxPlayers': 4, 'location': Location(1, 11), 'readOnly': True } ],
            [ LocationButton, { 'x': 735, 'y': 120 - self.buttonOffset2, 'maxPlayers': 4, 'location': Location(1, 12), 'readOnly': True } ],
            [ LocationButton, { 'x': 750, 'y': 93 - self.buttonOffset2, 'maxPlayers': 4, 'location': Location(1, 13), 'readOnly': True } ],
            [ LocationButton, { 'x': 780, 'y': 82 - self.buttonOffset2, 'maxPlayers': 4, 'location': Location(1, 14), 'readOnly': True } ],
            [ LocationButton, { 'x': 810, 'y': 93 - self.buttonOffset2, 'maxPlayers': 4, 'location': Location(1, 15), 'readOnly': True } ],
            [ LocationButton, { 'x': 838, 'y': 108 - self.buttonOffset2, 'maxPlayers': 4, 'location': Location(1, 16), 'readOnly': True } ],
            [ LocationButton, { 'x': 852, 'y': 137 - self.buttonOffset2, 'maxPlayers': 4, 'location': Location(1, 17), 'readOnly': True } ],
            [ LocationButton, { 'x': 852, 'y': 166 - self.buttonOffset2, 'maxPlayers': 4, 'location': Location(1, 18), 'readOnly': True } ],
            [ LocationButton, { 'x': 830, 'y': 189 - self.buttonOffset2, 'maxPlayers': 4, 'location': Location(1, 19), 'readOnly': True } ],
            [ LocationButton, { 'x': 810, 'y': 212 - self.buttonOffset2, 'maxPlayers': 4, 'location': Location(1, 20), 'readOnly': True } ],
            [ LocationButton, { 'x': 791, 'y': 236 - self.buttonOffset2, 'maxPlayers': 4, 'location': Location(1, 21), 'readOnly': True } ],
            [ LocationButton, { 'x': 765, 'y': 250 - self.buttonOffset2, 'maxPlayers': 4, 'location': Location(1, 22), 'readOnly': True } ],
            
            [ LocationButton, { 'x': 779, 'y': 312 - self.buttonOffset2, 'maxPlayers': 4, 'location': Location(2, 1), 'readOnly': True } ],
            [ LocationButton, { 'x': 803, 'y': 282 - self.buttonOffset2, 'maxPlayers': 4, 'location': Location(2, 2), 'readOnly': True } ],
            [ LocationButton, { 'x': 818, 'y': 255 - self.buttonOffset2, 'maxPlayers': 4, 'location': Location(2, 3), 'readOnly': True } ], 
            [ LocationButton, { 'x': 840, 'y': 235 - self.buttonOffset2, 'maxPlayers': 4, 'location': Location(2, 4), 'readOnly': True } ],
            [ LocationButton, { 'x': 863, 'y': 213 - self.buttonOffset2, 'maxPlayers': 4, 'location': Location(2, 5), 'readOnly': True } ], 
            [ LocationButton, { 'x': 888, 'y': 192 - self.buttonOffset2, 'maxPlayers': 4, 'location': Location(2, 6), 'readOnly': True } ],
            [ LocationButton, { 'x': 918, 'y': 192 - self.buttonOffset2, 'maxPlayers': 4, 'location': Location(2, 7), 'readOnly': True } ],
            [ LocationButton, { 'x': 948, 'y': 204 - self.buttonOffset2, 'maxPlayers': 4, 'location': Location(2, 8), 'readOnly': True } ],
            [ LocationButton, { 'x': 960, 'y': 235 - self.buttonOffset2, 'maxPlayers': 4, 'location': Location(2, 9), 'readOnly': True } ],
            [ LocationButton, { 'x': 970, 'y': 265 - self.buttonOffset2, 'maxPlayers': 4, 'location': Location(2, 10), 'readOnly': True } ],
            [ LocationButton, { 'x': 957, 'y': 295 - self.buttonOffset2, 'maxPlayers': 4, 'location': Location(2, 11), 'readOnly': True } ],
            [ LocationButton, { 'x': 930, 'y': 310 - self.buttonOffset2, 'maxPlayers': 4, 'location': Location(2, 12), 'readOnly': True } ],
            [ LocationButton, { 'x': 957, 'y': 328 - self.buttonOffset2, 'maxPlayers': 4, 'location': Location(2, 13), 'readOnly': True } ],
            [ LocationButton, { 'x': 970, 'y': 357 - self.buttonOffset2, 'maxPlayers': 4, 'location': Location(2, 14), 'readOnly': True } ],
            [ LocationButton, { 'x': 960, 'y': 387 - self.buttonOffset2, 'maxPlayers': 4, 'location': Location(2, 15), 'readOnly': True } ],
            [ LocationButton, { 'x': 945, 'y': 415 - self.buttonOffset2, 'maxPlayers': 4, 'location': Location(2, 16), 'readOnly': True } ],
            [ LocationButton, { 'x': 915, 'y': 432 - self.buttonOffset2, 'maxPlayers': 4, 'location': Location(2, 17), 'readOnly': True } ],
            [ LocationButton, { 'x': 885, 'y': 432 - self.buttonOffset2, 'maxPlayers': 4, 'location': Location(2, 18), 'readOnly': True } ],
            [ LocationButton, { 'x': 863, 'y': 410 - self.buttonOffset2, 'maxPlayers': 4, 'location': Location(2, 19), 'readOnly': True } ],
            [ LocationButton, { 'x': 840, 'y': 389 - self.buttonOffset2, 'maxPlayers': 4, 'location': Location(2, 20), 'readOnly': True } ],
            [ LocationButton, { 'x': 818, 'y': 368 - self.buttonOffset2, 'maxPlayers': 4, 'location': Location(2, 21), 'readOnly': True } ],
            [ LocationButton, { 'x': 802, 'y': 342 - self.buttonOffset2, 'maxPlayers': 4, 'location': Location(2, 22), 'readOnly': True } ],
            
            [ LocationButton, { 'x': 735, 'y': 353 - self.buttonOffset2, 'maxPlayers': 4, 'location': Location(3, 1), 'readOnly': True } ],
            [ LocationButton, { 'x': 765, 'y': 378 - self.buttonOffset2, 'maxPlayers': 4, 'location': Location(3, 2), 'readOnly': True } ],
            [ LocationButton, { 'x': 791, 'y': 393 - self.buttonOffset2, 'maxPlayers': 4, 'location': Location(3, 3), 'readOnly': True } ],
            [ LocationButton, { 'x': 812, 'y': 415 - self.buttonOffset2, 'maxPlayers': 4, 'location': Location(3, 4), 'readOnly': True } ],
            [ LocationButton, { 'x': 832, 'y': 438 - self.buttonOffset2, 'maxPlayers': 4, 'location': Location(3, 5), 'readOnly': True } ],
            [ LocationButton, { 'x': 852, 'y': 466 - self.buttonOffset2, 'maxPlayers': 4, 'location': Location(3, 6), 'readOnly': True } ],
            [ LocationButton, { 'x': 852, 'y': 496 - self.buttonOffset2, 'maxPlayers': 4, 'location': Location(3, 7), 'readOnly': True } ],
            [ LocationButton, { 'x': 840, 'y': 524 - self.buttonOffset2, 'maxPlayers': 4, 'location': Location(3, 8), 'readOnly': True } ],
            [ LocationButton, { 'x': 810, 'y': 538 - self.buttonOffset2, 'maxPlayers': 4, 'location': Location(3, 9), 'readOnly': True } ],
            [ LocationButton, { 'x': 780, 'y': 548 - self.buttonOffset2, 'maxPlayers': 4, 'location': Location(3, 10), 'readOnly': True } ],
            [ LocationButton, { 'x': 753, 'y': 536 - self.buttonOffset2, 'maxPlayers': 4, 'location': Location(3, 11), 'readOnly': True } ],
            [ LocationButton, { 'x': 735, 'y': 510 - self.buttonOffset2, 'maxPlayers': 4, 'location': Location(3, 12), 'readOnly': True } ],
            [ LocationButton, { 'x': 719, 'y': 536 - self.buttonOffset2, 'maxPlayers': 4, 'location': Location(3, 13), 'readOnly': True } ],
            [ LocationButton, { 'x': 688, 'y': 548 - self.buttonOffset2, 'maxPlayers': 4, 'location': Location(3, 14), 'readOnly': True } ],
            [ LocationButton, { 'x': 660, 'y': 534 - self.buttonOffset2, 'maxPlayers': 4, 'location': Location(3, 15), 'readOnly': True } ],
            [ LocationButton, { 'x': 630, 'y': 521 - self.buttonOffset2, 'maxPlayers': 4, 'location': Location(3, 16), 'readOnly': True } ],
            [ LocationButton, { 'x': 616, 'y': 494 - self.buttonOffset2, 'maxPlayers': 4, 'location': Location(3, 17), 'readOnly': True } ],
            [ LocationButton, { 'x': 616, 'y': 462 - self.buttonOffset2, 'maxPlayers': 4, 'location': Location(3, 18), 'readOnly': True } ],
            [ LocationButton, { 'x': 638, 'y': 440 - self.buttonOffset2, 'maxPlayers': 4, 'location': Location(3, 19), 'readOnly': True } ],
            [ LocationButton, { 'x': 657, 'y': 415 - self.buttonOffset2, 'maxPlayers': 4, 'location': Location(3, 20), 'readOnly': True } ],
            [ LocationButton, { 'x': 678, 'y': 393 - self.buttonOffset2, 'maxPlayers': 4, 'location': Location(3, 21), 'readOnly': True } ],
            [ LocationButton, { 'x': 705, 'y': 378 - self.buttonOffset2, 'maxPlayers': 4, 'location': Location(3, 22), 'readOnly': True } ],
            
            [ LocationButton, { 'x': 692, 'y': 312 - self.buttonOffset2, 'maxPlayers': 4, 'location': Location(4, 1), 'readOnly': True } ],
            [ LocationButton, { 'x': 669, 'y': 342 - self.buttonOffset2, 'maxPlayers': 4, 'location': Location(4, 2), 'readOnly': True } ],
            [ LocationButton, { 'x': 655, 'y': 368 - self.buttonOffset2, 'maxPlayers': 4, 'location': Location(4, 3), 'readOnly': True } ],
            [ LocationButton, { 'x': 630, 'y': 389 - self.buttonOffset2, 'maxPlayers': 4, 'location': Location(4, 4), 'readOnly': True } ],
            [ LocationButton, { 'x': 606, 'y': 410 - self.buttonOffset2, 'maxPlayers': 4, 'location': Location(4, 5), 'readOnly': True } ],
            [ LocationButton, { 'x': 583, 'y': 432 - self.buttonOffset2, 'maxPlayers': 4, 'location': Location(4, 6), 'readOnly': True } ],
            [ LocationButton, { 'x': 553, 'y': 432 - self.buttonOffset2, 'maxPlayers': 4, 'location': Location(4, 7), 'readOnly': True } ],
            [ LocationButton, { 'x': 525, 'y': 420 - self.buttonOffset2, 'maxPlayers': 4, 'location': Location(4, 8), 'readOnly': True } ],
            [ LocationButton, { 'x': 510, 'y': 390 - self.buttonOffset2, 'maxPlayers': 4, 'location': Location(4, 9), 'readOnly': True } ],
            [ LocationButton, { 'x': 497, 'y': 360 - self.buttonOffset2, 'maxPlayers': 4, 'location': Location(4, 10), 'readOnly': True } ],
            [ LocationButton, { 'x': 512, 'y': 330 - self.buttonOffset2, 'maxPlayers': 4, 'location': Location(4, 11), 'readOnly': True } ],
            [ LocationButton, { 'x': 542, 'y': 314 - self.buttonOffset2, 'maxPlayers': 4, 'location': Location(4, 12), 'readOnly': True } ],
            [ LocationButton, { 'x': 512, 'y': 298 - self.buttonOffset2, 'maxPlayers': 4, 'location': Location(4, 13), 'readOnly': True } ],
            [ LocationButton, { 'x': 500, 'y': 267 - self.buttonOffset2, 'maxPlayers': 4, 'location': Location(4, 14), 'readOnly': True } ],
            [ LocationButton, { 'x': 512, 'y': 238 - self.buttonOffset2, 'maxPlayers': 4, 'location': Location(4, 15), 'readOnly': True } ],
            [ LocationButton, { 'x': 525, 'y': 208 - self.buttonOffset2, 'maxPlayers': 4, 'location': Location(4, 16), 'readOnly': True } ],
            [ LocationButton, { 'x': 553, 'y': 195 - self.buttonOffset2, 'maxPlayers': 4, 'location': Location(4, 17), 'readOnly': True } ],
            [ LocationButton, { 'x': 583, 'y': 195 - self.buttonOffset2, 'maxPlayers': 4, 'location': Location(4, 18), 'readOnly': True } ],
            [ LocationButton, { 'x': 606, 'y': 215 - self.buttonOffset2, 'maxPlayers': 4, 'location': Location(4, 19), 'readOnly': True } ],
            [ LocationButton, { 'x': 630, 'y': 235 - self.buttonOffset2, 'maxPlayers': 4, 'location': Location(4, 20), 'readOnly': True } ],
            [ LocationButton, { 'x': 655, 'y': 256 - self.buttonOffset2, 'maxPlayers': 4, 'location': Location(4, 21), 'readOnly': True } ],
            [ LocationButton, { 'x': 669, 'y': 282 - self.buttonOffset2, 'maxPlayers': 4, 'location': Location(4, 22), 'readOnly': True } ],
            
            # Left up
            [ LocationButton, { 'x': 735 - 147.5, 'y': 275 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(1, 1), 'readOnly': True } ],
            [ LocationButton, { 'x': 705 - 147.5, 'y': 250 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(1, 2), 'readOnly': True } ],
            [ LocationButton, { 'x': 678 - 147.5, 'y': 236 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(1, 3), 'readOnly': True } ],
            [ LocationButton, { 'x': 655 - 147.5, 'y': 210 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(1, 4), 'readOnly': True } ],
            [ LocationButton, { 'x': 635 - 147.5, 'y': 189 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(1, 5), 'readOnly': True } ],
            [ LocationButton, { 'x': 615 - 147.5, 'y': 163 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(1, 6), 'readOnly': True } ],
            [ LocationButton, { 'x': 615 - 147.5, 'y': 131 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(1, 7), 'readOnly': True } ],
            [ LocationButton, { 'x': 628 - 147.5, 'y': 105 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(1, 8), 'readOnly': True } ],
            [ LocationButton, { 'x': 658 - 147.5, 'y': 90 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(1, 9), 'readOnly': True } ],
            [ LocationButton, { 'x': 688 - 147.5, 'y': 79 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(1, 10), 'readOnly': True } ],
            [ LocationButton, { 'x': 716 - 147.5, 'y': 90 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(1, 11), 'readOnly': True } ],
            [ LocationButton, { 'x': 735 - 147.5, 'y': 120 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(1, 12), 'readOnly': True } ],
            [ LocationButton, { 'x': 750 - 147.5, 'y': 90 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(1, 13), 'readOnly': True } ],
            [ LocationButton, { 'x': 780 - 147.5, 'y': 79 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(1, 14), 'readOnly': True } ],
            [ LocationButton, { 'x': 812 - 147.5, 'y': 90 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(1, 15), 'readOnly': True } ],
            [ LocationButton, { 'x': 840 - 147.5, 'y': 106 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(1, 16), 'readOnly': True } ],
            [ LocationButton, { 'x': 854 - 147.5, 'y': 137 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(1, 17), 'readOnly': True } ],
            [ LocationButton, { 'x': 854 - 147.5, 'y': 166 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(1, 18), 'readOnly': True } ],
            [ LocationButton, { 'x': 833 - 147.5, 'y': 183 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(1, 19), 'readOnly': True } ],
            [ LocationButton, { 'x': 812 - 147.5, 'y': 210 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(1, 20), 'readOnly': True } ],
            [ LocationButton, { 'x': 791 - 147.5, 'y': 236 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(1, 21), 'readOnly': True } ],
            [ LocationButton, { 'x': 765 - 147.5, 'y': 250 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(1, 22), 'readOnly': True } ],
            
            # Right up
            [ LocationButton, { 'x': 735 + 142, 'y': 275 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(2, 1), 'readOnly': True } ],
            [ LocationButton, { 'x': 705 + 142, 'y': 249 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(2, 2), 'readOnly': True } ],
            [ LocationButton, { 'x': 676 + 142, 'y': 232 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(2, 3), 'readOnly': True } ],
            [ LocationButton, { 'x': 655 + 142, 'y': 210 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(2, 4), 'readOnly': True } ],
            [ LocationButton, { 'x': 632 + 142, 'y': 189 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(2, 5), 'readOnly': True } ],
            [ LocationButton, { 'x': 612 + 142, 'y': 160 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(2, 6), 'readOnly': True } ],
            [ LocationButton, { 'x': 612 + 142, 'y': 132 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(2, 7), 'readOnly': True } ],
            [ LocationButton, { 'x': 625 + 142, 'y': 99 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(2, 8), 'readOnly': True } ],
            [ LocationButton, { 'x': 655 + 142, 'y': 91 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(2, 9), 'readOnly': True } ],
            [ LocationButton, { 'x': 688 + 142, 'y': 79 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(2, 10), 'readOnly': True } ],
            [ LocationButton, { 'x': 715 + 142, 'y': 91 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(2, 11), 'readOnly': True } ],
            [ LocationButton, { 'x': 733 + 142, 'y': 118 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(2, 12), 'readOnly': True } ],
            [ LocationButton, { 'x': 750 + 142, 'y': 91 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(2, 13), 'readOnly': True } ],
            [ LocationButton, { 'x': 780 + 142, 'y': 79 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(2, 14), 'readOnly': True } ],
            [ LocationButton, { 'x': 810 + 142, 'y': 91 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(2, 15), 'readOnly': True } ],
            [ LocationButton, { 'x': 838 + 142, 'y': 100 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(2, 16), 'readOnly': True } ],
            [ LocationButton, { 'x': 852 + 142, 'y': 137 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(2, 17), 'readOnly': True } ],
            [ LocationButton, { 'x': 852 + 142, 'y': 166 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(2, 18), 'readOnly': True } ],
            [ LocationButton, { 'x': 830 + 142, 'y': 189 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(2, 19), 'readOnly': True } ],
            [ LocationButton, { 'x': 810 + 142, 'y': 212 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(2, 20), 'readOnly': True } ],
            [ LocationButton, { 'x': 791 + 142, 'y': 236 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(2, 21), 'readOnly': True } ],
            [ LocationButton, { 'x': 765 + 142, 'y': 249 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(2, 22), 'readOnly': True } ], 
            
            # Right
            [ LocationButton, { 'x': 779 + self.buttonOffset, 'y': 312 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(3, 1), 'readOnly': True } ],
            [ LocationButton, { 'x': 800 + self.buttonOffset, 'y': 282 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(3, 2), 'readOnly': True } ],
            [ LocationButton, { 'x': 816 + self.buttonOffset, 'y': 255 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(3, 3), 'readOnly': True } ], 
            [ LocationButton, { 'x': 840 + self.buttonOffset, 'y': 235 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(3, 4), 'readOnly': True } ],
            [ LocationButton, { 'x': 863 + self.buttonOffset, 'y': 215 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(3, 5), 'readOnly': True } ], 
            [ LocationButton, { 'x': 888 + self.buttonOffset, 'y': 192 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(3, 6), 'readOnly': True } ],
            [ LocationButton, { 'x': 918 + self.buttonOffset, 'y': 192 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(3, 7), 'readOnly': True } ],
            [ LocationButton, { 'x': 948 + self.buttonOffset, 'y': 204 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(3, 8), 'readOnly': True } ],
            [ LocationButton, { 'x': 960 + self.buttonOffset, 'y': 235 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(3, 9), 'readOnly': True } ],
            [ LocationButton, { 'x': 973 + self.buttonOffset, 'y': 265 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(3, 10), 'readOnly': True } ],
            [ LocationButton, { 'x': 957 + self.buttonOffset, 'y': 295 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(3, 11), 'readOnly': True } ],
            [ LocationButton, { 'x': 930 + self.buttonOffset, 'y': 312 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(3, 12), 'readOnly': True } ],
            [ LocationButton, { 'x': 957 + self.buttonOffset, 'y': 327 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(3, 13), 'readOnly': True } ],
            [ LocationButton, { 'x': 970 + self.buttonOffset, 'y': 357 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(3, 14), 'readOnly': True } ],
            [ LocationButton, { 'x': 960 + self.buttonOffset, 'y': 387 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(3, 15), 'readOnly': True } ],
            [ LocationButton, { 'x': 945 + self.buttonOffset, 'y': 415 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(3, 16), 'readOnly': True } ],
            [ LocationButton, { 'x': 915 + self.buttonOffset, 'y': 432 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(3, 17), 'readOnly': True } ],
            [ LocationButton, { 'x': 885 + self.buttonOffset, 'y': 432 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(3, 18), 'readOnly': True } ],
            [ LocationButton, { 'x': 863 + self.buttonOffset, 'y': 410 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(3, 19), 'readOnly': True } ],
            [ LocationButton, { 'x': 840 + self.buttonOffset, 'y': 389 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(3, 20), 'readOnly': True } ],
            [ LocationButton, { 'x': 816 + self.buttonOffset, 'y': 368 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(3, 21), 'readOnly': True } ],
            [ LocationButton, { 'x': 800 + self.buttonOffset, 'y': 342 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(3, 22), 'readOnly': True } ],
            
            # Right down
            [ LocationButton, { 'x': 736 + 142, 'y': 350 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(4, 1), 'readOnly': True } ],
            [ LocationButton, { 'x': 706 + 142, 'y': 377 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(4, 2), 'readOnly': True } ],
            [ LocationButton, { 'x': 681 + 142, 'y': 392 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(4, 3), 'readOnly': True } ],
            [ LocationButton, { 'x': 657 + 145, 'y': 415 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(4, 4), 'readOnly': True } ],
            [ LocationButton, { 'x': 637 + 145, 'y': 440 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(4, 5), 'readOnly': True } ],
            [ LocationButton, { 'x': 617 + 142, 'y': 466 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(4, 6), 'readOnly': True } ],
            [ LocationButton, { 'x': 617 + 142, 'y': 494 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(4, 7), 'readOnly': True } ],
            [ LocationButton, { 'x': 633 + 142, 'y': 523 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(4, 8), 'readOnly': True } ],
            [ LocationButton, { 'x': 658 + 145, 'y': 540 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(4, 9), 'readOnly': True } ],
            [ LocationButton, { 'x': 688 + 145, 'y': 550 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(4, 10), 'readOnly': True } ],
            [ LocationButton, { 'x': 717 + 145, 'y': 535 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(4, 11), 'readOnly': True } ],
            [ LocationButton, { 'x': 736 + 145, 'y': 510 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(4, 12), 'readOnly': True } ],
            [ LocationButton, { 'x': 754 + 145, 'y': 535 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(4, 13), 'readOnly': True } ],
            [ LocationButton, { 'x': 780 + 145, 'y': 550 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(4, 14), 'readOnly': True } ],
            [ LocationButton, { 'x': 811 + 145, 'y': 540 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(4, 15), 'readOnly': True } ],
            [ LocationButton, { 'x': 840 + 145, 'y': 525 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(4, 16), 'readOnly': True } ],
            [ LocationButton, { 'x': 854 + 145, 'y': 494 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(4, 17), 'readOnly': True } ],
            [ LocationButton, { 'x': 854 + 145, 'y': 466 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(4, 18), 'readOnly': True } ],
            [ LocationButton, { 'x': 832 + 145, 'y': 440 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(4, 19), 'readOnly': True } ],
            [ LocationButton, { 'x': 812 + 145, 'y': 415 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(4, 20), 'readOnly': True } ],
            [ LocationButton, { 'x': 791 + 145, 'y': 392 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(4, 21), 'readOnly': True } ],
            [ LocationButton, { 'x': 765 + 145, 'y': 377 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(4, 22), 'readOnly': True } ],
            
            # Left down
            [ LocationButton, { 'x': 736 - 145, 'y': 352 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(5, 1), 'readOnly': True } ],
            [ LocationButton, { 'x': 705 - 145, 'y': 378 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(5, 2), 'readOnly': True } ],
            [ LocationButton, { 'x': 678 - 145, 'y': 390 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(5, 3), 'readOnly': True } ],
            [ LocationButton, { 'x': 656 - 145, 'y': 416 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(5, 4), 'readOnly': True } ],
            [ LocationButton, { 'x': 637 - 145, 'y': 440 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(5, 5), 'readOnly': True } ],
            [ LocationButton, { 'x': 617 - 145, 'y': 466 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(5, 6), 'readOnly': True } ],
            [ LocationButton, { 'x': 617 - 145, 'y': 494 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(5, 7), 'readOnly': True } ],
            [ LocationButton, { 'x': 628 - 145, 'y': 525 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(5, 8), 'readOnly': True } ],
            [ LocationButton, { 'x': 658 - 145, 'y': 540 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(5, 9), 'readOnly': True } ],
            [ LocationButton, { 'x': 688 - 145, 'y': 550 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(5, 10), 'readOnly': True } ],
            [ LocationButton, { 'x': 720 - 145, 'y': 535 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(5, 11), 'readOnly': True } ],
            [ LocationButton, { 'x': 738 - 145, 'y': 510 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(5, 12), 'readOnly': True } ],
            [ LocationButton, { 'x': 755 - 145, 'y': 535 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(5, 13), 'readOnly': True } ],
            [ LocationButton, { 'x': 785 - 145, 'y': 550 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(5, 14), 'readOnly': True } ],
            [ LocationButton, { 'x': 814 - 145, 'y': 540 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(5, 15), 'readOnly': True } ],
            [ LocationButton, { 'x': 849 - 145, 'y': 528 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(5, 16), 'readOnly': True } ],
            [ LocationButton, { 'x': 859 - 145, 'y': 494 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(5, 17), 'readOnly': True } ],
            [ LocationButton, { 'x': 859 - 145, 'y': 466 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(5, 18), 'readOnly': True } ],
            [ LocationButton, { 'x': 837 - 145, 'y': 438 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(5, 19), 'readOnly': True } ],
            [ LocationButton, { 'x': 821 - 145, 'y': 418 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(5, 20), 'readOnly': True } ],
            [ LocationButton, { 'x': 795 - 145, 'y': 390 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(5, 21), 'readOnly': True } ],
            [ LocationButton, { 'x': 765 - 145, 'y': 378 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(5, 22), 'readOnly': True } ],
            
            # Left 
            [ LocationButton, { 'x': 692 - self.buttonOffset, 'y': 317 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(6, 1), 'readOnly': True } ],
            [ LocationButton, { 'x': 669 - self.buttonOffset, 'y': 347 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(6, 2), 'readOnly': True } ],
            [ LocationButton, { 'x': 652 - self.buttonOffset, 'y': 375 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(6, 3), 'readOnly': True } ],
            [ LocationButton, { 'x': 630 - self.buttonOffset, 'y': 396 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(6, 4), 'readOnly': True } ],
            [ LocationButton, { 'x': 606 - self.buttonOffset, 'y': 416 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(6, 5), 'readOnly': True } ],
            [ LocationButton, { 'x': 583 - self.buttonOffset, 'y': 437 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(6, 6), 'readOnly': True } ],
            [ LocationButton, { 'x': 553 - self.buttonOffset, 'y': 437 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(6, 7), 'readOnly': True } ],
            [ LocationButton, { 'x': 525 - self.buttonOffset, 'y': 423 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(6, 8), 'readOnly': True } ],
            [ LocationButton, { 'x': 510 - self.buttonOffset, 'y': 393 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(6, 9), 'readOnly': True } ],
            [ LocationButton, { 'x': 497 - self.buttonOffset, 'y': 363 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(6, 10), 'readOnly': True } ],
            [ LocationButton, { 'x': 512 - self.buttonOffset, 'y': 333 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(6, 11), 'readOnly': True } ],
            [ LocationButton, { 'x': 542 - self.buttonOffset, 'y': 318 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(6, 12), 'readOnly': True } ],
            [ LocationButton, { 'x': 512 - self.buttonOffset, 'y': 300 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(6, 13), 'readOnly': True } ],
            [ LocationButton, { 'x': 500 - self.buttonOffset, 'y': 270 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(6, 14), 'readOnly': True } ],
            [ LocationButton, { 'x': 512 - self.buttonOffset, 'y': 240 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(6, 15), 'readOnly': True } ],
            [ LocationButton, { 'x': 525 - self.buttonOffset, 'y': 208 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(6, 16), 'readOnly': True } ],
            [ LocationButton, { 'x': 553 - self.buttonOffset, 'y': 196 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(6, 17), 'readOnly': True } ],
            [ LocationButton, { 'x': 583 - self.buttonOffset, 'y': 196 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(6, 18), 'readOnly': True } ],
            [ LocationButton, { 'x': 606 - self.buttonOffset, 'y': 217 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(6, 19), 'readOnly': True } ],
            [ LocationButton, { 'x': 630 - self.buttonOffset, 'y': 237 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(6, 20), 'readOnly': True } ],
            [ LocationButton, { 'x': 655 - self.buttonOffset, 'y': 258 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(6, 21), 'readOnly': True } ],
            [ LocationButton, { 'x': 670 - self.buttonOffset, 'y': 287 - self.buttonOffset2, 'maxPlayers': 6, 'location': Location(6, 22), 'readOnly': True } ],
        ]
        
        playerButtonX = ui.SPACING_SM
        playerButtonY = ui.SPACING_MD + ui.SPACING_SM + 50 + ui.SPACING_MD + ui.SPACING_SM
        
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
