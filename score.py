from module import Module

class Score(Module):
    
    counter = 0
    
    def setup(self):
        global counter
        
        counter = 0
    
    def draw(self):
        global counter
        
        counter += 1
        text('Score: ' + str(counter), 20, 20)
