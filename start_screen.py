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
        textSize(50);
        
        text('Love it!', 600, 100)
        
        textSize(25);
        text('Kies het aantal teams', 600, 180)
        
        textSize(25);
        text('Kies het aantal spelers', 600, 380)
    
        
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
            'x': 600,
            'y': 200,
            'width': 250,
            'height': 100, 
            'color': [242, 84, 91],
            'text': '3 teams',
            'textColor': [11, 60, 73],
            'callback': playerManager.updateList
        }]
        
        testButton2 = [Button, {
            'x': 300,
            'y': 200,
            'width': 250,
            'height': 100, 
            'color': [242, 84, 91],
            'text': '2 Teams',
            'textColor': [11, 60, 73],
            'callback': self.testButtonAction1
        }]
        
        testButton3 = [Button, {
            'x': 600,
            'y': 400,
            'width': 250,
            'height': 100, 
            'color': [242, 84, 91],
            'text': 'Naam',
            'textColor': [11, 60, 73],
            'callback': self.testButtonAction1
        }]
   
        testButton4 = [Button, {
            'x': 300,
            'y': 400,
            'width': 250,
            'height': 100, 
            'color': [242, 84, 91],
            'text': 'Naam',
            'textColor': [11, 60, 73],
            'callback': self.testButtonAction1
        }]
   
        testButton5 = [Button, {
            'x': 300,
            'y': 600,
            'width': 250,
            'height': 100, 
            'color': [242, 84, 91],
            'text': 'Naam',
            'textColor': [11, 60, 73],
            'callback': self.testButtonAction1
        }]
     
        testButton6 = [Button, {
            'x': 600,
            'y': 600,
            'width': 250,
            'height': 100, 
            'color': [242, 84, 91],
            'text': 'Naam',
            'textColor': [11, 60, 73],
            'callback': self.testButtonAction1
        }]
     
        testButton7 = [Button, {
            'x': 450,
            'y': 800,
            'width': 250,
            'height': 100, 
            'color': [242, 84, 91],
            'text': 'Start',
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
