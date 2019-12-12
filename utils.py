# Returns whether the mouse is colliding with the object
def collidesWith(objectX, objectY, objectWidth, objectHeight):
    return objectX < mouseX < objectX + objectWidth and objectY < mouseY < objectY + objectHeight

# Returns the grayscale version of a color
def colorGrayscale(inputColor):
    b =  inputColor & 255
    g = (inputColor >> 8) & 255
    r =   (inputColor >> 16) & 255
    
    # Get avarage
    avg = (r + g + b) / 3
    
    return color(avg, avg, avg)

# Returns the value of the variable or function
def parseValue(var):
    return var() if callable(var) else var
