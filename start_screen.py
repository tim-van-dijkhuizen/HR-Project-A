from screen import Screen

class StartScreen(Screen):
    
    def getHandle(self):
        return 'start'
    
    def isDefault(self):
        return True
        
    def draw(self):
        background(0, 0, 255)
        
    def keyPressed(self):
        if keyCode == 10:
            gameScreen = self.getScreen('game')
            self.setCurrentScreen(gameScreen)
