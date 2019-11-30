from module import Module
import utils

class Clickable(Module):
    
    x = 0
    y = 0
    width = 0
    height = 0
    callback = None
    
    def draw(self):
        if self.app.devMode:
            fill(0, 0, 0, 0.1)
            rect(self.x, self.y, self.width, self.height)

    
    def mousePressed(self):
        if utils.collidesWith(self.x, self.y, self.width, self.height) and self.callback != None:
            self.callback()
            
            if self.app.devMode:
                print('Clickable was clicked:', self)
