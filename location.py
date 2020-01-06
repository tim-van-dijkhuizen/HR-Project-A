class Location:
    
    section = None
    position = None
    
    def __init__(self, section, position):
        self.section = section
        self.position = position
        
    def __eq__(self, other): 
        if not isinstance(other, Location):
            return NotImplemented

        return self.section == other.section and self.position == other.position
