from modules import modules as moduleList
from screen import Screen

# Globals
# ==========================================================

# Whether development mode should be enabled.
# Development mode add debugging tools
devMode = True

# All registered module objects
modules = []

# All registered screens handle -> instance
screens = {}

# Current screen
currentScreen = None

# Functions
# ==========================================================

# Returns a Screen by its handle
def getScreen(handle):
    return screens[handle]

# Returns the currently active screen
def getCurrentScreen():
    return currentScreen
        
# Sets the current screen
def setCurrentScreen(screen):
    global currentScreen
    currentScreen = screen

# Registers a module and its sub-modules
def registerModule(module, config):
    instance = module(getScreen, getCurrentScreen, setCurrentScreen)
    
    # Register module
    modules.append(instance)
    instance.init(config)
    
    # Add to screens if its a Screen
    if isinstance(instance, Screen):
        screens[instance.getHandle()] = instance

    # Register sub-modules
    for subModule in instance.getSubModules():
        subModule[1]['parent'] = instance
        registerModule(subModule[0], subModule[1])
    
    # Print message if devMode is enabled
    if devMode:
        print('Registered module: ' + str(instance))
    

# Program
# ==========================================================

def setup():
    global modules, activeScreen
    
    # Set app settings
    size(500, 500)
    
    # Register modules
    for module in moduleList:
        registerModule(module[0], module[1])
    
def draw():
    background(255, 253, 253)
    
    for module in modules:
        if module.getIsActive(): module.draw()
    
def mousePressed():
    for module in modules: 
        if module.getIsActive(): module.mousePressed()
    
def keyPressed():
    for module in modules: 
        if module.getIsActive(): module.keyPressed()
    
def keyReleased():
    for module in modules: 
        if module.getIsActive(): module.keyReleased()
