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
            
    def getSubModules(self):
        testButton = [Button, {
            'x': 600,
            'y': 200,
            'width': 120,
            'height': 100, 
            'color': [242, 84, 91],
            'text': '3 Teams',
            'textColor': [11, 60, 73],
        }]
        
        testButton2 = [Button, {
            'x': 400,
            'y': 200,
            'width': 120,
            'height': 100, 
            'color': [242, 84, 91],
            'text': '2 Teams',
            'textColor': [11, 60, 73],
        }]
        
        testButton3 = [Button, {
            'x': 650,
            'y': 400,
            'width': 250,
            'height': 100, 
            'color': [242, 84, 91],
            'text': 'Met de klok mee',
            'textColor': [11, 60, 73],
        }]
   
        testButton4 = [Button, {
            'x': 350,
            'y': 400,
            'width': 250,
            'height': 100, 
            'color': [242, 84, 91],
            'text': 'Tegen de klok in',
            'textColor': [11, 60, 73],
        }]
   
        return [
            testButton,
            testButton2,
            testButton3,
            testButton4
        
        ]
