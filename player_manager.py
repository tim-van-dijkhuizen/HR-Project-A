from module import Module
from player import Player

class PlayerManager(Module):
    
    # The max amount of players
    maxPlayers = None
    
    # The current bot player
    botPlayer = None
    
    # List containing all player objects
    _players = []
    _activePlayers = []
    
    def getHandle(self):
        return 'playerManager'
    
    def checkWinLose(self):
        playerManager = self.app.getModule('playerManager')
        for player in playerManager.getPlayers():
            if player.getLocation() == player.getPartner().getLocation() :
                if player.getLocation() == player.getPartner().getLocation() == 41 or player.getLocation() == player.getPartner().getLocation() == 85:
                    print ('lose')
                else :
                    print ('win')
                    gameOver = True
    
    def setup(self):
        imageLoader = self.app.getModule('imageLoader')
        
        # Load images
        imageLoader.load('pion-1')
        imageLoader.load('pion-2')
        imageLoader.load('pion-3')
        imageLoader.load('pion-4')
        imageLoader.load('pion-5')
        imageLoader.load('pion-6')
    
    def init(self):
        self._players = self.app.getModulesByType(Player)
        
        # Create active player list
        self.updateActiveList()
    
    def updateActiveList(self):
        self._activePlayers = list(filter(lambda p: p.isPlaying(), self._players))
    
    def setMaxPlayers(self, maxPlayers):
        self.maxPlayers = maxPlayers
        self.updateActiveList()
    
    def getPlayer(self, index):
        if index < 0 or index > (self.maxPlayers - 1):
            return None
        
        return self._players[index]
    
    def getPlayerByLocation(self, location):
        for player in self.getPlayers():
            if player.getLocation() == location:
                return player
            
        return None
    
    def getPlayers(self):
        return self._activePlayers
    
    def getAllPlayers(self):
        return self._players
    
    def getSubModules(self):
        modules = []
        
        # Create 6 players
        for i in range(6):
            imageFile = 'pion-' + str(i + 1)
            modules.append([Player, { 'index': i, 'image': imageFile }])
            
        return modules
    
