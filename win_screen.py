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
        textAlign(CENTER)
        
        # Show text
        if self.isWinner:
            text('Gefeliciteerd, je hebt gewonnen!', width / 2, height / 2)
        else:
            text('Helaas, je hebt verloren!', width / 2, height / 2)
