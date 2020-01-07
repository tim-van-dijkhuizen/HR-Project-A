import ui
from module import Module
from button import Button
from selectable_button import SelectableButton

class PlayerButton(Module):

    # Constants
    width = 160
    height = 80
    
    # Settings
    x = 0
    y = 0
    readOnly = False
    reverseAlignment = False
    
    # Position
    _imageBoxWidth = None
    _buttonBoxWidth = None
    _imageBoxX = None
    _buttonBoxX = None

    # The player which this button belongs to
    player = None
    
    def isActive(self):
        return self.player.isActive()
    
    def setup(self):
        if self.player == None:
            raise ValueError('player must be set')
            
        # Calc widths
        self._imageBoxWidth = (self.width / 6) * 3
        self._buttonBoxWidth = self.width / 6 * 3
        
        if self.reverseAlignment:
            self._buttonBoxX = self.x
            self._imageBoxX = self.x + self._buttonBoxWidth
        else:
            self._buttonBoxX = self.x + self._imageBoxWidth
            self._imageBoxX = self.x
        
    def draw(self):
        imageLoader = self.app.getModule('imageLoader')
        
        fill(ui.COLOR_WHITE)
        rect(self._imageBoxX, self.y, self._imageBoxWidth, self.height)
        
        playerImage = imageLoader.get(self.player.image)
        imageSize = self._imageBoxWidth - ui.SPACING_SM
        image(playerImage, (self._imageBoxX + self._imageBoxWidth / 2) - imageSize / 2, (self.y + self.height / 2) - imageSize / 2, imageSize, imageSize)
    
    def changeLocation(self):
        locationScreen = self.app.getScreen('location')
        
        locationScreen.fromScreen = self.parent
        locationScreen.player = self.player
        self.app.setCurrentScreen(locationScreen)
    
    def selectBot(self):
        playerManager = self.app.getModule('playerManager')
        playerManager.botPlayer = self.player
    
    def getSubModules(self):
        locationButton = [Button,  {
            'x': self._buttonBoxX,
            'y': self.y,
            'width': self._buttonBoxWidth,
            'height': self.height / 2,
            'text': 'Locatie',
            'callback': self.changeLocation
        }]
        
        botButton = [SelectableButton,  {
            'x': self._buttonBoxX,
            'y': self.y + self.height / 2,
            'width': self._buttonBoxWidth,
            'height': self.height / 2,
            'text': 'BOT',
            'group': 'botSelect',
            'selectedColor': ui.COLOR_RED_DARK,
            'onSelect': self.selectBot,
            'readOnly': self.readOnly
        }]
        
        return [
            locationButton,
            botButton
        ]
