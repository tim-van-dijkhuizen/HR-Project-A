from module import Module

class Player(Module):
    
    name = None
    bot = False
    
    _location = None
    _oldLocation = None
    
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
