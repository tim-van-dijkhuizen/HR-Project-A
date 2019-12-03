import utils
from clickable import Clickable

class TextInput(Clickable):

    # The current value of the input
    value = ''

    # Whether the input is focused
    _focused = False

    def mousePressed(self):
        if utils.collidesWith(self.x, self.y, self.width, self.height):
            self._focused = True
        elif self._focused:
            self._focused = False

    def keyPressed():
        if self._focused:
            if keyCode == 8:
                self.value = self.value[0:-1] 
            else:
                self.value += key
