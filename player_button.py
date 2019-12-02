from clickable import Clickable

class PlayerButton(Clickable):

    # Button properties
    color = [255, 255, 255]
    text = ''
    textSize = 15
    textColor = [0, 0, 0]
        
    def draw(self):        
        # Create rectangle
        fill(self.color[0], self.color[1], self.color[2])
        rect(self.x, self.y, self.width, self.height)
        
        # Create text
        textSize(self.textSize);
        textAlign(CENTER);
        fill(self.textColor[0], self.textColor[1], self.textColor[2])
        text(self.text, self.x + self.width / 2, self.y + self.height / 2 + self.height / 12)
