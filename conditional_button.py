import utils
from button import Button

class ConditionalButton(Button):
    
    condition = None
    
    def setup(self):
        if self.condition == None:
            raise NotImplementedError('condition not set')
    
    def isActive(self):
        if not Button.isActive(self):
            return False
        
        return utils.parseValue(self.condition)
