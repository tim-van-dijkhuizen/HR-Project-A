from screen import Screen
from button import Button
from selectable_button import SelectableButton

class StartScreen(Screen):
    
    def getHandle(self):
        return 'start'
    
    def isDefault(self):
        return True
        
    def draw(self):
        background(112,238,255)
        fill(11, 60, 73)
        
        textSize(50);
        text('Love It!', width / 2, 100);
        
        textSize(25);
        text('Kies het aantal teams', width / 2, 200);
        
        textSize(25);
        text('Configureer de spelers', width/2, 450);
            
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
        playerManager = self.app.getModule('playerManager')
        
        maxToFourButton = [SelectableButton, {
            'x': width / 2 - (260),
            'y': 250,
            'width': 250,
            'height': 100, 
            'color': [255,74,113],
            'text': '2 teams',
            'textColor': [11, 60, 73],
            'group': 'maxPlayers',
            'selectedColor': [255, 22, 84],
            'onSelect': self.setMaxToFour,
            'default': True
        }]
        
        maxToSixButton = [SelectableButton, {
            'x': width / 2 + 10,
            'y': 250,
            'width': 250,
            'height': 100, 
            'color': [255,74,113],
            'text': '3 Teams',
            'textColor': [11, 60, 73],
            'group': 'maxPlayers',
            'selectedColor': [255, 22, 84],
            'onSelect': self.setMaxToSix
        }]
        
        testButton = [SelectableButton, {
            'x': width / 2 + 10,
            'y': 500,
            'width': 250,
            'height': 100, 
            'color': [255,74,113],
            'text': 'Test',
            'textColor': [11, 60, 73],
            'group': 'test',
            'selectedColor': [255, 22, 84]
        }]
     
        startButton = [Button, {
            'x': width / 2 - 125,
            'y': 800,
            'width': 250,
            'height': 100, 
            'color': [255,74,113],
            'text': 'START',
            'textColor': [11, 60, 73],
            'callback': self.startGame
        }]
     
        return [
            maxToFourButton,
            maxToSixButton,
            startButton,
            testButton
        ]
