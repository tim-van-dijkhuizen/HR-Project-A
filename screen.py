from module import Module

class Screen(Module):
    
    # Returns the handle of this screen
    def getHandle(self): raise NotImplementedError
    
    # Returns whether this is the default screen
    def isDefault(self): return False
    
    # Returns true if this screen is the current screen
    # or if there is no current and this is the default.
    def isActive(self):
        screen = self.getCurrentScreen()
        
        # No screen, return if this is the default
        if screen == None:
            return self.isDefault()
        
        # Return whether the current screen handle matches
        # the handle of this screen.
        return screen.getHandle() == self.getHandle()
