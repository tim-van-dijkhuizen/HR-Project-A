import ui
import utils
from clickable import Clickable

class TextInput(Clickable):

    # Max value length
    maxLength = None

    # The current value of the input
    value = ''

    # Whether the input is focused
    focused = False
    
    # Callback for when the value changes
    callback = None

    def draw(self):
        if self.focused:
            fill(ui.COLOR_GRAY_LIGHT)
        else:
            fill(ui.COLOR_WHITE)
        
        rect(self.x, self.y, self.width, self.height)
        
        fill(ui.COLOR_TEXT)
        textAlign(LEFT)
        textSize(ui.TEXT_SIZE_SM)
        
        textOffset = self.height / 2 + textAscent() / 2
        text(self.value, self.x + textOffset, self.y + textOffset)

    def mousePressed(self):
        if utils.collidesWith(self.x, self.y, self.width, self.height):
            self.focused = True
        elif self.focused:
            self.focused = False

    def keyPressed(self):
        if self.focused:
            if keyCode == 8:
                self.value = self.value[0:-1] 
            elif self.maxLength == None or len(self.value) < self.maxLength:
                self.value += str(key)
                
            if self.callback != None:
                self.callback(self.value)
