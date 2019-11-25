from app import App
from modules import modules as moduleList

app = None

# Bootstrap
# ==========================================================

def setup():
    global app
    
    # Configure program
    size(500, 500)
    
    # Create app
    app = App({ 'devMode': True })
    
    # Register modules inside App
    for module in moduleList:
        app.registerModule(module[0], module[1])
    
def draw():
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
