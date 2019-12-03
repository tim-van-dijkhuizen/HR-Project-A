from module import Module
from button import Button
from selectable_button import SelectableButton

class PlayerButton(Module):

    # Constants
    width = 250
    height = 100

    # Position
    x = 0
    y = 0

    # The player which this button belongs to
    player = None
    
    def setup(self):
        if self.player == None:
            raise ValueError('player must be set')
        
    def draw(self):        
        fill(255, 74, 113)
        rect(self.x, self.y, self.width, self.height)
        
    def changeLocation(self):
        locationScreen = self.app.getScreen('location')
        
        locationScreen.fromScreen = self.parent
        locationScreen.player = self.player
        self.app.setCurrentScreen(locationScreen)
    
    def getSubModules(self):
        locationButton = [Button,  {
            'x': self.x,
            'y': self.y + self.height / 2,
            'width': self.width / 2,
            'height': self.height / 2,
            'color': [255, 74, 113],
            'text': 'Locatie',
            'callback': self.changeLocation
        }]
        
        botButton = [SelectableButton,  {
            'x': self.x + self.width / 2,
            'y': self.y + self.height / 2,
            'width': self.width / 2,
            'height': self.height / 2,
            'color': [255, 74, 113],
            'text': 'BOT',
            'group': 'botSelect',
            'selectedColor': [255, 22, 84]
        }]
        
        return [
            locationButton,
            botButton
        ]
