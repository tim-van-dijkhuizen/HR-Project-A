from component import Component

class Module(Component):

    # Main app object
    app = None

    # Handle of this module
    handle = None
    
    # Priority of the module
    # Higher priorities will be triggered later
    priority = 1

    # The parent module of this module.
    # This attribute will be set automatically.
    parent = None
    
    # Returns whether this module and its
    # potential parent is active.
    def getIsActive(self):
        parent = self.parent
        
        # Return false if the parent is disabled
        if parent != None and not parent.getIsActive():
            return False
        
        # Return own active state
        return self.isActive()
    
    # Returns the top-level parent
    def getTopLevelParent(self):
        parent = self.parent
        
        # Return if we've got no parent
        if parent == None:
            return self
        
        return parent.getTopLevelParent()
    
    # Returns a sub-module by its type
    def getSubModulesByType(self, type):
        return [ i for i in self.app.getModulesByParent(self) if isinstance(i, type) ]
    
    # Optional functions
    # ==========================================================
    
    def getHandle(self): return self.handle
    def getPriority(self): return self.priority
    
    # Override this to decide whether the module is active.
    # Disabled modules won't be visible/interactive.
    def isActive(self): return True
    
    # Override this to provide a list of child (sub) modules.
    # Keep in mind that these will be inactive if their parent is.
    def getSubModules(self): return []
    
    # Called after the module and its subModules have been loaded
    def init(self): pass
    
    # Called after all modules are loaded
    def afterLoadModules(self): pass
    
    # Called on draw
    def draw(self): pass
    
    # Called on mousePressed
    def mousePressed(self): pass
    
    # Called on keyPressed
    def keyPressed(self): pass
    
    # Called on keyReleased
    def keyReleased(self): pass
    
    # Called on mouseMoved
    def mouseMoved(self): pass
    
