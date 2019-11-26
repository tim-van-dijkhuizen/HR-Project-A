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
    
        
    def keyPressed(self):
        if keyCode == 10:
            gameScreen = self.app.getScreen('game')
            self.app.setCurrentScreen(gameScreen)
            
    def getSubModules(self):
        team3Button = [Button, {
            'x': 650,
            'y': 200,
            'width': 250,
            'height': 100, 
            'color': [242, 84, 91],
            'text': '3 teams',
            'textColor': [11, 60, 73],
        }]
        
        team2Button = [Button, {
            'x': 300,
            'y': 200,
            'width': 250,
            'height': 100, 
            'color': [242, 84, 91],
            'text': '2 Teams',
            'textColor': [11, 60, 73],
        }]
   
        gamemanualButton = [Button, {
            'x': 475,
            'y': 400,
            'width': 250,
            'height': 100, 
            'color': [242, 84, 91],
            'text': 'Game manual',
            'textColor': [11, 60, 73],
        }]
   
        return [
            team3Button,
            team2Button,
            gamemanualButton
        
        ]
