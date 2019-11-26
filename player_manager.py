from module import Module
from player import Player

class PlayerManager(Module):
    
    maxPlayers = None
    players = []
    
    def getHandle(self):
        return 'playerManager'
    
    def setup(self):
        self.updateList()
    
    def setMaxPlayers(self, maxPlayers):
        self.maxPlayers = maxPlayers
        self.updateList()
    
    def updateList(self):
        currentPlayers = len(self.players)
        
        # Slice list if its to big
        if currentPlayers > self.maxPlayers:
            self.players = self.players[0:self.maxPlayers]
            
        # Add players if we need more
        if currentPlayers < self.maxPlayers:
            toAdd = self.maxPlayers - currentPlayers
            
            for i in range(toAdd):
                self.players.append(Player())
        
        if self.app.devMode:
            print('Max players:', self.maxPlayers)
            print('Updated players:', self.players)
    
    def getPlayer(self, index):
        if index < 0 or index > (self.maxPlayers - 1):
            return None
        
        return self.players[index]
