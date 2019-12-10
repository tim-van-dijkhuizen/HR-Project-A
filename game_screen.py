from screen import Screen
from score import Score
from button import Button

class GameScreen(Screen):
    
    boardWidth = 800
    boardHeight = 500
    
    boardImageFour = None
    boardImageSix = None
    
    fromScreen = None
    player = None
    
    def setup(self):
        
        playerManager = self.app.getModule('playerManager')
        
        self.boardImageFour = loadImage('board-players4.png')
        self.boardImageSix = loadImage('board-players6.png')
        
        self.boardX = 200
        self.boardY = 75
        
    def getHandle(self):
        return 'game'
        
    def draw(self):
        
        playerManager = self.app.getModule('playerManager')
            
        background(255, 74, 113)
        fill(11, 60, 73)
        
        textSize(50);
        textAlign(LEFT);
        
        text('Spelers', 475, 100)
        
        boardImage = self.boardImageSix if playerManager.maxPlayers == 6 else self.boardImageFour
        image(boardImage, self.boardX, self.boardY, self.boardWidth, self.boardHeight)
    
    def keyPressed(self):
        if keyCode == 32:
            startScreen = self.app.getScreen('start')
            self.app.setCurrentScreen(startScreen)
            
    def goBack(self):
        self.app.setCurrentScreen(self.fromScreen)
        self.fromScreen = None
        self.player = None
    
    def getSubModules(self):
        testButton = [Button, {
            'x': 50,
            'y': 100,
            'width': 50,
            'height': 50, 
            'color': [255, 255, 255],
            'text': 'Test knop',
            'textSize': 10,
            'textColor': [11, 60, 73],
            'callback': self.printTest
        }]
        
        testButton2 = [Button, {
            'x': 50,
            'y': 550,
            'width': 50,
            'height': 50, 
            'color': [255, 255, 255],
            'text': 'Test knop 2',
            'textColor': [11, 60, 73],
            'callback': self.printTest
        }]
        
        testButton3 = [Button, {
            'x': 1100,
            'y': 100,
            'width': 50,
            'height': 50, 
            'color': [255, 255, 255],
            'text': 'Test knop 3',
            'textColor': [11, 60, 73],
            'callback': self.printTest
        }]
        
        testButton4 = [Button, {
            'x': 1100,
            'y': 550,
            'width': 50,
            'height': 50, 
            'color': [255, 255, 255],
            'text': 'Test knop 2',
            'textColor': [11, 60, 73],
            'callback': self.printTest
        }]
        [ Button, { 'x': 20, 'y': 20, 'width': 100, 'height': 50, 'text': 'Terug', 'textSize': 20, 'callback': self.goBack } ]
        
        return [
            [ Score, {} ],
            testButton,
            testButton2,
            testButton3,
            testButton4
        ]
        
    def printTest(self):
        scoreModule = self.app.getModule('gameCounter')
