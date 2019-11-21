from screen import Screen
from score import Score

class GameScreen(Screen):
        
    def getHandle(self):
        return 'game'
        
    def draw(self):
        background(0, 255, 0)
        fill(11, 60, 73)
        text('playerCount: ' + str(self.playerCount), 15, 15)
    
    def getSubModules(self):
        return [
            [Score, {}]    
        ]
