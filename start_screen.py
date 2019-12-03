from screen import Screen
from button import Button

class StartScreen(Screen):
    
    def getHandle(self):
        return 'start'
    
    def isDefault(self):
        return True
        
    def draw(self):
        background(112,238,255)
        fill(11, 60, 73)
        
        textSize(38);
        text('Kies het aantal teams', width/3.6, height/6.2);
        
        textSize(38);
        text('Kies het aantal spelers', width/3.6, height/2.9);
    
        
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
            'x': width / 2 - (400),
            'y': 200,
            'width': 250,
            'height': 100,
            'textSize':(23), 
            'color': [255,74,113],
            'text': '3 teams',
            'textColor': [11, 60, 73],
            'callback': self.testButtonAction1
        }]
        
        testButton2 = [Button, {
            'x': width / 2 - (700),
            'y': 200,
            'width': 250,
            'height': 100,
            'textSize':(23),  
            'color': [255,74,113],
            'text': '2 Teams',
            'textColor': [11, 60, 73],
            'callback': self.testButtonAction2
        }]
        
        testButton3 = [Button, {
            'x': width / 2 - (400),
            'y': 400,
            'width': 250,
            'height': 100, 
            'textSize':(23), 
            'color': [255,74,113],
            'text': 'Naam',
            'textColor': [11, 60, 73],
            'callback': self.testButtonAction1
        }]
   
        testButton4 = [Button, {
            'x': width / 2 - (700),
            'y': 400,
            'width': 250,
            'height': 100, 
            'textSize':(23), 
            'color': [255,74,113],
            'text': 'Naam',
            'textColor': [11, 60, 73],
            'callback': self.testButtonAction1
        }]
   
        testButton5 = [Button, {
            'x': width / 2 - (400),
            'y': 600,
            'width': 250,
            'height': 100, 
            'textSize':(23), 
            'color': [255,74,113],
            'text': 'Naam',
            'textColor': [11, 60, 73],
            'callback': self.testButtonAction1
        }]
     
        testButton6 = [Button, {
            'x': width / 2 - (700),
            'y': 600,
            'width': 250,
            'height': 100, 
            'textSize':(23), 
            'color': [255,74,113],
            'text': 'Naam',
            'textColor': [11, 60, 73],
            'callback': self.testButtonAction1
        }]
     
        testButton7 = [Button, {
            'x': width / 3.6 - 125,
            'y': 800,
            'width': 250,
            'height': 100,
            'textSize':(23),  
            'color': [255,74,113],
            'text': 'START',
            'textColor': [11, 60, 73],
            'callback': self.testButtonAction1
        }]
     
        return [
            testButton1,
            testButton2,
            testButton3,
            testButton4,
            testButton5,
            testButton6,
            testButton7
        
        ]
