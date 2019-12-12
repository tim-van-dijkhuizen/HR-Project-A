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
        locationScreen = self.app.getScreen('location')
        player = locationScreen.player
        circleSize = self.width / 2
        
        # Set color
        fill(255, 22, 84)
        
        # Show if selected
        if player.getLocation() == self.location:
            circle(self.x + circleSize, self.y + circleSize, circleSize)
                  
    def callback(self):
        locationScreen = self.app.getScreen('location')
        
        player = locationScreen.player
        player.setLocation(self.location)
