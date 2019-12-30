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
        
    def botLocation(self):
        playerManager = self.app.getModule('playerManager')
        players = playerManager.getPlayers()
        bot = playerManager.botPlayer
        for player in players:
            if player == bot:
                botLocation = player.playerManager.getLocation()
        
    def Partner(self):        
        playerManager = self.app.getModule('playerManager')
        players = playerManager.getPlayers()
        bot = playerManager.botPlayer
        currentIndex = 0 if self.currentBot == None else players.index(self.currentBot)
        self.botPartner = currentIndex - 1 if bot % 2 == 0 else currentIndex + 1
        for player in players:
            if player == self.botPartner:
                player.playerManager.getLocation()

                    
        
        
        
