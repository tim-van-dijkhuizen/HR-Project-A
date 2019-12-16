import ui
from screen import Screen
from button import Button
from dice_manager import DiceManager
from location_button  import LocationButton
from player_button import PlayerButton

class GameScreen(Screen):
    
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
            
        background(ui.COLOR_RED_LIGHT)
        
        fill(ui.COLOR_TEXT)
        textSize(30);
        textAlign(LEFT);
        text('Huidige beurt:', 60, 60)
        
        for player in playerManager.getPlayers():
            print(player.getLocation())
            
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
        return [
            [ DiceManager, {  } ]    
        ]
