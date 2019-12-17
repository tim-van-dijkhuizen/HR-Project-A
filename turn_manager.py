import ui
from module import Module
from button import Button

class TurnManager(Module):
    
    # All active players
    currentPlayer = None
    
    def getHandle(self):
        return 'turnManager'
    
    def setup(self):
        playerManager = self.app.getModule('playerManager')            
            
    def nextPlayer(self):
        playerManager = self.app.getModule('playerManager')
        players = playerManager.getPlayers()
        currentIndex = 0 if self.currentPlayer == None else players.index(self.currentPlayer)
        nextIndex = currentIndex + 1
        
        #reset index if max players exceeded
        if nextIndex >= len(players):
            nextIndex = 0
            
        self.currentPlayer = playerManager.getPlayer(nextIndex)
        
    def getSubModules(self):
        modules = []
        turnManager = self.app.getModule('turnManager')
        
        modules.append([Button, {
            'x': 60,
            'y': 70,
            'width': 200,
            'height': 50,
            'textSize': ui.TEXT_SIZE_MD,  
            'text': 'Next',
            'callback': turnManager.nextPlayer
        }])
        
        return modules
