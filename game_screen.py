from screen import Screen
from score import Score
from button import Button

class GameScreen(Screen):
        
    def getHandle(self):
        return 'game'
        
    def draw(self):
        background(0, 255, 0)
        fill(11, 60, 73)
        
        textSize(50);
        textAlign(LEFT);
        
        text('Spelers', 475, 100)
    
    def keyPressed(self):
        if keyCode == 32:
            startScreen = self.app.getScreen('start')
            self.app.setCurrentScreen(startScreen)
    
    def getSubModules(self):
        testButton = [Button, {
            'x': 50,
            'y': 100,
            'width': 90,
            'height': 50, 
            'color': [242, 84, 91],
            'text': 'Test knop',
            'textSize': 10,
            'textColor': [11, 60, 73],
            'callback': self.printTest
        }]
        
        testButton2 = [Button, {
            'x': 200,
            'y': 100,
            'width': 90,
            'height': 50, 
            'color': [242, 84, 91],
            'text': 'Test knop 2',
            'textColor': [11, 60, 73],
            'callback': self.printTest
        }]
        
        testButton3 = [Button, {
            'x': 350,
            'y': 100,
            'width': 90,
            'height': 50, 
            'color': [242, 84, 91],
            'text': 'Test knop 3',
            'textColor': [11, 60, 73],
            'callback': self.printTest
        }]
        
        testButton4 = [Button, {
            'x': 600,
            'y': 100,
            'width': 90,
            'height': 50, 
            'color': [242, 84, 91],
            'text': 'Test knop 2',
            'textColor': [11, 60, 73],
            'callback': self.printTest
        }]
        
        return [
            [ Score, {} ],
            testButton,
            testButton2,
            testButton3,
            testButton4
        ]
        
    def printTest(self):
        scoreModule = self.app.getModule('gameCounter')
        print('test: ' + str(scoreModule.counter))
