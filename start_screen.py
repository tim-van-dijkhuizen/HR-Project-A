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
        text('Teams', 60, 60)
        
        textSize(25)
        textAlign(LEFT)
        text('Spelers', 60, 220)
        
        logoWidth = 400
        logoHeight = 300
    
        image(self._logoImage, 750, 100, logoWidth, logoHeight)
        
    def keyPressed(self):
        if keyCode == 10:
            gameScreen = self.app.getScreen('game')
            self.app.setCurrentScreen(gameScreen)
            
    def setMaxToFour(self):
        playerManager = self.app.getModule('playerManager')
        playerManager.setMaxPlayers(4)
        
    def setMaxToSix(self):
        playerManager = self.app.getModule('playerManager')
        playerManager.setMaxPlayers(6)
       
    def startDisabled(self):
        playerManager = self.app.getModule('playerManager')
        configInvalid = False

        # Make sure a bot was selected
        botSelected = False
        for player in playerManager.getPlayers():
            if player.bot: botSelected = True
            
            if player.name == None or len(player.name) <= 0:
                configInvalid = True
            
            if player.location == None:
                configInvalid = True
            
        if not botSelected: 
            configInvalid = True
        
        return configInvalid
       
    def startGame(self):
        gameScreen = self.app.getScreen('game')
        self.app.setCurrentScreen(gameScreen)
                      
    def getSubModules(self):
        modules = []
        playerManager = self.app.getModule('playerManager')
        
        modules.append([SelectableButton, {
            'x': 60,
            'y': 90,
            'width': 225,
            'height': 80,
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
            'x': 295,
            'y': 90,
            'width': 225,
            'height': 80, 
            'textSize':(23), 
            'color': [255,74,113],
            'text': '3 Teams',
            'textColor': [11, 60, 73],
            'group': 'maxPlayers',
            'selectedColor': [229, 250, 2],
            'onSelect': self.setMaxToSix
        }])
     
        modules.append([Button, {
            'x': 850,
            'y': height/4*3,
            'width': 200,
            'height': 80,
            'textSize':(23),  
            'color': [255,74,113],
            'text': 'START',
            'textColor': [11, 60, 73],
            'callback': self.startGame,
            'disabled': self.startDisabled
        }])
        
        playerButtonX = 60
        playerButtonY = 250
        
        players = playerManager.getAllPlayers()
        for i in range(1, len(players) + 1):
            modules.append([ PlayerButton, { 'x': playerButtonX, 'y': playerButtonY, 'player': players[i - 1] } ])
            
            playerButtonX += 235
            
            if i % 2 == 0:
                playerButtonX = 60
                playerButtonY += 110
            
        return modules
