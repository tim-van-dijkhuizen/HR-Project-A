from clickable import Clickable

class LocationButton(Clickable):
    
    location = None
    
    def getPriority(self):
        return 2
    
    def setup(self):
        if self.location == None:
            raise ValueError('Location must be set')
            
    def callback(self):
        playerManager = self.app.getModule('playerManager')
        locationScreen = self.app.getScreen('location')
        
        player = locationScreen.player
        player.location = self.location
