# Returns whether the mouse is colliding with the object
def collidesWith(objectX, objectY, objectWidth, objectHeight):
    return objectX < mouseX < objectX + objectWidth and objectY < mouseY < objectY + objectHeight

# Returns the grayscale version of a color
def colorGrayscale(color):
    r = color[0]
    g = color[1]
    b = color[2]
    
    # Get avarage
    avg = (r + g + b) / 3
    
    return [avg, avg, avg]

# Returns the value of the variable or function
def parseValue(var):
    return var() if callable(var) else var
