from screen import Screen
from button import Button
from user_input import UserInput

class StartScreen(Screen):
    
    def getHandle(self):
        return 'start'
    
    def isDefault(self):
        return True
        
    def draw(self):
        background(0, 0, 255)
        fill(11, 60, 73)
        textSize(50);
        
        text('Love it!', 600, 100)
        
        textSize(25);
        text('Kies het aantal teams', 600, 180)
    
        
    def keyPressed(self):
        if keyCode == 10:
            gameScreen = self.app.getScreen('game')
            self.app.setCurrentScreen(gameScreen)
            
    def testButtonAction1(self):
        playerManager = self.app.getModule('playerManager')
        playerManager.setMaxPlayers(6)
        
    def testButtonAction2(self):
        playerManager = self.app.getModule('playerManager')
        playerManager.setMaxPlayers(4)
        
    def testButtonAction3(self):
        playerManager = self.app.getModule('playerManager')
        player = playerManager.getPlayer(1)
        
        player.name = 'Tim'
        print(player, player.name)
            
    def getSubModules(self):
        playerManager = self.app.getModule('playerManager')
        
        testButton1 = [Button, {
            'x': 300,
            'y': 250,
            'width': 250,
            'height': 100, 
            'color': [242, 84, 91],
            'text': '2 Teams',
            'textColor': [11, 60, 73],
            'callback': self.testButtonAction2
        }]
        
        testButton2 = [Button, {
            'x': 650,
            'y': 250,
            'width': 250,
            'height': 100, 
<<<<<<< Updated upstream
            'color': [242, 84, 91],
            'text': '3 Teams',
=======
            'color': [255,74,113],
            'text':'Naam',
>>>>>>> Stashed changes
            'textColor': [11, 60, 73],
            'callback': self.testButtonAction1
        }]
   
        testButton3 = [Button, {
            'x': 400,
            'y': 400,
            'width': 400,
            'height': 100, 
            'color': [242, 84, 91],
            'text': 'Game manual',
            'textColor': [11, 60, 73],
            'callback': self.testButtonAction3
        }]
   
        return [
            testButton1,
            testButton2,
            testButton3
        
        ]
