import ui
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
        playerManager = self.app.getModule('playerManager')
        screen = self.app.getCurrentScreen()
        circleSize = self.width / 2
        
        fill(0, 0, 0, 0)
        rect(self.x, self.y, self.width, self.height)
        
        # Set color
        fill(ui.COLOR_RED_DARK)
        
        # Check if the LocationScreen is active
        if screen != None and screen.getHandle() == 'location':
            player = screen.player
        
            # Show circle if selected
            if player.getLocation() == self.location:
                circle(self.x + circleSize, self.y + circleSize, circleSize)
        else:
            player = playerManager.getPlayerByLocation(self.location)
            
            if player != None:
                text('Player: ' + player.name, self.x, self.y)
                  
    def callback(self):
        locationScreen = self.app.getScreen('location')
        
        player = locationScreen.player
        player.setLocation(self.location)
