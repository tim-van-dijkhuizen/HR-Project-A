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
            
            [ LocationButton, { 'x': self.boardX, 'y': self.boardY, 'width': 100, 'height': 100, 'location': 1 } ],
            [ LocationButton, { 'x': self.boardX, 'y': self.boardY + 100, 'width': 100, 'height': 100, 'location': 2 } ],
            [ LocationButton, { 'x': self.boardX, 'y': self.boardY + 200, 'width': 100, 'height': 100, 'location': 3 } ]    
        ]
        
