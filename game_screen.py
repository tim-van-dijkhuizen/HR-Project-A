from screen import Screen
from score import Score
from button import Button
from dice_manager import DiceManager

class GameScreen(Screen):
    
    boardX = 440
    boardY = 60
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
        
    def getHandle(self):
        return 'game'
        
    def draw(self):    
        playerManager = self.app.getModule('playerManager')
            
        background(255, 74, 113)
        fill(11, 60, 73)
        
        textSize(30);
        textAlign(LEFT);
        
        text('Huidige beurt:', 60, 60)
        
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
        return [
            [ DiceManager, {  } ]    
        ]
        
