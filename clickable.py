from module import Module
import utils

class Clickable(Module):
    
    x = 0
    y = 0
    width = 0
    height = 0
    callback = None
    readOnly = False
    
    _hovered = False

    def mouseMoved(self):
        readOnly = utils.parseValue(self.readOnly)
        
        if utils.collidesWith(self.x, self.y, self.width, self.height) and not readOnly:
            self._hovered = True
            cursor(HAND)
        elif self._hovered:
            self._hovered = False
            cursor(ARROW)
    
    def mousePressed(self):
        readOnly = utils.parseValue(self.readOnly)
        
        if utils.collidesWith(self.x, self.y, self.width, self.height) and not readOnly and self.callback != None:
            self.callback()
