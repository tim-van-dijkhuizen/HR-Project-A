from screen import Screen
from score import Score

class GameScreen(Screen):
        
    def getHandle(self):
        return 'game'
        
    def draw(self):
        background(0, 255, 0)
        fill(11, 60, 73)
        
        text('Press space to quit', 100, 100)
    
    def keyPressed(self):
        if keyCode == 32:
            startScreen = self.app.getScreen('start')
            self.app.setCurrentScreen(startScreen)
    
    def getSubModules(self):
        return [
            [Score, {}]    
        ]
