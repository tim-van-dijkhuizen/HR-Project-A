from screen import Screen
from button import Button
from location_button  import LocationButton

class LocationScreen(Screen):
    
    # Settings
    boardWidth = 794
    boardHeight = 500
    
    # Image of the board game
    boardImageFour = None
    boardImageSix = None
    
    # The player to edit the location for
    fromScreen = None
    player = None
    
    def getHandle(self):
        return 'location'
        
    def setup(self):
        playerManager = self.app.getModule('playerManager')
        
        # Load board image
        self.boardImageFour = loadImage('board-players4.png')
        self.boardImageSix = loadImage('board-players6.png')
        
        self.boardX = width / 2 - (self.boardWidth / 3.2)
        self.boardY = height / 2 - (self.boardHeight / 2)
            
    def draw(self):
        playerManager = self.app.getModule('playerManager')
        
        if self.player == None or self.fromScreen == None:
            raise ValueError('Variables player and fromScreen must be set')
            
        # Background
        background(255, 74, 113)
        
        # Board    
        boardImage = self.boardImageSix if playerManager.maxPlayers == 6 else self.boardImageFour
        image(boardImage, self.boardX, self.boardY, self.boardWidth, self.boardHeight)
        
        # Current location
        fill(0, 0, 0)
        textSize(35)
        textAlign(CENTER)
        text('Location: ' + str(self.player.location), width / 5, 100)
        
    def keyPressed(self):
        try:
            location = int(key)
        except ValueError:
            location = 0
            
        self.player.location = location
            
    def goBack(self):
        self.app.setCurrentScreen(self.fromScreen)
        self.fromScreen = None
        self.player = None
            
        
    def getSubModules(self):
        return [
            [ Button, { 'x': 20, 'y': 20, 'width': 100, 'height': 50, 'text': 'Terug', 'textSize': 20, 'callback': self.goBack } ],
            
            [ LocationButton, { 'x': 735, 'y': 275, 'maxPlayers': 4, 'location': 1 } ],
            [ LocationButton, { 'x': 705, 'y': 250, 'maxPlayers': 4, 'location': 2 } ],
            [ LocationButton, { 'x': 678, 'y': 236, 'maxPlayers': 4, 'location': 3 } ],
            [ LocationButton, { 'x': 655, 'y': 210, 'maxPlayers': 4, 'location': 4 } ],
            [ LocationButton, { 'x': 635, 'y': 189, 'maxPlayers': 4, 'location': 5 } ],
            [ LocationButton, { 'x': 615, 'y': 166, 'maxPlayers': 4, 'location': 6 } ],
            [ LocationButton, { 'x': 615, 'y': 134, 'maxPlayers': 4, 'location': 7 } ],
            [ LocationButton, { 'x': 628, 'y': 105, 'maxPlayers': 4, 'location': 8 } ],
            [ LocationButton, { 'x': 658, 'y': 93, 'maxPlayers': 4, 'location': 9 } ],
            [ LocationButton, { 'x': 688, 'y': 82, 'maxPlayers': 4, 'location': 10 } ],
            [ LocationButton, { 'x': 715, 'y': 93, 'maxPlayers': 4, 'location': 11 } ],
            [ LocationButton, { 'x': 735, 'y': 120, 'maxPlayers': 4, 'location': 12 } ],
            [ LocationButton, { 'x': 750, 'y': 93, 'maxPlayers': 4, 'location': 13 } ],
            [ LocationButton, { 'x': 780, 'y': 82, 'maxPlayers': 4, 'location': 14 } ],
            [ LocationButton, { 'x': 810, 'y': 93, 'maxPlayers': 4, 'location': 15 } ],
            [ LocationButton, { 'x': 838, 'y': 108, 'maxPlayers': 4, 'location': 16 } ],
            [ LocationButton, { 'x': 852, 'y': 137, 'maxPlayers': 4, 'location': 17 } ],
            [ LocationButton, { 'x': 852, 'y': 166, 'maxPlayers': 4, 'location': 18 } ],
            [ LocationButton, { 'x': 830, 'y': 189, 'maxPlayers': 4, 'location': 19 } ],
            [ LocationButton, { 'x': 810, 'y': 212, 'maxPlayers': 4, 'location': 20 } ],
            [ LocationButton, { 'x': 791, 'y': 236, 'maxPlayers': 4, 'location': 21 } ],
            [ LocationButton, { 'x': 765, 'y': 250, 'maxPlayers': 4, 'location': 22 } ],
            
            [ LocationButton, { 'x': 779, 'y': 312, 'maxPlayers': 4, 'location': 23 } ],
            [ LocationButton, { 'x': 803, 'y': 282, 'maxPlayers': 4, 'location': 24 } ],
            [ LocationButton, { 'x': 818, 'y': 255, 'maxPlayers': 4, 'location': 25 } ], 
            [ LocationButton, { 'x': 840, 'y': 235, 'maxPlayers': 4, 'location': 26 } ],
            [ LocationButton, { 'x': 863, 'y': 215, 'maxPlayers': 4, 'location': 27 } ], 
            [ LocationButton, { 'x': 888, 'y': 192, 'maxPlayers': 4, 'location': 28 } ],
            [ LocationButton, { 'x': 918, 'y': 192, 'maxPlayers': 4, 'location': 29 } ],
            [ LocationButton, { 'x': 948, 'y': 204, 'maxPlayers': 4, 'location': 30 } ],
            [ LocationButton, { 'x': 960, 'y': 235, 'maxPlayers': 4, 'location': 31 } ],
            [ LocationButton, { 'x': 973, 'y': 265, 'maxPlayers': 4, 'location': 32 } ],
            [ LocationButton, { 'x': 957, 'y': 295, 'maxPlayers': 4, 'location': 33 } ],
            [ LocationButton, { 'x': 930, 'y': 312, 'maxPlayers': 4, 'location': 34 } ],
            [ LocationButton, { 'x': 957, 'y': 327, 'maxPlayers': 4, 'location': 35 } ],
            [ LocationButton, { 'x': 970, 'y': 357, 'maxPlayers': 4, 'location': 36 } ],
            [ LocationButton, { 'x': 960, 'y': 387, 'maxPlayers': 4, 'location': 37 } ],
            [ LocationButton, { 'x': 945, 'y': 415, 'maxPlayers': 4, 'location': 38 } ],
            [ LocationButton, { 'x': 915, 'y': 432, 'maxPlayers': 4, 'location': 39 } ],
            [ LocationButton, { 'x': 885, 'y': 432, 'maxPlayers': 4, 'location': 40 } ],
            [ LocationButton, { 'x': 863, 'y': 410, 'maxPlayers': 4, 'location': 41 } ],
            [ LocationButton, { 'x': 840, 'y': 389, 'maxPlayers': 4, 'location': 42 } ],
            [ LocationButton, { 'x': 818, 'y': 368, 'maxPlayers': 4, 'location': 43 } ],
            [ LocationButton, { 'x': 802, 'y': 342, 'maxPlayers': 4, 'location': 44 } ],
            
            [ LocationButton, { 'x': 735, 'y': 353, 'maxPlayers': 4, 'location': 45 } ],
            [ LocationButton, { 'x': 765, 'y': 378, 'maxPlayers': 4, 'location': 46 } ],
            [ LocationButton, { 'x': 791, 'y': 393, 'maxPlayers': 4, 'location': 47 } ],
            [ LocationButton, { 'x': 812, 'y': 415, 'maxPlayers': 4, 'location': 48 } ],
            [ LocationButton, { 'x': 832, 'y': 438, 'maxPlayers': 4, 'location': 49 } ],
            [ LocationButton, { 'x': 852, 'y': 466, 'maxPlayers': 4, 'location': 50 } ],
            [ LocationButton, { 'x': 852, 'y': 496, 'maxPlayers': 4, 'location': 51 } ],
            [ LocationButton, { 'x': 840, 'y': 524, 'maxPlayers': 4, 'location': 52 } ],
            [ LocationButton, { 'x': 810, 'y': 538, 'maxPlayers': 4, 'location': 53 } ],
            [ LocationButton, { 'x': 780, 'y': 548, 'maxPlayers': 4, 'location': 54 } ],
            [ LocationButton, { 'x': 753, 'y': 536, 'maxPlayers': 4, 'location': 55 } ],
            [ LocationButton, { 'x': 735, 'y': 510, 'maxPlayers': 4, 'location': 56 } ],
            [ LocationButton, { 'x': 719, 'y': 536, 'maxPlayers': 4, 'location': 57 } ],
            [ LocationButton, { 'x': 688, 'y': 548, 'maxPlayers': 4, 'location': 58 } ],
            [ LocationButton, { 'x': 660, 'y': 534, 'maxPlayers': 4, 'location': 59 } ],
            [ LocationButton, { 'x': 630, 'y': 521, 'maxPlayers': 4, 'location': 60 } ],
            [ LocationButton, { 'x': 616, 'y': 494, 'maxPlayers': 4, 'location': 61 } ],
            [ LocationButton, { 'x': 616, 'y': 462, 'maxPlayers': 4, 'location': 62 } ],
            [ LocationButton, { 'x': 638, 'y': 440, 'maxPlayers': 4, 'location': 63 } ],
            [ LocationButton, { 'x': 657, 'y': 415, 'maxPlayers': 4, 'location': 64 } ],
            [ LocationButton, { 'x': 678, 'y': 393, 'maxPlayers': 4, 'location': 65 } ],
            [ LocationButton, { 'x': 705, 'y': 378, 'maxPlayers': 4, 'location': 66 } ],
            
            [ LocationButton, { 'x': 692, 'y': 312, 'maxPlayers': 4, 'location': 67 } ],
            [ LocationButton, { 'x': 669, 'y': 342, 'maxPlayers': 4, 'location': 68 } ],
            [ LocationButton, { 'x': 652, 'y': 368, 'maxPlayers': 4, 'location': 69 } ],
            [ LocationButton, { 'x': 630, 'y': 389, 'maxPlayers': 4, 'location': 70 } ],
            [ LocationButton, { 'x': 606, 'y': 410, 'maxPlayers': 4, 'location': 71 } ],
            [ LocationButton, { 'x': 583, 'y': 432, 'maxPlayers': 4, 'location': 72 } ],
            [ LocationButton, { 'x': 553, 'y': 432, 'maxPlayers': 4, 'location': 73 } ],
            [ LocationButton, { 'x': 525, 'y': 420, 'maxPlayers': 4, 'location': 74 } ],
            [ LocationButton, { 'x': 510, 'y': 390, 'maxPlayers': 4, 'location': 75 } ],
            [ LocationButton, { 'x': 497, 'y': 360, 'maxPlayers': 4, 'location': 76 } ],
            [ LocationButton, { 'x': 512, 'y': 330, 'maxPlayers': 4, 'location': 77 } ],
            [ LocationButton, { 'x': 542, 'y': 314, 'maxPlayers': 4, 'location': 78 } ],
            [ LocationButton, { 'x': 512, 'y': 298, 'maxPlayers': 4, 'location': 79 } ],
            [ LocationButton, { 'x': 500, 'y': 267, 'maxPlayers': 4, 'location': 80 } ],
            [ LocationButton, { 'x': 512, 'y': 238, 'maxPlayers': 4, 'location': 81 } ],
            [ LocationButton, { 'x': 525, 'y': 208, 'maxPlayers': 4, 'location': 82 } ],
            [ LocationButton, { 'x': 553, 'y': 195, 'maxPlayers': 4, 'location': 83 } ],
            [ LocationButton, { 'x': 583, 'y': 195, 'maxPlayers': 4, 'location': 84 } ],
            [ LocationButton, { 'x': 606, 'y': 215, 'maxPlayers': 4, 'location': 85 } ],
            [ LocationButton, { 'x': 630, 'y': 235, 'maxPlayers': 4, 'location': 86 } ],
            [ LocationButton, { 'x': 652, 'y': 258, 'maxPlayers': 4, 'location': 87 } ],
            [ LocationButton, { 'x': 669, 'y': 282, 'maxPlayers': 4, 'location': 88 } ],
            
            
            ]
        
        
