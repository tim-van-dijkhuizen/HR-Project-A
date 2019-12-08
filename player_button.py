from module import Module
from button import Button
from selectable_button import SelectableButton
from text_input import TextInput

class PlayerButton(Module):

    # Constants
    width = 225
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
        
    def isActive(self):
        return self.player.isPlaying()
       
    def changeName(self, value):
       self.player.name = value     
    
    def changeLocation(self):
        locationScreen = self.app.getScreen('location')
        
        locationScreen.fromScreen = self.parent
        locationScreen.player = self.player
        self.app.setCurrentScreen(locationScreen)
    
    def selectBot(self):
        self.player.bot = True
        
    def deselectBot(self):
        self.player.bot = False
    
    def getSubModules(self):
        nameInput = [TextInput,  {
            'x': self.x,
            'y': self.y,
            'width': self.width,
            'height': self.height / 2,
            'maxLength': 18,
            'callback': self.changeName
        }]
        
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
            'x': self.x + self.width / 2 + 1,
            'y': self.y + self.height / 2,
            'width': self.width / 2,
            'height': self.height / 2,
            'color': [255, 74, 113],
            'text': 'BOT',
            'group': 'botSelect',
            'selectedColor': [255, 22, 84],
            'onSelect': self.selectBot,
            'onDeselect': self.deselectBot
        }]
        
        return [
            nameInput,
            locationButton,
            botButton
        ]
