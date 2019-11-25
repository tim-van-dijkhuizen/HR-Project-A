from screen import Screen

class StartScreen(Screen):
    
    def getHandle(self):
        return 'start'
    
    def isDefault(self):
        return True
        
    def draw(self):
        background(0, 0, 255)
        fill(11, 60, 73)
        
        text('Press enter to start', 100, 100)
        
    def keyPressed(self):
        if keyCode == 10:
            gameScreen = self.app.getScreen('game')
            self.app.setCurrentScreen(gameScreen)
