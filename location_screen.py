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
            
            ]
        
        
