# Returns whether the mouse is colliding with the object
def collidesWith(objectX, objectY, objectWidth, objectHeight):
    return objectX < mouseX < objectX + objectWidth and objectY < mouseY < objectY + objectHeight
