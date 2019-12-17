from module import Module

class DiceManager(Module):
    
    diceImageOne = None
    diceImageTwo = None
    diceImageThree = None
    diceImageFour = None
    diceImageFive = None
    diceImageSix = None
    
    diceValue = 0
    
    def setup(self):
        self.diceImageOne = loadImage("dice1.png")
        self.diceImageTwo = loadImage("dice2.png")
        self.diceImageThree = loadImage("dice3.png")
        self.diceImageFour = loadImage("dice4.png")
        self.diceImageFive = loadImage("dice5.png")
        self.diceImageSix = loadImage("dice6.png")
                     
    def getHandle(self):
       return 'diceManager'
        
    def mousePressed(self): 
        self.diceValue = int(random(1, 7))
        
