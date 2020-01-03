from module import Module

class BotManager(Module):
    
    currentBot = None
    botPartner = None
    diceValue = None
    currentPlayer = None
    
    def getHandle(self):
        return 'botManager'
    
    def setup(self):
        playerManager = self.app.getModule('playerManager')
        
    def draw(self):
        playerManager = self.app.getModule('playerManager')
        
    def autoBot(self):
        playerManager = self.app.getModule('playerManager')
        botManager = self.app.getModule('botManager')
        turnManager = self.app.getModule('turnManager')
        
        self.diceValue = int(random(1, 7))
        steps = self.diceValue
        botLocatie = playerManager.botPlayer.getLocation()
        currentPlayer = turnManager.currentPlayer
        partner = playerManager.botPlayer.getPartner()

        if botLocatie > partner.getLocation():
            botLocation = int(botLocatie) - steps
            newLocation = playerManager.botPlayer.setLocation(botLocation)
        elif botLocatie == partner.getLocation():
            gameOver = True
        else:
            botLocation = steps + int(botLocatie)
            newLocation = playerManager.botPlayer.setLocation(botLocation)
            
    def partnerLocation(self):        
        playerManager = self.app.getModule('playerManager')
        partnerLocation = self.botPartner.getLocation()
        return partnerLocation
    
