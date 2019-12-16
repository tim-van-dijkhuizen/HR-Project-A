import ui
from screen import Screen
from button import Button
from dice_manager import DiceManager
from location_button  import LocationButton

class GameScreen(Screen):
    
    boardX = 440
    boardY = ui.SPACING_LG
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
            
        background(ui.COLOR_RED_LIGHT)
        
        fill(ui.COLOR_TEXT)
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
