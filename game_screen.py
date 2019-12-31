import ui
import player_manager
from player import Player
from screen import Screen
from button import Button
from selectable_button import SelectableButton
from dice_manager import DiceManager
from location_button  import LocationButton
from player_button import PlayerButton
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

    def setup(self):
        playerManager = self.app.getModule('playerManager')
        imageLoader = self.app.getModule('imageLoader')

        imageLoader.load('board-players4.png')
        imageLoader.load('board-players6.png')
        
        self.boardX = width / 2 - (self.boardWidth / 3.2)
        self.boardY = 40

    def getHandle(self):
        return 'game'

    def draw(self):
        playerManager = self.app.getModule('playerManager')
        turnManager = self.app.getModule('turnManager')

        imageLoader = self.app.getModule('imageLoader')  
        botManager = self.app.getModule('botManager')  

        print(playerManager.checkWinLose())
        
        background(ui.COLOR_RED_LIGHT)
        fill(ui.COLOR_TEXT)
        textSize(30);
        textAlign(LEFT);
        text('Huidige beurt:', 60, 60)
            
        if playerManager.maxPlayers == 6:
            boardImage = imageLoader.get('board-players6')
        else:
            boardImage = imageLoader.get('board-players4')
            
        image(boardImage, self.boardX, self.boardY, self.boardWidth, self.boardHeight)

    def keyPressed(self):
        if keyCode == 32:
            startScreen = self.app.getScreen('start')
            self.app.setCurrentScreen(startScreen)

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

    def rollDice(self):
        diceManager = self.app.getModule('diceManager')
        diceManager.rollDice()

    def getSubModules(self):
        playerManager = self.app.getModule('playerManager')
        modules = [            
            [ DiceManager, {  } ],
            [ TurnManager, {  } ],
            [ BotManager, {  } ],
        
            [ LocationButton, { 'x': 735, 'y': 275 - self.buttonOffset2, 'maxPlayers': 4, 'location': 1, 'readOnly': True } ],
            [ LocationButton, { 'x': 705, 'y': 250 - self.buttonOffset2, 'maxPlayers': 4, 'location': 2, 'readOnly': True } ],
            [ LocationButton, { 'x': 678, 'y': 236 - self.buttonOffset2, 'maxPlayers': 4, 'location': 3, 'readOnly': True } ],
            [ LocationButton, { 'x': 657, 'y': 210 - self.buttonOffset2, 'maxPlayers': 4, 'location': 4, 'readOnly': True } ],
            [ LocationButton, { 'x': 635, 'y': 189 - self.buttonOffset2, 'maxPlayers': 4, 'location': 5, 'readOnly': True } ],
            [ LocationButton, { 'x': 615, 'y': 166 - self.buttonOffset2, 'maxPlayers': 4, 'location': 6, 'readOnly': True } ],
            [ LocationButton, { 'x': 615, 'y': 134 - self.buttonOffset2, 'maxPlayers': 4, 'location': 7, 'readOnly': True } ],
            [ LocationButton, { 'x': 628, 'y': 105 - self.buttonOffset2, 'maxPlayers': 4, 'location': 8, 'readOnly': True } ],
            [ LocationButton, { 'x': 658, 'y': 93 - self.buttonOffset2, 'maxPlayers': 4, 'location': 9, 'readOnly': True } ],
            [ LocationButton, { 'x': 688, 'y': 82 - self.buttonOffset2, 'maxPlayers': 4, 'location': 10, 'readOnly': True } ],
            [ LocationButton, { 'x': 715, 'y': 93 - self.buttonOffset2, 'maxPlayers': 4, 'location': 11, 'readOnly': True } ],
            [ LocationButton, { 'x': 735, 'y': 120 - self.buttonOffset2, 'maxPlayers': 4, 'location': 12, 'readOnly': True } ],
            [ LocationButton, { 'x': 750, 'y': 93 - self.buttonOffset2, 'maxPlayers': 4, 'location': 13, 'readOnly': True } ],
            [ LocationButton, { 'x': 780, 'y': 82 - self.buttonOffset2, 'maxPlayers': 4, 'location': 14, 'readOnly': True } ],
            [ LocationButton, { 'x': 810, 'y': 93 - self.buttonOffset2, 'maxPlayers': 4, 'location': 15, 'readOnly': True } ],
            [ LocationButton, { 'x': 838, 'y': 108 - self.buttonOffset2, 'maxPlayers': 4, 'location': 16, 'readOnly': True } ],
            [ LocationButton, { 'x': 852, 'y': 137 - self.buttonOffset2, 'maxPlayers': 4, 'location': 17, 'readOnly': True } ],
            [ LocationButton, { 'x': 852, 'y': 166 - self.buttonOffset2, 'maxPlayers': 4, 'location': 18, 'readOnly': True } ],
            [ LocationButton, { 'x': 830, 'y': 189 - self.buttonOffset2, 'maxPlayers': 4, 'location': 19, 'readOnly': True } ],
            [ LocationButton, { 'x': 810, 'y': 212 - self.buttonOffset2, 'maxPlayers': 4, 'location': 20, 'readOnly': True } ],
            [ LocationButton, { 'x': 791, 'y': 236 - self.buttonOffset2, 'maxPlayers': 4, 'location': 21, 'readOnly': True } ],
            [ LocationButton, { 'x': 765, 'y': 250 - self.buttonOffset2, 'maxPlayers': 4, 'location': 22, 'readOnly': True } ],
            
            [ LocationButton, { 'x': 779, 'y': 312 - self.buttonOffset2, 'maxPlayers': 4, 'location': 23, 'readOnly': True } ],
            [ LocationButton, { 'x': 803, 'y': 282 - self.buttonOffset2, 'maxPlayers': 4, 'location': 24, 'readOnly': True } ],
            [ LocationButton, { 'x': 818, 'y': 255 - self.buttonOffset2, 'maxPlayers': 4, 'location': 25, 'readOnly': True } ], 
            [ LocationButton, { 'x': 840, 'y': 235 - self.buttonOffset2, 'maxPlayers': 4, 'location': 26, 'readOnly': True } ],
            [ LocationButton, { 'x': 863, 'y': 213 - self.buttonOffset2, 'maxPlayers': 4, 'location': 27, 'readOnly': True } ], 
            [ LocationButton, { 'x': 888, 'y': 192 - self.buttonOffset2, 'maxPlayers': 4, 'location': 28, 'readOnly': True } ],
            [ LocationButton, { 'x': 918, 'y': 192 - self.buttonOffset2, 'maxPlayers': 4, 'location': 29, 'readOnly': True } ],
            [ LocationButton, { 'x': 948, 'y': 204 - self.buttonOffset2, 'maxPlayers': 4, 'location': 30, 'readOnly': True } ],
            [ LocationButton, { 'x': 960, 'y': 235 - self.buttonOffset2, 'maxPlayers': 4, 'location': 31, 'readOnly': True } ],
            [ LocationButton, { 'x': 970, 'y': 265 - self.buttonOffset2, 'maxPlayers': 4, 'location': 32, 'readOnly': True } ],
            [ LocationButton, { 'x': 957, 'y': 295 - self.buttonOffset2, 'maxPlayers': 4, 'location': 33, 'readOnly': True } ],
            [ LocationButton, { 'x': 930, 'y': 310 - self.buttonOffset2, 'maxPlayers': 4, 'location': 34, 'readOnly': True } ],
            [ LocationButton, { 'x': 957, 'y': 328 - self.buttonOffset2, 'maxPlayers': 4, 'location': 35, 'readOnly': True } ],
            [ LocationButton, { 'x': 970, 'y': 357 - self.buttonOffset2, 'maxPlayers': 4, 'location': 36, 'readOnly': True } ],
            [ LocationButton, { 'x': 960, 'y': 387 - self.buttonOffset2, 'maxPlayers': 4, 'location': 37, 'readOnly': True } ],
            [ LocationButton, { 'x': 945, 'y': 415 - self.buttonOffset2, 'maxPlayers': 4, 'location': 38, 'readOnly': True } ],
            [ LocationButton, { 'x': 915, 'y': 432 - self.buttonOffset2, 'maxPlayers': 4, 'location': 39, 'readOnly': True } ],
            [ LocationButton, { 'x': 885, 'y': 432 - self.buttonOffset2, 'maxPlayers': 4, 'location': 40, 'readOnly': True } ],
            [ LocationButton, { 'x': 863, 'y': 410 - self.buttonOffset2, 'maxPlayers': 4, 'location': 41, 'readOnly': True } ],
            [ LocationButton, { 'x': 840, 'y': 389 - self.buttonOffset2, 'maxPlayers': 4, 'location': 42, 'readOnly': True } ],
            [ LocationButton, { 'x': 818, 'y': 368 - self.buttonOffset2, 'maxPlayers': 4, 'location': 43, 'readOnly': True } ],
            [ LocationButton, { 'x': 802, 'y': 342 - self.buttonOffset2, 'maxPlayers': 4, 'location': 44, 'readOnly': True } ],
            
            [ LocationButton, { 'x': 735, 'y': 353 - self.buttonOffset2, 'maxPlayers': 4, 'location': 45, 'readOnly': True } ],
            [ LocationButton, { 'x': 765, 'y': 378 - self.buttonOffset2, 'maxPlayers': 4, 'location': 46, 'readOnly': True } ],
            [ LocationButton, { 'x': 791, 'y': 393 - self.buttonOffset2, 'maxPlayers': 4, 'location': 47, 'readOnly': True } ],
            [ LocationButton, { 'x': 812, 'y': 415 - self.buttonOffset2, 'maxPlayers': 4, 'location': 48, 'readOnly': True } ],
            [ LocationButton, { 'x': 832, 'y': 438 - self.buttonOffset2, 'maxPlayers': 4, 'location': 49, 'readOnly': True } ],
            [ LocationButton, { 'x': 852, 'y': 466 - self.buttonOffset2, 'maxPlayers': 4, 'location': 50, 'readOnly': True } ],
            [ LocationButton, { 'x': 852, 'y': 496 - self.buttonOffset2, 'maxPlayers': 4, 'location': 51, 'readOnly': True } ],
            [ LocationButton, { 'x': 840, 'y': 524 - self.buttonOffset2, 'maxPlayers': 4, 'location': 52, 'readOnly': True } ],
            [ LocationButton, { 'x': 810, 'y': 538 - self.buttonOffset2, 'maxPlayers': 4, 'location': 53, 'readOnly': True } ],
            [ LocationButton, { 'x': 780, 'y': 548 - self.buttonOffset2, 'maxPlayers': 4, 'location': 54, 'readOnly': True } ],
            [ LocationButton, { 'x': 753, 'y': 536 - self.buttonOffset2, 'maxPlayers': 4, 'location': 55, 'readOnly': True } ],
            [ LocationButton, { 'x': 735, 'y': 510 - self.buttonOffset2, 'maxPlayers': 4, 'location': 56, 'readOnly': True } ],
            [ LocationButton, { 'x': 719, 'y': 536 - self.buttonOffset2, 'maxPlayers': 4, 'location': 57, 'readOnly': True } ],
            [ LocationButton, { 'x': 688, 'y': 548 - self.buttonOffset2, 'maxPlayers': 4, 'location': 58, 'readOnly': True } ],
            [ LocationButton, { 'x': 660, 'y': 534 - self.buttonOffset2, 'maxPlayers': 4, 'location': 59, 'readOnly': True } ],
            [ LocationButton, { 'x': 630, 'y': 521 - self.buttonOffset2, 'maxPlayers': 4, 'location': 60, 'readOnly': True } ],
            [ LocationButton, { 'x': 616, 'y': 494 - self.buttonOffset2, 'maxPlayers': 4, 'location': 61, 'readOnly': True } ],
            [ LocationButton, { 'x': 616, 'y': 462 - self.buttonOffset2, 'maxPlayers': 4, 'location': 62, 'readOnly': True } ],
            [ LocationButton, { 'x': 638, 'y': 440 - self.buttonOffset2, 'maxPlayers': 4, 'location': 63, 'readOnly': True } ],
            [ LocationButton, { 'x': 657, 'y': 415 - self.buttonOffset2, 'maxPlayers': 4, 'location': 64, 'readOnly': True } ],
            [ LocationButton, { 'x': 678, 'y': 393 - self.buttonOffset2, 'maxPlayers': 4, 'location': 65, 'readOnly': True } ],
            [ LocationButton, { 'x': 705, 'y': 378 - self.buttonOffset2, 'maxPlayers': 4, 'location': 66, 'readOnly': True } ],
            
            [ LocationButton, { 'x': 692, 'y': 312 - self.buttonOffset2, 'maxPlayers': 4, 'location': 67, 'readOnly': True } ],
            [ LocationButton, { 'x': 669, 'y': 342 - self.buttonOffset2, 'maxPlayers': 4, 'location': 68, 'readOnly': True } ],
            [ LocationButton, { 'x': 655, 'y': 368 - self.buttonOffset2, 'maxPlayers': 4, 'location': 69, 'readOnly': True } ],
            [ LocationButton, { 'x': 630, 'y': 389 - self.buttonOffset2, 'maxPlayers': 4, 'location': 70, 'readOnly': True } ],
            [ LocationButton, { 'x': 606, 'y': 410 - self.buttonOffset2, 'maxPlayers': 4, 'location': 71, 'readOnly': True } ],
            [ LocationButton, { 'x': 583, 'y': 432 - self.buttonOffset2, 'maxPlayers': 4, 'location': 72, 'readOnly': True } ],
            [ LocationButton, { 'x': 553, 'y': 432 - self.buttonOffset2, 'maxPlayers': 4, 'location': 73, 'readOnly': True } ],
            [ LocationButton, { 'x': 525, 'y': 420 - self.buttonOffset2, 'maxPlayers': 4, 'location': 74, 'readOnly': True } ],
            [ LocationButton, { 'x': 510, 'y': 390 - self.buttonOffset2, 'maxPlayers': 4, 'location': 75, 'readOnly': True } ],
            [ LocationButton, { 'x': 497, 'y': 360 - self.buttonOffset2, 'maxPlayers': 4, 'location': 76, 'readOnly': True } ],
            [ LocationButton, { 'x': 512, 'y': 330 - self.buttonOffset2, 'maxPlayers': 4, 'location': 77, 'readOnly': True } ],
            [ LocationButton, { 'x': 542, 'y': 314 - self.buttonOffset2, 'maxPlayers': 4, 'location': 78, 'readOnly': True } ],
            [ LocationButton, { 'x': 512, 'y': 298 - self.buttonOffset2, 'maxPlayers': 4, 'location': 79, 'readOnly': True } ],
            [ LocationButton, { 'x': 500, 'y': 267 - self.buttonOffset2, 'maxPlayers': 4, 'location': 80, 'readOnly': True } ],
            [ LocationButton, { 'x': 512, 'y': 238 - self.buttonOffset2, 'maxPlayers': 4, 'location': 81, 'readOnly': True } ],
            [ LocationButton, { 'x': 525, 'y': 208 - self.buttonOffset2, 'maxPlayers': 4, 'location': 82, 'readOnly': True } ],
            [ LocationButton, { 'x': 553, 'y': 195 - self.buttonOffset2, 'maxPlayers': 4, 'location': 83, 'readOnly': True } ],
            [ LocationButton, { 'x': 583, 'y': 195 - self.buttonOffset2, 'maxPlayers': 4, 'location': 84, 'readOnly': True } ],
            [ LocationButton, { 'x': 606, 'y': 215 - self.buttonOffset2, 'maxPlayers': 4, 'location': 85, 'readOnly': True } ],
            [ LocationButton, { 'x': 630, 'y': 235 - self.buttonOffset2, 'maxPlayers': 4, 'location': 86, 'readOnly': True } ],
            [ LocationButton, { 'x': 655, 'y': 256 - self.buttonOffset2, 'maxPlayers': 4, 'location': 87, 'readOnly': True } ],
            [ LocationButton, { 'x': 669, 'y': 282 - self.buttonOffset2, 'maxPlayers': 4, 'location': 88, 'readOnly': True } ],
            
            # Left up
            [ LocationButton, { 'x': 735 - 147.5, 'y': 275 - self.buttonOffset2, 'maxPlayers': 6, 'location': 1, 'readOnly': True } ],
            [ LocationButton, { 'x': 705 - 147.5, 'y': 250 - self.buttonOffset2, 'maxPlayers': 6, 'location': 2, 'readOnly': True } ],
            [ LocationButton, { 'x': 678 - 147.5, 'y': 236 - self.buttonOffset2, 'maxPlayers': 6, 'location': 3, 'readOnly': True } ],
            [ LocationButton, { 'x': 655 - 147.5, 'y': 210 - self.buttonOffset2, 'maxPlayers': 6, 'location': 4, 'readOnly': True } ],
            [ LocationButton, { 'x': 635 - 147.5, 'y': 189 - self.buttonOffset2, 'maxPlayers': 6, 'location': 5, 'readOnly': True } ],
            [ LocationButton, { 'x': 615 - 147.5, 'y': 163 - self.buttonOffset2, 'maxPlayers': 6, 'location': 6, 'readOnly': True } ],
            [ LocationButton, { 'x': 615 - 147.5, 'y': 131 - self.buttonOffset2, 'maxPlayers': 6, 'location': 7, 'readOnly': True } ],
            [ LocationButton, { 'x': 628 - 147.5, 'y': 105 - self.buttonOffset2, 'maxPlayers': 6, 'location': 8, 'readOnly': True } ],
            [ LocationButton, { 'x': 658 - 147.5, 'y': 90 - self.buttonOffset2, 'maxPlayers': 6, 'location': 9, 'readOnly': True } ],
            [ LocationButton, { 'x': 688 - 147.5, 'y': 79 - self.buttonOffset2, 'maxPlayers': 6, 'location': 10, 'readOnly': True } ],
            [ LocationButton, { 'x': 716 - 147.5, 'y': 90 - self.buttonOffset2, 'maxPlayers': 6, 'location': 11, 'readOnly': True } ],
            [ LocationButton, { 'x': 735 - 147.5, 'y': 120 - self.buttonOffset2, 'maxPlayers': 6, 'location': 12, 'readOnly': True } ],
            [ LocationButton, { 'x': 750 - 147.5, 'y': 90 - self.buttonOffset2, 'maxPlayers': 6, 'location': 13, 'readOnly': True } ],
            [ LocationButton, { 'x': 780 - 147.5, 'y': 79 - self.buttonOffset2, 'maxPlayers': 6, 'location': 14, 'readOnly': True } ],
            [ LocationButton, { 'x': 812 - 147.5, 'y': 90 - self.buttonOffset2, 'maxPlayers': 6, 'location': 15, 'readOnly': True } ],
            [ LocationButton, { 'x': 840 - 147.5, 'y': 106 - self.buttonOffset2, 'maxPlayers': 6, 'location': 16, 'readOnly': True } ],
            [ LocationButton, { 'x': 854 - 147.5, 'y': 137 - self.buttonOffset2, 'maxPlayers': 6, 'location': 17, 'readOnly': True } ],
            [ LocationButton, { 'x': 854 - 147.5, 'y': 166 - self.buttonOffset2, 'maxPlayers': 6, 'location': 18, 'readOnly': True } ],
            [ LocationButton, { 'x': 833 - 147.5, 'y': 183 - self.buttonOffset2, 'maxPlayers': 6, 'location': 19, 'readOnly': True } ],
            [ LocationButton, { 'x': 812 - 147.5, 'y': 210 - self.buttonOffset2, 'maxPlayers': 6, 'location': 20, 'readOnly': True } ],
            [ LocationButton, { 'x': 791 - 147.5, 'y': 236 - self.buttonOffset2, 'maxPlayers': 6, 'location': 21, 'readOnly': True } ],
            [ LocationButton, { 'x': 765 - 147.5, 'y': 250 - self.buttonOffset2, 'maxPlayers': 6, 'location': 22, 'readOnly': True } ],
            
            # Right up
            [ LocationButton, { 'x': 735 + 142, 'y': 275 - self.buttonOffset2, 'maxPlayers': 6, 'location': 23, 'readOnly': True } ],
            [ LocationButton, { 'x': 705 + 142, 'y': 249 - self.buttonOffset2, 'maxPlayers': 6, 'location': 24, 'readOnly': True } ],
            [ LocationButton, { 'x': 676 + 142, 'y': 232 - self.buttonOffset2, 'maxPlayers': 6, 'location': 25, 'readOnly': True } ],
            [ LocationButton, { 'x': 655 + 142, 'y': 210 - self.buttonOffset2, 'maxPlayers': 6, 'location': 26, 'readOnly': True } ],
            [ LocationButton, { 'x': 632 + 142, 'y': 189 - self.buttonOffset2, 'maxPlayers': 6, 'location': 27, 'readOnly': True } ],
            [ LocationButton, { 'x': 612 + 142, 'y': 160 - self.buttonOffset2, 'maxPlayers': 6, 'location': 28, 'readOnly': True } ],
            [ LocationButton, { 'x': 612 + 142, 'y': 132 - self.buttonOffset2, 'maxPlayers': 6, 'location': 29, 'readOnly': True } ],
            [ LocationButton, { 'x': 625 + 142, 'y': 99 - self.buttonOffset2, 'maxPlayers': 6, 'location': 30, 'readOnly': True } ],
            [ LocationButton, { 'x': 655 + 142, 'y': 91 - self.buttonOffset2, 'maxPlayers': 6, 'location': 31, 'readOnly': True } ],
            [ LocationButton, { 'x': 688 + 142, 'y': 79 - self.buttonOffset2, 'maxPlayers': 6, 'location': 32, 'readOnly': True } ],
            [ LocationButton, { 'x': 715 + 142, 'y': 91 - self.buttonOffset2, 'maxPlayers': 6, 'location': 33, 'readOnly': True } ],
            [ LocationButton, { 'x': 733 + 142, 'y': 118 - self.buttonOffset2, 'maxPlayers': 6, 'location': 34, 'readOnly': True } ],
            [ LocationButton, { 'x': 750 + 142, 'y': 91 - self.buttonOffset2, 'maxPlayers': 6, 'location': 35, 'readOnly': True } ],
            [ LocationButton, { 'x': 780 + 142, 'y': 79 - self.buttonOffset2, 'maxPlayers': 6, 'location': 36, 'readOnly': True } ],
            [ LocationButton, { 'x': 810 + 142, 'y': 91 - self.buttonOffset2, 'maxPlayers': 6, 'location': 37, 'readOnly': True } ],
            [ LocationButton, { 'x': 838 + 142, 'y': 100 - self.buttonOffset2, 'maxPlayers': 6, 'location': 38, 'readOnly': True } ],
            [ LocationButton, { 'x': 852 + 142, 'y': 137 - self.buttonOffset2, 'maxPlayers': 6, 'location': 39, 'readOnly': True } ],
            [ LocationButton, { 'x': 852 + 142, 'y': 166 - self.buttonOffset2, 'maxPlayers': 6, 'location': 40, 'readOnly': True } ],
            [ LocationButton, { 'x': 830 + 142, 'y': 189 - self.buttonOffset2, 'maxPlayers': 6, 'location': 41, 'readOnly': True } ],
            [ LocationButton, { 'x': 810 + 142, 'y': 212 - self.buttonOffset2, 'maxPlayers': 6, 'location': 42, 'readOnly': True } ],
            [ LocationButton, { 'x': 791 + 142, 'y': 236 - self.buttonOffset2, 'maxPlayers': 6, 'location': 43, 'readOnly': True } ],
            [ LocationButton, { 'x': 765 + 142, 'y': 249 - self.buttonOffset2, 'maxPlayers': 6, 'location': 44, 'readOnly': True } ], 
            
            # Right
            [ LocationButton, { 'x': 779 + self.buttonOffset, 'y': 312 - self.buttonOffset2, 'maxPlayers': 6, 'location': 45, 'readOnly': True } ],
            [ LocationButton, { 'x': 800 + self.buttonOffset, 'y': 282 - self.buttonOffset2, 'maxPlayers': 6, 'location': 46, 'readOnly': True } ],
            [ LocationButton, { 'x': 816 + self.buttonOffset, 'y': 255 - self.buttonOffset2, 'maxPlayers': 6, 'location': 47, 'readOnly': True } ], 
            [ LocationButton, { 'x': 840 + self.buttonOffset, 'y': 235 - self.buttonOffset2, 'maxPlayers': 6, 'location': 48, 'readOnly': True } ],
            [ LocationButton, { 'x': 863 + self.buttonOffset, 'y': 215 - self.buttonOffset2, 'maxPlayers': 6, 'location': 49, 'readOnly': True } ], 
            [ LocationButton, { 'x': 888 + self.buttonOffset, 'y': 192 - self.buttonOffset2, 'maxPlayers': 6, 'location': 50, 'readOnly': True } ],
            [ LocationButton, { 'x': 918 + self.buttonOffset, 'y': 192 - self.buttonOffset2, 'maxPlayers': 6, 'location': 51, 'readOnly': True } ],
            [ LocationButton, { 'x': 948 + self.buttonOffset, 'y': 204 - self.buttonOffset2, 'maxPlayers': 6, 'location': 52, 'readOnly': True } ],
            [ LocationButton, { 'x': 960 + self.buttonOffset, 'y': 235 - self.buttonOffset2, 'maxPlayers': 6, 'location': 53, 'readOnly': True } ],
            [ LocationButton, { 'x': 973 + self.buttonOffset, 'y': 265 - self.buttonOffset2, 'maxPlayers': 6, 'location': 54, 'readOnly': True } ],
            [ LocationButton, { 'x': 957 + self.buttonOffset, 'y': 295 - self.buttonOffset2, 'maxPlayers': 6, 'location': 55, 'readOnly': True } ],
            [ LocationButton, { 'x': 930 + self.buttonOffset, 'y': 312 - self.buttonOffset2, 'maxPlayers': 6, 'location': 56, 'readOnly': True } ],
            [ LocationButton, { 'x': 957 + self.buttonOffset, 'y': 327 - self.buttonOffset2, 'maxPlayers': 6, 'location': 57, 'readOnly': True } ],
            [ LocationButton, { 'x': 970 + self.buttonOffset, 'y': 357 - self.buttonOffset2, 'maxPlayers': 6, 'location': 58, 'readOnly': True } ],
            [ LocationButton, { 'x': 960 + self.buttonOffset, 'y': 387 - self.buttonOffset2, 'maxPlayers': 6, 'location': 59, 'readOnly': True } ],
            [ LocationButton, { 'x': 945 + self.buttonOffset, 'y': 415 - self.buttonOffset2, 'maxPlayers': 6, 'location': 60, 'readOnly': True } ],
            [ LocationButton, { 'x': 915 + self.buttonOffset, 'y': 432 - self.buttonOffset2, 'maxPlayers': 6, 'location': 61, 'readOnly': True } ],
            [ LocationButton, { 'x': 885 + self.buttonOffset, 'y': 432 - self.buttonOffset2, 'maxPlayers': 6, 'location': 62, 'readOnly': True } ],
            [ LocationButton, { 'x': 863 + self.buttonOffset, 'y': 410 - self.buttonOffset2, 'maxPlayers': 6, 'location': 63, 'readOnly': True } ],
            [ LocationButton, { 'x': 840 + self.buttonOffset, 'y': 389 - self.buttonOffset2, 'maxPlayers': 6, 'location': 64, 'readOnly': True } ],
            [ LocationButton, { 'x': 816 + self.buttonOffset, 'y': 368 - self.buttonOffset2, 'maxPlayers': 6, 'location': 65, 'readOnly': True } ],
            [ LocationButton, { 'x': 800 + self.buttonOffset, 'y': 342 - self.buttonOffset2, 'maxPlayers': 6, 'location': 66, 'readOnly': True } ],
            
            # Right down
            [ LocationButton, { 'x': 736 + 142, 'y': 350 - self.buttonOffset2, 'maxPlayers': 6, 'location': 67, 'readOnly': True } ],
            [ LocationButton, { 'x': 706 + 142, 'y': 377 - self.buttonOffset2, 'maxPlayers': 6, 'location': 68, 'readOnly': True } ],
            [ LocationButton, { 'x': 681 + 142, 'y': 392 - self.buttonOffset2, 'maxPlayers': 6, 'location': 69, 'readOnly': True } ],
            [ LocationButton, { 'x': 657 + 145, 'y': 415 - self.buttonOffset2, 'maxPlayers': 6, 'location': 70, 'readOnly': True } ],
            [ LocationButton, { 'x': 637 + 145, 'y': 440 - self.buttonOffset2, 'maxPlayers': 6, 'location': 71, 'readOnly': True } ],
            [ LocationButton, { 'x': 617 + 142, 'y': 466 - self.buttonOffset2, 'maxPlayers': 6, 'location': 72, 'readOnly': True } ],
            [ LocationButton, { 'x': 617 + 142, 'y': 494 - self.buttonOffset2, 'maxPlayers': 6, 'location': 73, 'readOnly': True } ],
            [ LocationButton, { 'x': 633 + 142, 'y': 523 - self.buttonOffset2, 'maxPlayers': 6, 'location': 74, 'readOnly': True } ],
            [ LocationButton, { 'x': 658 + 145, 'y': 540 - self.buttonOffset2, 'maxPlayers': 6, 'location': 75, 'readOnly': True } ],
            [ LocationButton, { 'x': 688 + 145, 'y': 550 - self.buttonOffset2, 'maxPlayers': 6, 'location': 76, 'readOnly': True } ],
            [ LocationButton, { 'x': 717 + 145, 'y': 535 - self.buttonOffset2, 'maxPlayers': 6, 'location': 77, 'readOnly': True } ],
            [ LocationButton, { 'x': 736 + 145, 'y': 510 - self.buttonOffset2, 'maxPlayers': 6, 'location': 78, 'readOnly': True } ],
            [ LocationButton, { 'x': 754 + 145, 'y': 535 - self.buttonOffset2, 'maxPlayers': 6, 'location': 79, 'readOnly': True } ],
            [ LocationButton, { 'x': 780 + 145, 'y': 550 - self.buttonOffset2, 'maxPlayers': 6, 'location': 80, 'readOnly': True } ],
            [ LocationButton, { 'x': 811 + 145, 'y': 540 - self.buttonOffset2, 'maxPlayers': 6, 'location': 81, 'readOnly': True } ],
            [ LocationButton, { 'x': 840 + 145, 'y': 525 - self.buttonOffset2, 'maxPlayers': 6, 'location': 82, 'readOnly': True } ],
            [ LocationButton, { 'x': 854 + 145, 'y': 494 - self.buttonOffset2, 'maxPlayers': 6, 'location': 83, 'readOnly': True } ],
            [ LocationButton, { 'x': 854 + 145, 'y': 466 - self.buttonOffset2, 'maxPlayers': 6, 'location': 84, 'readOnly': True } ],
            [ LocationButton, { 'x': 832 + 145, 'y': 440 - self.buttonOffset2, 'maxPlayers': 6, 'location': 85, 'readOnly': True } ],
            [ LocationButton, { 'x': 812 + 145, 'y': 415 - self.buttonOffset2, 'maxPlayers': 6, 'location': 86, 'readOnly': True } ],
            [ LocationButton, { 'x': 791 + 145, 'y': 392 - self.buttonOffset2, 'maxPlayers': 6, 'location': 87, 'readOnly': True } ],
            [ LocationButton, { 'x': 765 + 145, 'y': 377 - self.buttonOffset2, 'maxPlayers': 6, 'location': 88, 'readOnly': True } ],
            
            # Left down
            [ LocationButton, { 'x': 736 - 145, 'y': 352 - self.buttonOffset2, 'maxPlayers': 6, 'location': 89, 'readOnly': True } ],
            [ LocationButton, { 'x': 705 - 145, 'y': 378 - self.buttonOffset2, 'maxPlayers': 6, 'location': 90, 'readOnly': True } ],
            [ LocationButton, { 'x': 678 - 145, 'y': 390 - self.buttonOffset2, 'maxPlayers': 6, 'location': 91, 'readOnly': True } ],
            [ LocationButton, { 'x': 656 - 145, 'y': 416 - self.buttonOffset2, 'maxPlayers': 6, 'location': 92, 'readOnly': True } ],
            [ LocationButton, { 'x': 637 - 145, 'y': 440 - self.buttonOffset2, 'maxPlayers': 6, 'location': 93, 'readOnly': True } ],
            [ LocationButton, { 'x': 617 - 145, 'y': 466 - self.buttonOffset2, 'maxPlayers': 6, 'location': 94, 'readOnly': True } ],
            [ LocationButton, { 'x': 617 - 145, 'y': 494 - self.buttonOffset2, 'maxPlayers': 6, 'location': 95, 'readOnly': True } ],
            [ LocationButton, { 'x': 628 - 145, 'y': 525 - self.buttonOffset2, 'maxPlayers': 6, 'location': 96, 'readOnly': True } ],
            [ LocationButton, { 'x': 658 - 145, 'y': 540 - self.buttonOffset2, 'maxPlayers': 6, 'location': 97, 'readOnly': True } ],
            [ LocationButton, { 'x': 688 - 145, 'y': 550 - self.buttonOffset2, 'maxPlayers': 6, 'location': 98, 'readOnly': True } ],
            [ LocationButton, { 'x': 720 - 145, 'y': 535 - self.buttonOffset2, 'maxPlayers': 6, 'location': 99, 'readOnly': True } ],
            [ LocationButton, { 'x': 738 - 145, 'y': 510 - self.buttonOffset2, 'maxPlayers': 6, 'location': 100, 'readOnly': True } ],
            [ LocationButton, { 'x': 755 - 145, 'y': 535 - self.buttonOffset2, 'maxPlayers': 6, 'location': 101, 'readOnly': True } ],
            [ LocationButton, { 'x': 785 - 145, 'y': 550 - self.buttonOffset2, 'maxPlayers': 6, 'location': 102, 'readOnly': True } ],
            [ LocationButton, { 'x': 814 - 145, 'y': 540 - self.buttonOffset2, 'maxPlayers': 6, 'location': 103, 'readOnly': True } ],
            [ LocationButton, { 'x': 849 - 145, 'y': 528 - self.buttonOffset2, 'maxPlayers': 6, 'location': 104, 'readOnly': True } ],
            [ LocationButton, { 'x': 859 - 145, 'y': 494 - self.buttonOffset2, 'maxPlayers': 6, 'location': 105, 'readOnly': True } ],
            [ LocationButton, { 'x': 859 - 145, 'y': 466 - self.buttonOffset2, 'maxPlayers': 6, 'location': 106, 'readOnly': True } ],
            [ LocationButton, { 'x': 837 - 145, 'y': 438 - self.buttonOffset2, 'maxPlayers': 6, 'location': 107, 'readOnly': True } ],
            [ LocationButton, { 'x': 821 - 145, 'y': 418 - self.buttonOffset2, 'maxPlayers': 6, 'location': 108, 'readOnly': True } ],
            [ LocationButton, { 'x': 795 - 145, 'y': 390 - self.buttonOffset2, 'maxPlayers': 6, 'location': 109, 'readOnly': True } ],
            [ LocationButton, { 'x': 765 - 145, 'y': 378 - self.buttonOffset2, 'maxPlayers': 6, 'location': 110, 'readOnly': True } ],
            
            # Left 
            [ LocationButton, { 'x': 692 - self.buttonOffset, 'y': 317 - self.buttonOffset2, 'maxPlayers': 6, 'location': 111, 'readOnly': True } ],
            [ LocationButton, { 'x': 669 - self.buttonOffset, 'y': 347 - self.buttonOffset2, 'maxPlayers': 6, 'location': 112, 'readOnly': True } ],
            [ LocationButton, { 'x': 652 - self.buttonOffset, 'y': 375 - self.buttonOffset2, 'maxPlayers': 6, 'location': 113, 'readOnly': True } ],
            [ LocationButton, { 'x': 630 - self.buttonOffset, 'y': 396 - self.buttonOffset2, 'maxPlayers': 6, 'location': 114, 'readOnly': True } ],
            [ LocationButton, { 'x': 606 - self.buttonOffset, 'y': 416 - self.buttonOffset2, 'maxPlayers': 6, 'location': 115, 'readOnly': True } ],
            [ LocationButton, { 'x': 583 - self.buttonOffset, 'y': 437 - self.buttonOffset2, 'maxPlayers': 6, 'location': 116, 'readOnly': True } ],
            [ LocationButton, { 'x': 553 - self.buttonOffset, 'y': 437 - self.buttonOffset2, 'maxPlayers': 6, 'location': 117, 'readOnly': True } ],
            [ LocationButton, { 'x': 525 - self.buttonOffset, 'y': 423 - self.buttonOffset2, 'maxPlayers': 6, 'location': 118, 'readOnly': True } ],
            [ LocationButton, { 'x': 510 - self.buttonOffset, 'y': 393 - self.buttonOffset2, 'maxPlayers': 6, 'location': 119, 'readOnly': True } ],
            [ LocationButton, { 'x': 497 - self.buttonOffset, 'y': 363 - self.buttonOffset2, 'maxPlayers': 6, 'location': 120, 'readOnly': True } ],
            [ LocationButton, { 'x': 512 - self.buttonOffset, 'y': 333 - self.buttonOffset2, 'maxPlayers': 6, 'location': 121, 'readOnly': True } ],
            [ LocationButton, { 'x': 542 - self.buttonOffset, 'y': 318 - self.buttonOffset2, 'maxPlayers': 6, 'location': 122, 'readOnly': True } ],
            [ LocationButton, { 'x': 512 - self.buttonOffset, 'y': 300 - self.buttonOffset2, 'maxPlayers': 6, 'location': 123, 'readOnly': True } ],
            [ LocationButton, { 'x': 500 - self.buttonOffset, 'y': 270 - self.buttonOffset2, 'maxPlayers': 6, 'location': 124, 'readOnly': True } ],
            [ LocationButton, { 'x': 512 - self.buttonOffset, 'y': 240 - self.buttonOffset2, 'maxPlayers': 6, 'location': 125, 'readOnly': True } ],
            [ LocationButton, { 'x': 525 - self.buttonOffset, 'y': 208 - self.buttonOffset2, 'maxPlayers': 6, 'location': 126, 'readOnly': True } ],
            [ LocationButton, { 'x': 553 - self.buttonOffset, 'y': 196 - self.buttonOffset2, 'maxPlayers': 6, 'location': 127, 'readOnly': True } ],
            [ LocationButton, { 'x': 583 - self.buttonOffset, 'y': 196 - self.buttonOffset2, 'maxPlayers': 6, 'location': 128, 'readOnly': True } ],
            [ LocationButton, { 'x': 606 - self.buttonOffset, 'y': 217 - self.buttonOffset2, 'maxPlayers': 6, 'location': 129, 'readOnly': True } ],
            [ LocationButton, { 'x': 630 - self.buttonOffset, 'y': 237 - self.buttonOffset2, 'maxPlayers': 6, 'location': 130, 'readOnly': True } ],
            [ LocationButton, { 'x': 655 - self.buttonOffset, 'y': 258 - self.buttonOffset2, 'maxPlayers': 6, 'location': 131, 'readOnly': True } ],
            [ LocationButton, { 'x': 670 - self.buttonOffset, 'y': 287 - self.buttonOffset2, 'maxPlayers': 6, 'location': 132, 'readOnly': True } ],
        ]
        
        playerButtonX = 20
        playerButtonY = 250
        
        players = playerManager.getAllPlayers()
        for i in range(1, len(players) + 1):
            modules.append([ PlayerButton, {
                'x': playerButtonX,
                'y': playerButtonY,
                'player': players[i - 1],
                'reverseAlignment': i % 2 != 0,
                'readOnly': True
            } ])
            
            playerButtonX += 140 + 20
            
            if i % 2 == 0:
                playerButtonX = 20
                playerButtonY += 100 + ui.SPACING_XS
            
        return modules
