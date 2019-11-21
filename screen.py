from module import Module

class Screen(Module):
    
    def getHandle(self): raise NotImplementedError
    def isDefault(self): return False
    
    def isActive(self):
        screen = self.getCurrentScreen()
        
        if screen == None:
            return self.isDefault()
        
        return screen.getHandle() == self.getHandle()
