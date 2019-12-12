import ui
import utils
from clickable import Clickable

class Button(Clickable):

    # Button properties
    color = ui.COLOR_BUTTON
    text = ''
    textSize = ui.TEXT_SIZE_SM
    textColor = ui.COLOR_TEXT
    disabled = False
        
    def draw(self):
        color = utils.colorGrayscale(self.color) if utils.parseValue(self.disabled) else self.color
                
        # Create rectangle
        fill(color)
        rect(self.x, self.y, self.width, self.height)
        
        # Create text
        textSize(self.textSize);
        textAlign(CENTER);
        fill(self.textColor)
        text(self.text, self.x + self.width / 2, self.y + self.height / 2 + self.textSize / 2 - 2)
        
    def mouseMoved(self):
        # Cancel hover if disabled
        if not utils.parseValue(self.disabled):
            Clickable.mouseMoved(self)
        
    def mousePressed(self):
        # Cancel click if disabled
        if not utils.parseValue(self.disabled):
            Clickable.mousePressed(self)
        
        
