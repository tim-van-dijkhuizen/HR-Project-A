def setup(): 
    global a, font, 
    size(1200, 650)
    textSize(150)
    font = createFont("Segoe script",  60) 
    
def draw(): 
    global message, font
    background(255, 74, 113)
    textFont(font)
    textAlign(CENTER)
    fill(0)
    text('Congratulations you won !', 600, 300)
    
    font = createFont('Arial Black', 35)
    textFont(fontt)
    textSize(35)
    text('Thanks for playing our game !', 600, 550)
