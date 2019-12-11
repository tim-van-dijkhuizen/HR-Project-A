from module import Module

class DiceManager(Module):
    
    imgDice1 = None
    imgDice2 = None
    imgDice3 = None
    imgDice4 = None
    imgDice5 = None
    imgDice6 = None
    
    rand = 0
    value = 0
    
    def setup(self):
        self.imgDice1 = loadImage("dice1.png")
        self.imgDice2 = loadImage("dice2.png")
        self.imgDice3 = loadImage("dice3.png")
        self.imgDice4 = loadImage("dice4.png")
        self.imgDice5 = loadImage("dice5.png")
        self.imgDice6 = loadImage("dice6.png")
                     
    def getHandle(self):
       return 'diceManager'
   
    def rollDice(self):
        pass
        
    def mouseClicked(): 
        global value
        if value == 0:
            global rand
            rand = int(random(6)) + 1
        else:
            rand = int(random(6)) + 1
        
