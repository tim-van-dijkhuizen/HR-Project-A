import ui
from screen import Screen

class WinScreen(Screen):
    
    isWinner = True
    
    def getHandle(self):
        return 'win'
    
    def draw(self):
        # Set styling
        fill(ui.COLOR_TEXT)
        textSize(ui.TEXT_SIZE_XL)
        textAlign(LEFT)
        
        if self.isWinner:
            text('Gefeliciteerd, je hebt gewonnen!', 600, 300)
        else:
            text('Helaas, je hebt verloren!', 600, 550)
