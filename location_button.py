from clickable import Clickable

class LocationButton(Clickable):
    
    width = 25
    height = 25
    
    maxPlayers = None
    location = None
    
    def getPriority(self):
        return 2
    
    def isActive(self):
        playerManager = self.app.getModule('playerManager')
        return self.maxPlayers == playerManager.maxPlayers
    
    def setup(self):
        if self.maxPlayers == None or self.location == None:
            raise ValueError('Max players and location must be set')
         
    def draw(self):
        fill(0, 0, 0, 0)
        rect(self.x, self.y, self.width, self.height)
                  
    def callback(self):
        playerManager = self.app.getModule('playerManager')
        locationScreen = self.app.getScreen('location')
        
        player = locationScreen.player
        player.setLocation(self.location)
