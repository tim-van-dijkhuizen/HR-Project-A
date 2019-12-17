import ui
from screen import Screen
from button import Button
from dice_manager import DiceManager
from location_button  import LocationButton
from player_button import PlayerButton
from turn_manager import TurnManager

class GameScreen(Screen):

    # Button offset
    buttonOffset = 145
    buttonOffset2 = 35
    
    boardWidth = 794
    boardHeight = 500

    boardImageFour = None
    boardImageSix = None
    

    pionRoodR = None
    pionRoodL = None
    pionBlauwL = None
    pionBlauwR = None
    pionGroenL = None
    pionGroenR = None
    
    fromScreen = None
    player = None

    def setup(self):
        playerManager = self.app.getModule('playerManager')
        locationButton = self.app.getModule('location')
        turnManager = self.app.getModule('turnManager')

        self.boardImageFour = loadImage('board-players4.png')
        self.boardImageSix = loadImage('board-players6.png')
        
        self.pionRoodL = loadImage('RoodL.png')
        self.pionRoodR = loadImage('RoodR.png')
        self.pionBlauwL = loadImage('BlauwL.png')
        self.pionBlauwR = loadImage('BlauwR.png')
        self.pionGroenL = loadImage('GroenL.png')
        self.pionGroenR = loadImage('GroenR.png')
        
        self.boardX = width / 2 - (self.boardWidth / 3.2)
        self.boardY = 40

    def getHandle(self):
        return 'game'

    def draw(self):
        playerManager = self.app.getModule('playerManager')
        locationButton = self.app.getModule('location')
        turnManager = self.app.getModule('turnManager')
        
        print

        background(ui.COLOR_RED_LIGHT)

        fill(ui.COLOR_TEXT)
        textSize(30);
        textAlign(LEFT);
        text('Huidige beurt:', 60, 60)
            
        image(self.pionRoodR, 50, 150, 40, 50)
        image(self.pionRoodL, 50, 210, 40, 50)
        image(self.pionBlauwL, 100, 150, 40, 50)
        image(self.pionBlauwR, 100, 210, 40, 50)
        image(self.pionGroenL, 150, 150, 40, 50)
        image(self.pionGroenR, 150, 210, 40, 50)
            
        
        boardImage = self.boardImageSix if playerManager.maxPlayers == 6 else self.boardImageFour
        image(boardImage, self.boardX, self.boardY, self.boardWidth, self.boardHeight)

    def keyPressed(self):
        if keyCode == 32:
            startScreen = self.app.getScreen('start')
            self.app.setCurrentScreen(startScreen)

    def rollDice(self):
        diceManager = self.app.getModule('diceManager')
        diceManager.rollDice()

    def getSubModules(self):
        playerManager = self.app.getModule('playerManager')
        modules = [            
            [ DiceManager, {  } ],
            [ TurnManager, {  } ],
        
            [ LocationButton, { 'x': 735, 'y': 275 - self.buttonOffset2, 'maxPlayers': 4, 'location': 1 } ],
            [ LocationButton, { 'x': 705, 'y': 250 - self.buttonOffset2, 'maxPlayers': 4, 'location': 2 } ],
            [ LocationButton, { 'x': 678, 'y': 236 - self.buttonOffset2, 'maxPlayers': 4, 'location': 3 } ],
            [ LocationButton, { 'x': 657, 'y': 210 - self.buttonOffset2, 'maxPlayers': 4, 'location': 4 } ],
            [ LocationButton, { 'x': 635, 'y': 189 - self.buttonOffset2, 'maxPlayers': 4, 'location': 5 } ],
            [ LocationButton, { 'x': 615, 'y': 166 - self.buttonOffset2, 'maxPlayers': 4, 'location': 6 } ],
            [ LocationButton, { 'x': 615, 'y': 134 - self.buttonOffset2, 'maxPlayers': 4, 'location': 7 } ],
            [ LocationButton, { 'x': 628, 'y': 105 - self.buttonOffset2, 'maxPlayers': 4, 'location': 8 } ],
            [ LocationButton, { 'x': 658, 'y': 93 - self.buttonOffset2, 'maxPlayers': 4, 'location': 9 } ],
            [ LocationButton, { 'x': 688, 'y': 82 - self.buttonOffset2, 'maxPlayers': 4, 'location': 10 } ],
            [ LocationButton, { 'x': 715, 'y': 93 - self.buttonOffset2, 'maxPlayers': 4, 'location': 11 } ],
            [ LocationButton, { 'x': 735, 'y': 120 - self.buttonOffset2, 'maxPlayers': 4, 'location': 12 } ],
            [ LocationButton, { 'x': 750, 'y': 93 - self.buttonOffset2, 'maxPlayers': 4, 'location': 13 } ],
            [ LocationButton, { 'x': 780, 'y': 82 - self.buttonOffset2, 'maxPlayers': 4, 'location': 14 } ],
            [ LocationButton, { 'x': 810, 'y': 93 - self.buttonOffset2, 'maxPlayers': 4, 'location': 15 } ],
            [ LocationButton, { 'x': 838, 'y': 108 - self.buttonOffset2, 'maxPlayers': 4, 'location': 16 } ],
            [ LocationButton, { 'x': 852, 'y': 137 - self.buttonOffset2, 'maxPlayers': 4, 'location': 17 } ],
            [ LocationButton, { 'x': 852, 'y': 166 - self.buttonOffset2, 'maxPlayers': 4, 'location': 18 } ],
            [ LocationButton, { 'x': 830, 'y': 189 - self.buttonOffset2, 'maxPlayers': 4, 'location': 19 } ],
            [ LocationButton, { 'x': 810, 'y': 212 - self.buttonOffset2, 'maxPlayers': 4, 'location': 20 } ],
            [ LocationButton, { 'x': 791, 'y': 236 - self.buttonOffset2, 'maxPlayers': 4, 'location': 21 } ],
            [ LocationButton, { 'x': 765, 'y': 250 - self.buttonOffset2, 'maxPlayers': 4, 'location': 22 } ],
            
            [ LocationButton, { 'x': 779, 'y': 312 - self.buttonOffset2, 'maxPlayers': 4, 'location': 23 } ],
            [ LocationButton, { 'x': 803, 'y': 282 - self.buttonOffset2, 'maxPlayers': 4, 'location': 24 } ],
            [ LocationButton, { 'x': 818, 'y': 255 - self.buttonOffset2, 'maxPlayers': 4, 'location': 25 } ], 
            [ LocationButton, { 'x': 840, 'y': 235 - self.buttonOffset2, 'maxPlayers': 4, 'location': 26 } ],
            [ LocationButton, { 'x': 863, 'y': 213 - self.buttonOffset2, 'maxPlayers': 4, 'location': 27 } ], 
            [ LocationButton, { 'x': 888, 'y': 192 - self.buttonOffset2, 'maxPlayers': 4, 'location': 28 } ],
            [ LocationButton, { 'x': 918, 'y': 192 - self.buttonOffset2, 'maxPlayers': 4, 'location': 29 } ],
            [ LocationButton, { 'x': 948, 'y': 204 - self.buttonOffset2, 'maxPlayers': 4, 'location': 30 } ],
            [ LocationButton, { 'x': 960, 'y': 235 - self.buttonOffset2, 'maxPlayers': 4, 'location': 31 } ],
            [ LocationButton, { 'x': 970, 'y': 265 - self.buttonOffset2, 'maxPlayers': 4, 'location': 32 } ],
            [ LocationButton, { 'x': 957, 'y': 295 - self.buttonOffset2, 'maxPlayers': 4, 'location': 33 } ],
            [ LocationButton, { 'x': 930, 'y': 310 - self.buttonOffset2, 'maxPlayers': 4, 'location': 34 } ],
            [ LocationButton, { 'x': 957, 'y': 328 - self.buttonOffset2, 'maxPlayers': 4, 'location': 35 } ],
            [ LocationButton, { 'x': 970, 'y': 357 - self.buttonOffset2, 'maxPlayers': 4, 'location': 36 } ],
            [ LocationButton, { 'x': 960, 'y': 387 - self.buttonOffset2, 'maxPlayers': 4, 'location': 37 } ],
            [ LocationButton, { 'x': 945, 'y': 415 - self.buttonOffset2, 'maxPlayers': 4, 'location': 38 } ],
            [ LocationButton, { 'x': 915, 'y': 432 - self.buttonOffset2, 'maxPlayers': 4, 'location': 39 } ],
            [ LocationButton, { 'x': 885, 'y': 432 - self.buttonOffset2, 'maxPlayers': 4, 'location': 40 } ],
            [ LocationButton, { 'x': 863, 'y': 410 - self.buttonOffset2, 'maxPlayers': 4, 'location': 41 } ],
            [ LocationButton, { 'x': 840, 'y': 389 - self.buttonOffset2, 'maxPlayers': 4, 'location': 42 } ],
            [ LocationButton, { 'x': 818, 'y': 368 - self.buttonOffset2, 'maxPlayers': 4, 'location': 43 } ],
            [ LocationButton, { 'x': 802, 'y': 342 - self.buttonOffset2, 'maxPlayers': 4, 'location': 44 } ],
            
            [ LocationButton, { 'x': 735, 'y': 353 - self.buttonOffset2, 'maxPlayers': 4, 'location': 45 } ],
            [ LocationButton, { 'x': 765, 'y': 378 - self.buttonOffset2, 'maxPlayers': 4, 'location': 46 } ],
            [ LocationButton, { 'x': 791, 'y': 393 - self.buttonOffset2, 'maxPlayers': 4, 'location': 47 } ],
            [ LocationButton, { 'x': 812, 'y': 415 - self.buttonOffset2, 'maxPlayers': 4, 'location': 48 } ],
            [ LocationButton, { 'x': 832, 'y': 438 - self.buttonOffset2, 'maxPlayers': 4, 'location': 49 } ],
            [ LocationButton, { 'x': 852, 'y': 466 - self.buttonOffset2, 'maxPlayers': 4, 'location': 50 } ],
            [ LocationButton, { 'x': 852, 'y': 496 - self.buttonOffset2, 'maxPlayers': 4, 'location': 51 } ],
            [ LocationButton, { 'x': 840, 'y': 524 - self.buttonOffset2, 'maxPlayers': 4, 'location': 52 } ],
            [ LocationButton, { 'x': 810, 'y': 538 - self.buttonOffset2, 'maxPlayers': 4, 'location': 53 } ],
            [ LocationButton, { 'x': 780, 'y': 548 - self.buttonOffset2, 'maxPlayers': 4, 'location': 54 } ],
            [ LocationButton, { 'x': 753, 'y': 536 - self.buttonOffset2, 'maxPlayers': 4, 'location': 55 } ],
            [ LocationButton, { 'x': 735, 'y': 510 - self.buttonOffset2, 'maxPlayers': 4, 'location': 56 } ],
            [ LocationButton, { 'x': 719, 'y': 536 - self.buttonOffset2, 'maxPlayers': 4, 'location': 57 } ],
            [ LocationButton, { 'x': 688, 'y': 548 - self.buttonOffset2, 'maxPlayers': 4, 'location': 58 } ],
            [ LocationButton, { 'x': 660, 'y': 534 - self.buttonOffset2, 'maxPlayers': 4, 'location': 59 } ],
            [ LocationButton, { 'x': 630, 'y': 521 - self.buttonOffset2, 'maxPlayers': 4, 'location': 60 } ],
            [ LocationButton, { 'x': 616, 'y': 494 - self.buttonOffset2, 'maxPlayers': 4, 'location': 61 } ],
            [ LocationButton, { 'x': 616, 'y': 462 - self.buttonOffset2, 'maxPlayers': 4, 'location': 62 } ],
            [ LocationButton, { 'x': 638, 'y': 440 - self.buttonOffset2, 'maxPlayers': 4, 'location': 63 } ],
            [ LocationButton, { 'x': 657, 'y': 415 - self.buttonOffset2, 'maxPlayers': 4, 'location': 64 } ],
            [ LocationButton, { 'x': 678, 'y': 393 - self.buttonOffset2, 'maxPlayers': 4, 'location': 65 } ],
            [ LocationButton, { 'x': 705, 'y': 378 - self.buttonOffset2, 'maxPlayers': 4, 'location': 66 } ],
            
            [ LocationButton, { 'x': 692, 'y': 312 - self.buttonOffset2, 'maxPlayers': 4, 'location': 67 } ],
            [ LocationButton, { 'x': 669, 'y': 342 - self.buttonOffset2, 'maxPlayers': 4, 'location': 68 } ],
            [ LocationButton, { 'x': 655, 'y': 368 - self.buttonOffset2, 'maxPlayers': 4, 'location': 69 } ],
            [ LocationButton, { 'x': 630, 'y': 389 - self.buttonOffset2, 'maxPlayers': 4, 'location': 70 } ],
            [ LocationButton, { 'x': 606, 'y': 410 - self.buttonOffset2, 'maxPlayers': 4, 'location': 71 } ],
            [ LocationButton, { 'x': 583, 'y': 432 - self.buttonOffset2, 'maxPlayers': 4, 'location': 72 } ],
            [ LocationButton, { 'x': 553, 'y': 432 - self.buttonOffset2, 'maxPlayers': 4, 'location': 73 } ],
            [ LocationButton, { 'x': 525, 'y': 420 - self.buttonOffset2, 'maxPlayers': 4, 'location': 74 } ],
            [ LocationButton, { 'x': 510, 'y': 390 - self.buttonOffset2, 'maxPlayers': 4, 'location': 75 } ],
            [ LocationButton, { 'x': 497, 'y': 360 - self.buttonOffset2, 'maxPlayers': 4, 'location': 76 } ],
            [ LocationButton, { 'x': 512, 'y': 330 - self.buttonOffset2, 'maxPlayers': 4, 'location': 77 } ],
            [ LocationButton, { 'x': 542, 'y': 314 - self.buttonOffset2, 'maxPlayers': 4, 'location': 78 } ],
            [ LocationButton, { 'x': 512, 'y': 298 - self.buttonOffset2, 'maxPlayers': 4, 'location': 79 } ],
            [ LocationButton, { 'x': 500, 'y': 267 - self.buttonOffset2, 'maxPlayers': 4, 'location': 80 } ],
            [ LocationButton, { 'x': 512, 'y': 238 - self.buttonOffset2, 'maxPlayers': 4, 'location': 81 } ],
            [ LocationButton, { 'x': 525, 'y': 208 - self.buttonOffset2, 'maxPlayers': 4, 'location': 82 } ],
            [ LocationButton, { 'x': 553, 'y': 195 - self.buttonOffset2, 'maxPlayers': 4, 'location': 83 } ],
            [ LocationButton, { 'x': 583, 'y': 195 - self.buttonOffset2, 'maxPlayers': 4, 'location': 84 } ],
            [ LocationButton, { 'x': 606, 'y': 215 - self.buttonOffset2, 'maxPlayers': 4, 'location': 85 } ],
            [ LocationButton, { 'x': 630, 'y': 235 - self.buttonOffset2, 'maxPlayers': 4, 'location': 86 } ],
            [ LocationButton, { 'x': 655, 'y': 256 - self.buttonOffset2, 'maxPlayers': 4, 'location': 87 } ],
            [ LocationButton, { 'x': 669, 'y': 282 - self.buttonOffset2, 'maxPlayers': 4, 'location': 88 } ],
            
            # Left up
            [ LocationButton, { 'x': 735 - 147.5, 'y': 275 - self.buttonOffset2, 'maxPlayers': 6, 'location': 1 } ],
            [ LocationButton, { 'x': 705 - 147.5, 'y': 250 - self.buttonOffset2, 'maxPlayers': 6, 'location': 2 } ],
            [ LocationButton, { 'x': 678 - 147.5, 'y': 236 - self.buttonOffset2, 'maxPlayers': 6, 'location': 3 } ],
            [ LocationButton, { 'x': 655 - 147.5, 'y': 210 - self.buttonOffset2, 'maxPlayers': 6, 'location': 4 } ],
            [ LocationButton, { 'x': 635 - 147.5, 'y': 189 - self.buttonOffset2, 'maxPlayers': 6, 'location': 5 } ],
            [ LocationButton, { 'x': 615 - 147.5, 'y': 163 - self.buttonOffset2, 'maxPlayers': 6, 'location': 6 } ],
            [ LocationButton, { 'x': 615 - 147.5, 'y': 131 - self.buttonOffset2, 'maxPlayers': 6, 'location': 7 } ],
            [ LocationButton, { 'x': 628 - 147.5, 'y': 105 - self.buttonOffset2, 'maxPlayers': 6, 'location': 8 } ],
            [ LocationButton, { 'x': 658 - 147.5, 'y': 90 - self.buttonOffset2, 'maxPlayers': 6, 'location': 9 } ],
            [ LocationButton, { 'x': 688 - 147.5, 'y': 79 - self.buttonOffset2, 'maxPlayers': 6, 'location': 10 } ],
            [ LocationButton, { 'x': 716 - 147.5, 'y': 90 - self.buttonOffset2, 'maxPlayers': 6, 'location': 11 } ],
            [ LocationButton, { 'x': 735 - 147.5, 'y': 120 - self.buttonOffset2, 'maxPlayers': 6, 'location': 12 } ],
            [ LocationButton, { 'x': 750 - 147.5, 'y': 90 - self.buttonOffset2, 'maxPlayers': 6, 'location': 13 } ],
            [ LocationButton, { 'x': 780 - 147.5, 'y': 79 - self.buttonOffset2, 'maxPlayers': 6, 'location': 14 } ],
            [ LocationButton, { 'x': 812 - 147.5, 'y': 90 - self.buttonOffset2, 'maxPlayers': 6, 'location': 15 } ],
            [ LocationButton, { 'x': 840 - 147.5, 'y': 106 - self.buttonOffset2, 'maxPlayers': 6, 'location': 16 } ],
            [ LocationButton, { 'x': 854 - 147.5, 'y': 137 - self.buttonOffset2, 'maxPlayers': 6, 'location': 17 } ],
            [ LocationButton, { 'x': 854 - 147.5, 'y': 166 - self.buttonOffset2, 'maxPlayers': 6, 'location': 18 } ],
            [ LocationButton, { 'x': 833 - 147.5, 'y': 183 - self.buttonOffset2, 'maxPlayers': 6, 'location': 19 } ],
            [ LocationButton, { 'x': 812 - 147.5, 'y': 210 - self.buttonOffset2, 'maxPlayers': 6, 'location': 20 } ],
            [ LocationButton, { 'x': 791 - 147.5, 'y': 236 - self.buttonOffset2, 'maxPlayers': 6, 'location': 21 } ],
            [ LocationButton, { 'x': 765 - 147.5, 'y': 250 - self.buttonOffset2, 'maxPlayers': 6, 'location': 22 } ],
            
            # Right up
            [ LocationButton, { 'x': 735 + 142, 'y': 275 - self.buttonOffset2, 'maxPlayers': 6, 'location': 23 } ],
            [ LocationButton, { 'x': 705 + 142, 'y': 249 - self.buttonOffset2, 'maxPlayers': 6, 'location': 24 } ],
            [ LocationButton, { 'x': 676 + 142, 'y': 232 - self.buttonOffset2, 'maxPlayers': 6, 'location': 25 } ],
            [ LocationButton, { 'x': 655 + 142, 'y': 210 - self.buttonOffset2, 'maxPlayers': 6, 'location': 26 } ],
            [ LocationButton, { 'x': 632 + 142, 'y': 189 - self.buttonOffset2, 'maxPlayers': 6, 'location': 27 } ],
            [ LocationButton, { 'x': 612 + 142, 'y': 160 - self.buttonOffset2, 'maxPlayers': 6, 'location': 28 } ],
            [ LocationButton, { 'x': 612 + 142, 'y': 132 - self.buttonOffset2, 'maxPlayers': 6, 'location': 29 } ],
            [ LocationButton, { 'x': 625 + 142, 'y': 99 - self.buttonOffset2, 'maxPlayers': 6, 'location': 30 } ],
            [ LocationButton, { 'x': 655 + 142, 'y': 91 - self.buttonOffset2, 'maxPlayers': 6, 'location': 31 } ],
            [ LocationButton, { 'x': 688 + 142, 'y': 79 - self.buttonOffset2, 'maxPlayers': 6, 'location': 32 } ],
            [ LocationButton, { 'x': 715 + 142, 'y': 91 - self.buttonOffset2, 'maxPlayers': 6, 'location': 33 } ],
            [ LocationButton, { 'x': 733 + 142, 'y': 118 - self.buttonOffset2, 'maxPlayers': 6, 'location': 34 } ],
            [ LocationButton, { 'x': 750 + 142, 'y': 91 - self.buttonOffset2, 'maxPlayers': 6, 'location': 35 } ],
            [ LocationButton, { 'x': 780 + 142, 'y': 79 - self.buttonOffset2, 'maxPlayers': 6, 'location': 36 } ],
            [ LocationButton, { 'x': 810 + 142, 'y': 91 - self.buttonOffset2, 'maxPlayers': 6, 'location': 37 } ],
            [ LocationButton, { 'x': 838 + 142, 'y': 100 - self.buttonOffset2, 'maxPlayers': 6, 'location': 38 } ],
            [ LocationButton, { 'x': 852 + 142, 'y': 137 - self.buttonOffset2, 'maxPlayers': 6, 'location': 39 } ],
            [ LocationButton, { 'x': 852 + 142, 'y': 166 - self.buttonOffset2, 'maxPlayers': 6, 'location': 40 } ],
            [ LocationButton, { 'x': 830 + 142, 'y': 189 - self.buttonOffset2, 'maxPlayers': 6, 'location': 41 } ],
            [ LocationButton, { 'x': 810 + 142, 'y': 212 - self.buttonOffset2, 'maxPlayers': 6, 'location': 42 } ],
            [ LocationButton, { 'x': 791 + 142, 'y': 236 - self.buttonOffset2, 'maxPlayers': 6, 'location': 43 } ],
            [ LocationButton, { 'x': 765 + 142, 'y': 249 - self.buttonOffset2, 'maxPlayers': 6, 'location': 44 } ], 
            
            # Right
            [ LocationButton, { 'x': 779 + self.buttonOffset, 'y': 312 - self.buttonOffset2, 'maxPlayers': 6, 'location': 45 } ],
            [ LocationButton, { 'x': 800 + self.buttonOffset, 'y': 282 - self.buttonOffset2, 'maxPlayers': 6, 'location': 46 } ],
            [ LocationButton, { 'x': 816 + self.buttonOffset, 'y': 255 - self.buttonOffset2, 'maxPlayers': 6, 'location': 47 } ], 
            [ LocationButton, { 'x': 840 + self.buttonOffset, 'y': 235 - self.buttonOffset2, 'maxPlayers': 6, 'location': 48 } ],
            [ LocationButton, { 'x': 863 + self.buttonOffset, 'y': 215 - self.buttonOffset2, 'maxPlayers': 6, 'location': 49 } ], 
            [ LocationButton, { 'x': 888 + self.buttonOffset, 'y': 192 - self.buttonOffset2, 'maxPlayers': 6, 'location': 50 } ],
            [ LocationButton, { 'x': 918 + self.buttonOffset, 'y': 192 - self.buttonOffset2, 'maxPlayers': 6, 'location': 51 } ],
            [ LocationButton, { 'x': 948 + self.buttonOffset, 'y': 204 - self.buttonOffset2, 'maxPlayers': 6, 'location': 52 } ],
            [ LocationButton, { 'x': 960 + self.buttonOffset, 'y': 235 - self.buttonOffset2, 'maxPlayers': 6, 'location': 53 } ],
            [ LocationButton, { 'x': 973 + self.buttonOffset, 'y': 265 - self.buttonOffset2, 'maxPlayers': 6, 'location': 54 } ],
            [ LocationButton, { 'x': 957 + self.buttonOffset, 'y': 295 - self.buttonOffset2, 'maxPlayers': 6, 'location': 55 } ],
            [ LocationButton, { 'x': 930 + self.buttonOffset, 'y': 312 - self.buttonOffset2, 'maxPlayers': 6, 'location': 56 } ],
            [ LocationButton, { 'x': 957 + self.buttonOffset, 'y': 327 - self.buttonOffset2, 'maxPlayers': 6, 'location': 57 } ],
            [ LocationButton, { 'x': 970 + self.buttonOffset, 'y': 357 - self.buttonOffset2, 'maxPlayers': 6, 'location': 58 } ],
            [ LocationButton, { 'x': 960 + self.buttonOffset, 'y': 387 - self.buttonOffset2, 'maxPlayers': 6, 'location': 59 } ],
            [ LocationButton, { 'x': 945 + self.buttonOffset, 'y': 415 - self.buttonOffset2, 'maxPlayers': 6, 'location': 60 } ],
            [ LocationButton, { 'x': 915 + self.buttonOffset, 'y': 432 - self.buttonOffset2, 'maxPlayers': 6, 'location': 61 } ],
            [ LocationButton, { 'x': 885 + self.buttonOffset, 'y': 432 - self.buttonOffset2, 'maxPlayers': 6, 'location': 62 } ],
            [ LocationButton, { 'x': 863 + self.buttonOffset, 'y': 410 - self.buttonOffset2, 'maxPlayers': 6, 'location': 63 } ],
            [ LocationButton, { 'x': 840 + self.buttonOffset, 'y': 389 - self.buttonOffset2, 'maxPlayers': 6, 'location': 64 } ],
            [ LocationButton, { 'x': 816 + self.buttonOffset, 'y': 368 - self.buttonOffset2, 'maxPlayers': 6, 'location': 65 } ],
            [ LocationButton, { 'x': 800 + self.buttonOffset, 'y': 342 - self.buttonOffset2, 'maxPlayers': 6, 'location': 66 } ],
            
            # Right down
            [ LocationButton, { 'x': 736 + 142, 'y': 350 - self.buttonOffset2, 'maxPlayers': 6, 'location': 67 } ],
            [ LocationButton, { 'x': 706 + 142, 'y': 377 - self.buttonOffset2, 'maxPlayers': 6, 'location': 68 } ],
            [ LocationButton, { 'x': 681 + 142, 'y': 392 - self.buttonOffset2, 'maxPlayers': 6, 'location': 69 } ],
            [ LocationButton, { 'x': 657 + 145, 'y': 415 - self.buttonOffset2, 'maxPlayers': 6, 'location': 70 } ],
            [ LocationButton, { 'x': 637 + 145, 'y': 440 - self.buttonOffset2, 'maxPlayers': 6, 'location': 71 } ],
            [ LocationButton, { 'x': 617 + 142, 'y': 466 - self.buttonOffset2, 'maxPlayers': 6, 'location': 72 } ],
            [ LocationButton, { 'x': 617 + 142, 'y': 494 - self.buttonOffset2, 'maxPlayers': 6, 'location': 73 } ],
            [ LocationButton, { 'x': 633 + 142, 'y': 523 - self.buttonOffset2, 'maxPlayers': 6, 'location': 74 } ],
            [ LocationButton, { 'x': 658 + 145, 'y': 540 - self.buttonOffset2, 'maxPlayers': 6, 'location': 75 } ],
            [ LocationButton, { 'x': 688 + 145, 'y': 550 - self.buttonOffset2, 'maxPlayers': 6, 'location': 76 } ],
            [ LocationButton, { 'x': 717 + 145, 'y': 535 - self.buttonOffset2, 'maxPlayers': 6, 'location': 77 } ],
            [ LocationButton, { 'x': 736 + 145, 'y': 510 - self.buttonOffset2, 'maxPlayers': 6, 'location': 78 } ],
            [ LocationButton, { 'x': 754 + 145, 'y': 535 - self.buttonOffset2, 'maxPlayers': 6, 'location': 79 } ],
            [ LocationButton, { 'x': 780 + 145, 'y': 550 - self.buttonOffset2, 'maxPlayers': 6, 'location': 80 } ],
            [ LocationButton, { 'x': 811 + 145, 'y': 540 - self.buttonOffset2, 'maxPlayers': 6, 'location': 81 } ],
            [ LocationButton, { 'x': 840 + 145, 'y': 525 - self.buttonOffset2, 'maxPlayers': 6, 'location': 82 } ],
            [ LocationButton, { 'x': 854 + 145, 'y': 494 - self.buttonOffset2, 'maxPlayers': 6, 'location': 83 } ],
            [ LocationButton, { 'x': 854 + 145, 'y': 466 - self.buttonOffset2, 'maxPlayers': 6, 'location': 84 } ],
            [ LocationButton, { 'x': 832 + 145, 'y': 440 - self.buttonOffset2, 'maxPlayers': 6, 'location': 85 } ],
            [ LocationButton, { 'x': 812 + 145, 'y': 415 - self.buttonOffset2, 'maxPlayers': 6, 'location': 86 } ],
            [ LocationButton, { 'x': 791 + 145, 'y': 392 - self.buttonOffset2, 'maxPlayers': 6, 'location': 87 } ],
            [ LocationButton, { 'x': 765 + 145, 'y': 377 - self.buttonOffset2, 'maxPlayers': 6, 'location': 88 } ],
            
            # Left down
            [ LocationButton, { 'x': 736 - 145, 'y': 352 - self.buttonOffset2, 'maxPlayers': 6, 'location': 89 } ],
            [ LocationButton, { 'x': 705 - 145, 'y': 378 - self.buttonOffset2, 'maxPlayers': 6, 'location': 90 } ],
            [ LocationButton, { 'x': 678 - 145, 'y': 390 - self.buttonOffset2, 'maxPlayers': 6, 'location': 91 } ],
            [ LocationButton, { 'x': 656 - 145, 'y': 416 - self.buttonOffset2, 'maxPlayers': 6, 'location': 92 } ],
            [ LocationButton, { 'x': 637 - 145, 'y': 440 - self.buttonOffset2, 'maxPlayers': 6, 'location': 93 } ],
            [ LocationButton, { 'x': 617 - 145, 'y': 466 - self.buttonOffset2, 'maxPlayers': 6, 'location': 94 } ],
            [ LocationButton, { 'x': 617 - 145, 'y': 494 - self.buttonOffset2, 'maxPlayers': 6, 'location': 95 } ],
            [ LocationButton, { 'x': 628 - 145, 'y': 525 - self.buttonOffset2, 'maxPlayers': 6, 'location': 96 } ],
            [ LocationButton, { 'x': 658 - 145, 'y': 540 - self.buttonOffset2, 'maxPlayers': 6, 'location': 97 } ],
            [ LocationButton, { 'x': 688 - 145, 'y': 550 - self.buttonOffset2, 'maxPlayers': 6, 'location': 98 } ],
            [ LocationButton, { 'x': 720 - 145, 'y': 535 - self.buttonOffset2, 'maxPlayers': 6, 'location': 99 } ],
            [ LocationButton, { 'x': 738 - 145, 'y': 510 - self.buttonOffset2, 'maxPlayers': 6, 'location': 100 } ],
            [ LocationButton, { 'x': 755 - 145, 'y': 535 - self.buttonOffset2, 'maxPlayers': 6, 'location': 101 } ],
            [ LocationButton, { 'x': 785 - 145, 'y': 550 - self.buttonOffset2, 'maxPlayers': 6, 'location': 102 } ],
            [ LocationButton, { 'x': 814 - 145, 'y': 540 - self.buttonOffset2, 'maxPlayers': 6, 'location': 103 } ],
            [ LocationButton, { 'x': 849 - 145, 'y': 528 - self.buttonOffset2, 'maxPlayers': 6, 'location': 104 } ],
            [ LocationButton, { 'x': 859 - 145, 'y': 494 - self.buttonOffset2, 'maxPlayers': 6, 'location': 105 } ],
            [ LocationButton, { 'x': 859 - 145, 'y': 466 - self.buttonOffset2, 'maxPlayers': 6, 'location': 106 } ],
            [ LocationButton, { 'x': 837 - 145, 'y': 438 - self.buttonOffset2, 'maxPlayers': 6, 'location': 107 } ],
            [ LocationButton, { 'x': 821 - 145, 'y': 418 - self.buttonOffset2, 'maxPlayers': 6, 'location': 108 } ],
            [ LocationButton, { 'x': 795 - 145, 'y': 390 - self.buttonOffset2, 'maxPlayers': 6, 'location': 109 } ],
            [ LocationButton, { 'x': 765 - 145, 'y': 378 - self.buttonOffset2, 'maxPlayers': 6, 'location': 110 } ],
            
            # Left 
            [ LocationButton, { 'x': 692 - self.buttonOffset, 'y': 317 - self.buttonOffset2, 'maxPlayers': 6, 'location': 111 } ],
            [ LocationButton, { 'x': 669 - self.buttonOffset, 'y': 347 - self.buttonOffset2, 'maxPlayers': 6, 'location': 112 } ],
            [ LocationButton, { 'x': 652 - self.buttonOffset, 'y': 375 - self.buttonOffset2, 'maxPlayers': 6, 'location': 113 } ],
            [ LocationButton, { 'x': 630 - self.buttonOffset, 'y': 396 - self.buttonOffset2, 'maxPlayers': 6, 'location': 114 } ],
            [ LocationButton, { 'x': 606 - self.buttonOffset, 'y': 416 - self.buttonOffset2, 'maxPlayers': 6, 'location': 115 } ],
            [ LocationButton, { 'x': 583 - self.buttonOffset, 'y': 437 - self.buttonOffset2, 'maxPlayers': 6, 'location': 116 } ],
            [ LocationButton, { 'x': 553 - self.buttonOffset, 'y': 437 - self.buttonOffset2, 'maxPlayers': 6, 'location': 117 } ],
            [ LocationButton, { 'x': 525 - self.buttonOffset, 'y': 423 - self.buttonOffset2, 'maxPlayers': 6, 'location': 118 } ],
            [ LocationButton, { 'x': 510 - self.buttonOffset, 'y': 393 - self.buttonOffset2, 'maxPlayers': 6, 'location': 119 } ],
            [ LocationButton, { 'x': 497 - self.buttonOffset, 'y': 363 - self.buttonOffset2, 'maxPlayers': 6, 'location': 120 } ],
            [ LocationButton, { 'x': 512 - self.buttonOffset, 'y': 333 - self.buttonOffset2, 'maxPlayers': 6, 'location': 121 } ],
            [ LocationButton, { 'x': 542 - self.buttonOffset, 'y': 318 - self.buttonOffset2, 'maxPlayers': 6, 'location': 122 } ],
            [ LocationButton, { 'x': 512 - self.buttonOffset, 'y': 300 - self.buttonOffset2, 'maxPlayers': 6, 'location': 123 } ],
            [ LocationButton, { 'x': 500 - self.buttonOffset, 'y': 270 - self.buttonOffset2, 'maxPlayers': 6, 'location': 124 } ],
            [ LocationButton, { 'x': 512 - self.buttonOffset, 'y': 240 - self.buttonOffset2, 'maxPlayers': 6, 'location': 125 } ],
            [ LocationButton, { 'x': 525 - self.buttonOffset, 'y': 208 - self.buttonOffset2, 'maxPlayers': 6, 'location': 126 } ],
            [ LocationButton, { 'x': 553 - self.buttonOffset, 'y': 196 - self.buttonOffset2, 'maxPlayers': 6, 'location': 127 } ],
            [ LocationButton, { 'x': 583 - self.buttonOffset, 'y': 196 - self.buttonOffset2, 'maxPlayers': 6, 'location': 128 } ],
            [ LocationButton, { 'x': 606 - self.buttonOffset, 'y': 217 - self.buttonOffset2, 'maxPlayers': 6, 'location': 129 } ],
            [ LocationButton, { 'x': 630 - self.buttonOffset, 'y': 237 - self.buttonOffset2, 'maxPlayers': 6, 'location': 130 } ],
            [ LocationButton, { 'x': 655 - self.buttonOffset, 'y': 258 - self.buttonOffset2, 'maxPlayers': 6, 'location': 131 } ],
            [ LocationButton, { 'x': 670 - self.buttonOffset, 'y': 287 - self.buttonOffset2, 'maxPlayers': 6, 'location': 132 } ],
        ]
        
        playerButtonX = ui.SPACING_LG
        playerButtonY = ui.SPACING_LG + ui.SPACING_SM + 80 + ui.SPACING_LG + ui.SPACING_SM
        
        players = playerManager.getAllPlayers()
        for i in range(1, len(players) + 1):
            modules.append([ PlayerButton, { 'x': playerButtonX, 'y': playerButtonY, 'player': players[i - 1] } ])
            
            playerButtonX += 225 + ui.SPACING_XS
            
            if i % 2 == 0:
                playerButtonX = ui.SPACING_LG
                playerButtonY += 100 + ui.SPACING_XS
            
        return modules
