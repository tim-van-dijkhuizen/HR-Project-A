from module import Module

class BotManager(Module):
    
    currentBot = None
    botPartner = None
    
    def getHandle(self):
        return 'botManager'
    
    def setup(self):
        playerManager = self.app.getModule('playerManager')
        
    def draw(self):
        playerManager = self.app.getModule('playerManager')
        
    def botLocation(self):
        playerManager = self.app.getModule('playerManager')
        botLocation = playerManager.botPlayer.getLocation()
        return botLocation
            
    def partnerLocation(self):        
        playerManager = self.app.getModule('playerManager')
        partnerLocation = self.botPartner.getLocation()
        return partnerLocation
    
