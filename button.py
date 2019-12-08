import utils
from clickable import Clickable

class Button(Clickable):

    # Button properties
    color = [255, 255, 255]
    text = ''
    textSize = 15
    textColor = [0, 0, 0]
    disabled = False
        
    def draw(self):
        color = utils.colorGrayscale(self.color) if utils.parseValue(self.disabled) else self.color
                
        # Create rectangle
        fill(color[0], color[1], color[2])
        rect(self.x, self.y, self.width, self.height)
        
        # Create text
        textSize(self.textSize);
        textAlign(CENTER);
        fill(self.textColor[0], self.textColor[1], self.textColor[2])
        text(self.text, self.x + self.width / 2, self.y + self.height / 2 + self.height / 12)
        
    def mousePressed(self):
        # Cancel click if disabled
        if not utils.parseValue(self.disabled):
            Clickable.mousePressed(self)
        
        
