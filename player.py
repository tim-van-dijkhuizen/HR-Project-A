from module import Module

class Player(Module):
    
    index = None
    image = None
    teamNumber = None
    
    _location = None
    _oldLocation = None
    
    _partner = None
    _team = None
    
    def isActive(self):
        playerManager = self.app.getModule('playerManager')
        players = playerManager.getAllPlayers()
        
        # Return false if module not active
        if not Module.isActive(self):
            return False
        
        return (self.index + 1) <= playerManager.maxPlayers
    
    # Returns whether the player is playing
    def isPlaying(self):
        team = self.getTeam()
        return self.isActive() and team.isPlaying
    
    # Returns the location
    def getLocation(self):
        return self._location
    
    # Returns the previous location
    def getOldLocation(self):
        return self._oldLocation
    
    # Sets the location and saves the old location
    def setLocation(self, location):
        gameManager = self.app.getModule('gameManager')
        screen = self.app.getCurrentScreen()
        
        # Update location
        self._oldLocation = self._location
        self._location = location
        
        # Check for win/lose
        if screen != None and screen.getHandle() != 'location':
            gameManager.checkWinLose()
            gameManager.checkGoodCard(self)
            gameManager.checkBadCard(self)
            gameManager.checkBreakpoint(self)
        
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
    
    # Returns the team object of this player
    def getTeam(self):
        playerManager = self.app.getModule('playerManager')
        
        # Find it if not cached yet
        if self._team == None:
            self._team = playerManager.getTeamByNumber(self.teamNumber)
            
        return self._team
