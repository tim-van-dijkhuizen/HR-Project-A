from module import Module

class Button(Module):
    
    # Handle of this button module
    handle = None
    
    # Button properties
    x = None
    y = None
    width = None
    height = None
    color = None
    text = None
    textColor = None
    callback = None
        
    def draw(self):
        textSize(15);
        textAlign(CENTER);
        
        # Create rectangle
        fill(self.color[0], self.color[1], self.color[2])
        rect(self.x, self.y, self.width, self.height)
        
        # Create text
        fill(self.textColor[0], self.textColor[1], self.textColor[2])
        textSize(self.width / 6);
        text(self.text, self.x + self.width / 2, self.y + self.height / 2 + self.height / 12)
        
    def mousePressed(self):
        if self.collidesWith(self.x, self.y, self.width, self.height) and self.callback != None:
            self.callback()
        
    # Returns whether the mouse is colliding with the object
    def collidesWith(self, objectX, objectY, objectWidth, objectHeight):
        return objectX < mouseX < objectX + objectWidth and objectY < mouseY < objectY + objectHeight
    
    def getHandle(self):
        return self.handle
        
        
