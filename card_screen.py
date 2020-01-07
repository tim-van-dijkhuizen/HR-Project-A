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
        print(self.steps)
                
    def getSubModules(self):
        
        cardButton = [Button,  {
            'x': 725,
            'y': 325,
            'width': 50,
            'height': 50,
            'text': 'Number',
            'callback': self.makingChoise,
            'disabled': self.isDisabled
        }]
        
        nameInput = [TextInput,  {
            'x': 500,
            'y': 325,
            'width': 200,
            'height': 50,
            'callback': self.setSteps
        }]
        
        return [
            cardButton,
            nameInput
            ]
    
