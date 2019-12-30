from module import Module

class BotManager(Module):
    
    currentBot = None
    
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
        
        
    def botBuddy(self):
        # turnManager = self.app.getModule('turnManager')
        # playerManager = self.app.getModule('playerManager')
        # bot = playerManager.botPlayer
        # players = playerManager.getPlayers()
        # botPlayer = None if bot == None else players.index(self.Bot)
        # botBuddy = botPlayer - 1 if bot % botPlayer == 0 else botPlayer + 1
        
        playerManager = self.app.getModule('playerManager')
        players = playerManager.getPlayers()
        currentIndex = 0 if self.currentBot == None else players.index(self.currentBot)
        evenIndex = currentIndex % 2 == 0
        oddIndex = currentIndex % 2 == 1
                    
        #reset index if max players exceeded
        if nextIndex >= len(players):
            nextIndex = 0
            
        self.currentPlayer = playerManager.getPlayer(nextIndex)
        
        
        
