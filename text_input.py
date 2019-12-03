import utils
from clickable import Clickable

class TextInput(Clickable):

    # The current value of the input
    value = ''

    # Whether the input is focused
    focused = False

    def draw(self):
        if self.focused:
            fill(255, 235, 235)
        else:
            fill(255, 255, 255)
        
        rect(self.x, self.y, self.width, self.height)
        
        fill(0, 0, 0)
        textAlign(LEFT)
        textSize(15)
        
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
            else:
                self.value += str(key)
