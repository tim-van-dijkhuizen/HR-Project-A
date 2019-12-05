from screen import Screen
from button import Button
from selectable_button import SelectableButton
from player_button import PlayerButton

class StartScreen(Screen):
    
    _backgroundImage = None
    
    def getHandle(self):
        return 'start'
    
    def isDefault(self):
        return True
    
    def setup(self):
        self._backgroundImage = loadImage('background.png')
        self._logoImage = loadImage('logo.png')

    def draw(self):
        image(self._backgroundImage, 0 , 0 , width, height)
        fill(11, 60, 73)
        
        textSize(25)
        textAlign(LEFT)
        text('Teams', 100, 100)
        
        textSize(25)
        textAlign(LEFT)
        text('Spelers', 100, 350)
        
        logoWidth = width / 3
        logoHeight = height / 3
        image(self._logoImage, width - (logoWidth + 100), height / 2 - logoHeight / 2, logoWidth, logoHeight)
        
    def keyPressed(self):
        if keyCode == 32:
            gameScreen = self.app.getScreen('game')
            self.app.setCurrentScreen(gameScreen)
            
    def setMaxToFour(self):
        playerManager = self.app.getModule('playerManager')
        playerManager.setMaxPlayers(4)
        
    def setMaxToSix(self):
        playerManager = self.app.getModule('playerManager')
        playerManager.setMaxPlayers(6)
       
    def startGame():
        gameScreen = self.app.getScreen('game')
        self.app.setCurrentScreen(gameScreen)
                      
    def getSubModules(self):
        modules = []
        playerManager = self.app.getModule('playerManager')
        
        modules.append([SelectableButton, {
            'x': width/18,
            'y': height/4,
            'width': 250,
            'height': 100,
            'textSize':(23),  
            'color': [255,74,113],
            'text': '2 teams',
            'textColor': [11, 60, 73],
            'group': 'maxPlayers',
            'selectedColor': [229, 250, 2],
            'onSelect': self.setMaxToFour,
            'default': True
        }])
        
        modules.append([SelectableButton, {
            'x': width/18*4,
            'y': height/4,
            'width': 250,
            'height': 100, 
            'textSize':(23), 
            'color': [255,74,113],
            'text': '3 Teams',
            'textColor': [11, 60, 73],
            'group': 'maxPlayers',
            'selectedColor': [229, 250, 2],
            'onSelect': self.setMaxToSix
        }])
     
        modules.append([Button, {
            'x': width/18,
            'y': height/4*3,
            'width': 250,
            'height': 100,
            'textSize':(23),  
            'color': [255,74,113],
            'text': 'START',
            'textColor': [11, 60, 73],
            'callback': self.startGame
        }])
        
        playerButtonY = 700
        for player in playerManager.getAllPlayers():
            modules.append([ PlayerButton, { 'x': 100, 'y': playerButtonY, 'player': player } ])
            playerButtonY += 150
            
        return modules
    
