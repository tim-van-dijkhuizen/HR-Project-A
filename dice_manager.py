from module import Module

class DiceManager(Module):
    
    diceValue = 0
    
    def setup(self):
        imageLoader = self.app.getModule('imageLoader')
        
        imageLoader.load("dice1.png")
        imageLoader.load("dice2.png")
        imageLoader.load("dice3.png")
        imageLoader.load("dice4.png")
        imageLoader.load("dice5.png")
        imageLoader.load("dice6.png")
                     
    def getHandle(self):
       return 'diceManager'
        
    def mousePressed(self): 
        self.diceValue = int(random(1, 7))
        
