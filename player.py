from module import Module

class Player(Module):
    
    index = None
    image = None
    teamNumber = None
    
    _location = None
    _oldLocation = None
    
    _partner = None

    # Returns whether the player is playing
    def isPlaying(self):
        playerManager = self.app.getModule('playerManager')
        players = playerManager.getAllPlayers()
        index = players.index(self) + 1
        
        return index <= playerManager.maxPlayers
    
    # Returns the location
    def getLocation(self):
        return self._location
    
    # Returns the previous location
    def getOldLocation(self):
        return self._oldLocation
    
    # Sets the location and saves the old location
    def setLocation(self, location):
        self._oldLocation = self._location
        self._location = location
        
    # Returns whether this player is the bot
    def isBot(self):
        playerManager = self.app.getModule('playerManager')
        return playerManager.botPlayer is self
    
    # Returns the partner of this player
    def getPartner(self):
        playerManager = self.app.getModule('playerManager')
        
        # Find partner if not cached yet
        if self._partner == None:
            partnerIndex = (self.index + 1) if self.index % 2 == 0 else (self.index - 1)
            self._partner = playerManager.getPlayer(partnerIndex)
        
        return self._partner
