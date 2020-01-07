import ui
from screen import Screen
from button import Button
from text_input import TextInput

class CardScreen(Screen):
    
    cardType = None
    
    steps = None
    valid = False
    
    def getHandle(self):
        return 'card'

    def beforeShow(self):
        self.steps = None
        self.valid = False
        self.app.getModule('cardScreenInput').value = ''

    def draw(self):
        if self.cardType == None:
            raise NotImplementedError('cardType not set')
        
        # Set styling
        fill(ui.COLOR_TEXT)
        textSize(ui.TEXT_SIZE_MD)
        textAlign(CENTER)
        
        cardName = 'goede' if self.cardType == 'good' else 'slechte'
        pointName = 'plus' if self.cardType == 'good' else 'min'
        text('Pak een ' + cardName + ' kaart en vul het aantal ' + pointName + 'punten in', width / 2, height / 2 - ui.SPACING_SM)
        
    def goBack(self):
        gameScreen = self.app.getScreen('game')
        playerManager = self.app.getModule('playerManager')
        botManager = self.app.getModule('botManager')
        botPlayer = playerManager.botPlayer
        
        # Get locations
        botLocation = botPlayer.getLocation()
        partnerLocation = botPlayer.getPartner().getLocation()
        
        # Apply points
        clockwise = botManager.calcDistance(botLocation, partnerLocation, True)
        counterClockwise = botManager.calcDistance(botLocation, partnerLocation, False)
        
        if self.cardType == 'good':
            performClockwise = clockwise <= counterClockwise
        else:
            performClockwise = clockwise >= counterClockwise
        
        botManager.performSteps(self.steps, performClockwise)
        
        # Go back
        self.app.setCurrentScreen(gameScreen)
        
    def isDisabled(self):
        return not self.valid
        
    def setSteps(self, value):
        try: 
            self.steps = int(value)
            self.valid = True
        except ValueError:
            self.valid = False
                        
    def getSubModules(self):
        cardButton = [Button,  {
            'x': width / 2 - (80 + 120) / 2 + 120,
            'y': height / 2,
            'width': 80,
            'height': 50,
            'text': 'Klaar',
            'callback': self.goBack,
            'disabled': self.isDisabled
        }]
        
        nameInput = [TextInput,  {
            'handle': 'cardScreenInput',
            'x': width / 2 - (80 + 120) / 2,
            'y': height / 2,
            'width': 120,
            'height': 50,
            'callback': self.setSteps
        }]
        
        return [
            cardButton,
            nameInput
        ]
    
