from module import Module

class Player(Module):
    
    index = None
    image = None
    
    _location = None
    _oldLocation = None
    
    _partner = None
    
    def isPlaying(self):
        playerManager = self.app.getModule('playerManager')
        players = playerManager.getAllPlayers()
        index = players.index(self) + 1
        
        return index <= playerManager.maxPlayers
    
    def getLocation(self):
        return self._location
    
    def getOldLocation(self):
        return self._oldLocation
    
    def setLocation(self, location):
        self._oldLocation = self._location
        self._location = location
        
    def isBot(self):
        playerManager = self.app.getModule('playerManager')
        return playerManager.botPlayer is self
    
    def getPartner(self):
        playerManager = self.app.getModule('playerManager')
        
        # Find partner if not cached yet
        if self._partner == None:
            partnerIndex = (self.index + 1) if self.index % 2 == 0 else (self.index - 1)
            self._partner = playerManager.getPlayer(partnerIndex)
        
        return self._partner
