def setup(): 
    global a, font , score, img
    size(1200, 650)
    textSize(150)
    font = createFont("Segoe script",  60) 
    score = 0
    
def draw(): 
    global message, img, font
    background(255, 74, 113)
    textFont(font)
    textAlign(CENTER)
    fill(0)
    text('Congratulations you won !', 600, 300)
    
    fontt = createFont('Arial Black', 35)
    textFont(fontt)
    textSize(35)
    text('Thanks for playing our game !', 600, 550)
