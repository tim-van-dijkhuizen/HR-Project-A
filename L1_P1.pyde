from app import App
from modules import modules as moduleList

app = None

# Program
# ==========================================================

def setup():
    global app
    
    # Set app settings
    size(500, 500)
    
    # Register our app
    app = App({ 'devMode': True })
    
    # Register modules
    for module in moduleList:
        app.registerModule(module[0], module[1])
    
def draw():
    background(255, 253, 253)
    
    for module in app.modules:
        if module.getIsActive(): module.draw()
    
def mousePressed():
    for module in app.modules: 
        if module.getIsActive(): module.mousePressed()
    
def keyPressed():
    for module in app.modules: 
        if module.getIsActive(): module.keyPressed()
    
def keyReleased():
    for module in app.modules: 
        if module.getIsActive(): module.keyReleased()
