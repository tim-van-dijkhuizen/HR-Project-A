from module import Module

class BotManager(Module):
    
    diceValue = None
    
    def getHandle(self):
        return 'botManager'
    
    def setup(self):
        playerManager = self.app.getModule('playerManager')
        
    def draw(self):
        playerManager = self.app.getModule('playerManager')
        
    def rollDice(self):
        self.diceValue = random(1, 7)   
    
    def handleBotTurn(self):
        playerManager = self.app.getModule('playerManager')
        
        # Team players
        botPlayer = playerManager.botPlayer
        botPartner = botPlayer.getPartner()
        
        # Roll dice
        self.rollDice()
        steps = self.diceValue
        
        # Team locations
        botLocation = botPlayer.getLocation()
        partnerLocation = botPartner.getLocation()

        if botLocation > partnerLocation:
            botLocation = botLocation - steps
            botPlayer.setLocation(botLocation)
        else:
            botLocation = steps + botLocation
            botPlayer.setLocation(botLocation)
            
    #def _calcDistance(self, location1, location2, clockwise):
        # 88 132
        #if location1 > location2:
             
    
