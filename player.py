from component import Component

class Player(Component):
    
    name = None
    location = None
    bot = False
    
    def validate(self):
        return self.name != None and self.location != None and self.bot != None
