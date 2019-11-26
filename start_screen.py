from screen import Screen
from button import Button

class StartScreen(Screen):
    
    def getHandle(self):
        return 'start'
    
    def isDefault(self):
        return True
        
    def draw(self):
        background(0, 0, 255)
        fill(11, 60, 73)
        
        text('Press enter to start', 100, 100)
        
    def keyPressed(self):
        if keyCode == 10:
            gameScreen = self.app.getScreen('game')
            self.app.setCurrentScreen(gameScreen)
            
    def testButtonAction1(self):
        playerManager = self.app.getModule('playerManager')
        playerManager.maxPlayers = 6
        playerManager.updateList()
        
    def testButtonAction2(self):
        playerManager = self.app.getModule('playerManager')
        playerManager.maxPlayers = 4
        playerManager.updateList()
        
    def testButtonAction3(self):
        playerManager = self.app.getModule('playerManager')
        player = playerManager.getPlayer(1)
        
        player.name = 'Tim'
        print(player, player.name)
            
    def getSubModules(self):
        playerManager = self.app.getModule('playerManager')
        
        testButton = [Button, {
            'x': 600,
            'y': 200,
            'width': 120,
            'height': 100, 
            'color': [242, 84, 91],
            'text': '3 Teams',
            'textColor': [11, 60, 73],
            'callback': playerManager.updateList
        }]
        
        testButton2 = [Button, {
            'x': 400,
            'y': 200,
            'width': 120,
            'height': 100, 
            'color': [242, 84, 91],
            'text': '2 Teams',
            'textColor': [11, 60, 73],
            'callback': self.testButtonAction1
        }]
        
        testButton3 = [Button, {
            'x': 650,
            'y': 400,
            'width': 250,
            'height': 100, 
            'color': [242, 84, 91],
            'text': 'Met de klok mee',
            'textColor': [11, 60, 73],
            'callback': self.testButtonAction2
        }]
   
        testButton4 = [Button, {
            'x': 350,
            'y': 400,
            'width': 250,
            'height': 100, 
            'color': [242, 84, 91],
            'text': 'Tegen de klok in',
            'textColor': [11, 60, 73],
            'callback': self.testButtonAction3
        }]
   
        return [
            testButton,
            testButton2,
            testButton3,
            testButton4
        
        ]
