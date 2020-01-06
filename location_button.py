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
        imageLoader = self.app.getModule('imageLoader')
        screen = self.app.getCurrentScreen()
        circleSize = self.width / 2
        
        fill(0, 0, 0, 0)
        rect(self.x, self.y, self.width, self.height)
        
        # Set color
        fill(ui.COLOR_RED_DARK)
        
        # Check if we're in the LocationScreen context
        if screen != None and screen.getHandle() == 'location':
            player = screen.player
        
            # Show circle if selected
            if player.getLocation() == self.location:
                circle(self.x + circleSize, self.y + circleSize, circleSize)
        else:
            players = playerManager.getPlayersByLocation(self.location)
            
            # Show images for players
            for player in players:
                playerImage = imageLoader.get(player.image)
                
                imageWidth = self.width - 4
                imageHeight = self.height - 4
                imageOffsetX = (self.x + self.width / 2) - imageWidth / 2
                imageOffsetY = (self.y + self.height / 2) - imageHeight / 2
                
                image(playerImage, imageOffsetX, imageOffsetY, imageWidth, imageHeight)
                  
    def callback(self):
        screen = self.app.getCurrentScreen()
        
        # Check if we're in the LocationScreen context
        if screen != None and screen.getHandle() == 'location':
            player = screen.player
            player.setLocation(self.location)
