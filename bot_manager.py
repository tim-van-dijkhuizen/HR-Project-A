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
        
    def makingSteps(self):
        diceManager = self.app.getModule('diceManager')
        playerManager = self.app.getModule('playerManager')
        steps = diceManager.diceValue
        # er moet hier komen dat de bot naar zijn partner automatisch moet gaan
        if botLocation > partnerLocation:
            botLocation = steps + botLocation
        else:
            botLocation = steps - botLocation
        
    def botLocation(self):
        playerManager = self.app.getModule('playerManager')
        players = playerManager.getPlayers()
        botLocation = playerManager.botPlayer.getLocation()
        return botLocation

    def partner(self):        
        playerManager = self.app.getModule('playerManager')
        players = playerManager.getPlayers()
        bot = playerManager.botPlayer
        currentIndex = 0 if self.currentBot == None else players.index(self.currentBot)
        if bot % 2 == 0: 
            self.botPartner = currentIndex - 1
        else:
            self.botPartner = currentIndex + 1
        for player in players:
            if player == self.botPartner:
                partnerLocation = player.playerManager.getLocation()
                return partnerLocation


                    
        
        
        
