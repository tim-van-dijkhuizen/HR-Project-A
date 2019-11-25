from module import Module

class Score(Module):
    
    counter = 0
    
    def draw(self):
        self.counter += 1
        text('Score: ' + str(self.counter), 20, 20)
        
    def getHandle(self):
        return 'gameCounter'
