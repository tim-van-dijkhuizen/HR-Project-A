class Module:

    # Screen management functions from main file
    getScreenFunction = None
    getCurrentScreenFunction = None
    setCurrentScreenFunction = None

    # Init
    def __init__(self, getScreenFunction, getCurrentScreenFunction, setCurrentScreenFunction):
        self.getScreenFunction = getScreenFunction
        self.getCurrentScreenFunction = getCurrentScreenFunction
        self.setCurrentScreenFunction = setCurrentScreenFunction

    # The parent module of this module.
    # This attribute will be set automatically.
    parent = None

    # Sets all attributes from the config
    # and calls setup().
    def init(self, config):
        for attribute, value in config.items():
            setattr(self, attribute, value)
    
        self.setup()
    
    # Returns whether this module and its
    # potential parent is active.
    def getIsActive(self):
        parent = self.parent
        
        # Return false if the parent is disabled
        if parent != None and not parent.getIsActive():
            return False
        
        # Return own active state
        return self.isActive()
    
    # Get a screen by its handle
    def getScreen(self, handle):
        return self.getScreenFunction(handle)
    
    # Returns the currently active screen
    def getCurrentScreen(self):
        return self.getCurrentScreenFunction()
    
    # Sets the currently active screen
    def setCurrentScreen(self, screen):
        return self.setCurrentScreenFunction(screen)
    
    # Optional functions
    # ==========================================================
    
    # Override this to decide whether the module is active.
    # Disabled modules won't be visible/interactive.
    def isActive(self): return True
    
    # Override this to provide a list of child (sub) modules.
    # Keep in mind that these will be inactive if their parent is.
    def getSubModules(self): return []
    
    # Called on setup
    def setup(self): pass
    
    # Called on draw
    def draw(self): pass
    
    # Called on mousePressed
    def mousePressed(self): pass
    
    # Called on keyPressed
    def keyPressed(self): pass
    
    # Called on keyReleased
    def keyReleased(self): pass
