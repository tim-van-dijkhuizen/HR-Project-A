from component import Component
from screen import Screen

class App(Component):
    
    # Globals
    # ==========================================================
    
    # Whether development mode should be enabled.
    # Development mode add debugging tools
    devMode = False
    
    # All registered module objects
    modules = []
    
    # All registered screens handle -> instance
    screens = {}
    
    # Current screen
    currentScreen = None
    
    # Functions
    # ==========================================================
    
    # Returns a Screen by its handle
    def getScreen(self, handle):
        return self.screens[handle]
    
    # Returns the currently active screen
    def getCurrentScreen(self):
        return self.currentScreen
            
    # Sets the current screen
    def setCurrentScreen(self, screen):
        self.currentScreen = screen
    
    # Registers a module and its sub-modules.
    # Also returns the instance of the newly created module.
    def registerModule(self, module, config):
        config['app'] = self
        
        # Create and register module
        instance = module(config)
        self.modules.append(instance)
        
        # Add to screens if its a Screen
        if isinstance(instance, Screen):
            self.screens[instance.getHandle()] = instance
    
        # Register sub-modules
        for subModule in instance.getSubModules():
            subModule[1]['parent'] = instance
            self.registerModule(subModule[0], subModule[1])
        
        # Print message if devMode is enabled
        if self.devMode:
            print('Registered module: ' + str(instance))
            
        return instance
