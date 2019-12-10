from module import Module

class Player(Module):
    
    name = None
    location = None
    bot = False
    
    def isPlaying(self):
        playerManager = self.app.getModule('playerManager')
        players = playerManager.getAllPlayers()
        index = players.index(self) + 1
        
        return index <= playerManager.maxPlayers
    
    def validate(self):
        return self.name != None and self.location != None and self.bot != None
