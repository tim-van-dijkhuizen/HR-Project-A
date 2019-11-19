from module import Module
from score import Score

class Game(Module):
        
    def draw(self):
        fill(11, 60, 73)
        text('playerCount: ' + str(self.playerCount), 15, 15)
        
    def isActive(self):
        return True
    
    def getSubModules(self):
        return [
            [Score, {}]    
        ]
