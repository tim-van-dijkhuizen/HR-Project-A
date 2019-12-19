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
    
    _originalReadOnly = None
    
    def draw(self):
        disabled = utils.parseValue(self.disabled)
    
        # Set read-only value
        if disabled and not self.readOnly:
            self._originalReadOnly = self.readOnly
            self.readOnly = True
        elif not disabled and self._originalReadOnly != None and self.readOnly != self._originalReadOnly:
            self.readOnly = self._originalReadOnly
        
        # Determine color
        color = utils.colorGrayscale(self.color) if disabled else self.color
                
        # Create rectangle
        fill(color)
        rect(self.x, self.y, self.width, self.height)
        
        # Create text
        textSize(self.textSize);
        textAlign(CENTER);
        fill(self.textColor)
        text(self.text, self.x + self.width / 2, self.y + self.height / 2 + self.textSize / 2 - 2)
        
        
