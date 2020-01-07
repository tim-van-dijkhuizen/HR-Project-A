import ui
from screen import Screen
from button import Button
from text_input import TextInput

class CardScreen(Screen):
    
    steps = None
    valid = True
    
    def getHandle(self):
        return 'card'
    
    def setup(self):
        # Set styling
        fill(ui.COLOR_TEXT)
        textSize(ui.TEXT_SIZE_XL)
        textAlign(LEFT)
        
    def draw(self):
        text('give the number from your card', 500, 225)
        
    def makingChoise(self):
        gameScreen = self.app.getScreen('game')
        self.app.setCurrentScreen(gameScreen)
        
    def isDisabled(self):
        if self.steps > 0 and self.steps < 4:
            self.valid = False
        else:
            self.valid = True
        return self.valid
        
    def setSteps(self, value):
        try: 
            self.steps = int(value)
            self.valid = True
        except ValueError:
            self.valid = False
                        
    def getSubModules(self):
        
        cardButton = [Button,  {
            'x': 700,
            'y': 300,
            'width': 50,
            'height': 50,
            'callback': self.makingChoise,
            'disabled': self.isDisabled
        }]
        
        nameInput = [TextInput,  {
            'x': 500,
            'y': 300,
            'width': 200,
            'height': 50,
            'callback': self.setSteps
        }]
        
        return [
            cardButton,
            nameInput
            ]
    
