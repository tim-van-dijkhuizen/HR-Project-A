from screen import Screen
from score import Score
from button import Button
from dice_manager import DiceManager

class GameScreen(Screen):
    
    boardWidth = 700
    boardHeight = 400
    
    boardImageFour = None
    boardImageSix = None
    
    fromScreen = None
    player = None
    
    def setup(self):
        playerManager = self.app.getModule('playerManager')
        
        self.boardImageFour = loadImage('board-players4.png')
        self.boardImageSix = loadImage('board-players6.png')
        
        self.boardX = 440
        self.boardY = 60
        
    def getHandle(self):
        return 'game'
        
    def draw(self):    
        playerManager = self.app.getModule('playerManager')
            
        background(255, 74, 113)
        fill(11, 60, 73)
        
        textSize(30);
        textAlign(LEFT);
        
        text('Huidige beurt:', 50, 50)
        
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
        
    def rollDice(self):
        diceManager = self.app.getModule('diceManager')
        diceManager.rollDice()
    
    def getSubModules(self):
        
        testButton = [Button, {
            'x': 50,
            'y': 250,
            'width': 150,
            'height': 100, 
            'color': [255, 255, 255],
            'text': 'Test knop',
            'textSize': 10,
            'textColor': [11, 60, 73]
        }]
        
        testButton2 = [Button, {
            'x': 50,
            'y': 375,
            'width': 150,
            'height': 100, 
            'color': [255, 255, 255],
            'text': 'Test knop 2',
            'textSize': 10,
            'textColor': [11, 60, 73]
        }]
        
        testButton3 = [Button, {
            'x': 50,
            'y': 500,
            'width': 150,
            'height': 100, 
            'color': [255, 255, 255],
            'text': 'Test knop 3',
            'textSize': 10,
            'textColor': [11, 60, 73],
            'maxPlayers': 6
        }]

        testButton4 = [Button, {
            'x': 225,
            'y': 250,
            'width': 150,
            'height': 100, 
            'color': [255, 255, 255],
            'text': 'Test knop 4',
            'textSize': 10,
            'textColor': [11, 60, 73],
            'callback': self.rollDice
        }]
        testButton5 = [Button, {
            'x': 225,
            'y': 375,
            'width': 150,
            'height': 100, 
            'color': [255, 255, 255],
            'text': 'Test knop 2',
            'textSize': 10,
            'textColor': [11, 60, 73]
        }]
        testButton6 = [Button, {
            'x': 225,
            'y': 500,
            'width': 150,
            'height': 100, 
            'color': [255, 255, 255],
            'text': 'Test knop 2',
            'textSize': 10,
            'textColor': [11, 60, 73],
            'maxPlayers': 6
        }]
        testButton7 = [Button, {
            'x': 275,
            'y': 75,
            'width': 100,
            'height': 50, 
            'color': [255, 255, 255],
            'text': 'Volgende',
            'textSize': 10,
            'textColor': [11, 60, 73]
        }]
        
        [ Button, { 'x': 20, 'y': 20, 'width': 100, 'height': 50, 'text': 'Terug', 'textSize': 20, 'callback': self.goBack } ]
        
        return [
          #  [ Score, {} ],
            [ DiceManager, {  } ],
            testButton,
            testButton2,
            testButton3,
            testButton4,
            testButton5,
            testButton6,
            testButton7
        ]
        
