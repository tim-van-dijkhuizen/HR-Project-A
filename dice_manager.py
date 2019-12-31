import ui
from module import Module
from button import Button

class DiceManager(Module):
    
    diceValue = None
    currentPlayer = None
    
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
        
    def diceNumber(self):
        playerManager = self.app.getModule('playerManager')
        botManager = self.app.getModule('botManager')
        turnManager = self.app.getModule('turnManager')
        
        self.diceValue = int(random(1, 7))
        steps = self.diceValue
        botLocatie = botManager.botLocation()
        currentPlayer = turnManager.currentPlayer
        partner = playerManager.botPlayer.getPartner()

        if botLocatie > partner.getLocation():
            botLocation = int(botLocatie) - steps
            newLocation = playerManager.botPlayer.setLocation(botLocation)
        elif botLocatie == partner.getLocation():
            print('Bot heeft gewonnen')
        else:
            botLocation = steps + int(botLocatie)
            newLocation = playerManager.botPlayer.setLocation(botLocation)
        
    def diceDisabled(self):
        playerManager = self.app.getModule('playerManager')
        turnManager = self.app.getModule('turnManager')
        bot = playerManager.botPlayer
        configInvalid = True
        
        if bot == turnManager.currentPlayer:
            configInvalid = False
        return configInvalid  
        
    def getSubModules(self):
        modules = []
        diceManager = self.app.getModule('diceManager')
        
        modules.append([Button, {
            'x': 1100,
            'y': 550,
            'width': 50,
            'height': 50,
            'textSize': ui.TEXT_SIZE_MD,  
            'text': '',
            'callback': diceManager.diceNumber,
            'disabled': diceManager.diceDisabled
        }])
        
        return modules
        
