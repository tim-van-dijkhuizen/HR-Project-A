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
        imageLoader = self.app.getModule('imageLoader')
        
        # Load images
        imageLoader.load('pion-1')
        imageLoader.load('pion-2')
        imageLoader.load('pion-3')
        imageLoader.load('pion-4')
        imageLoader.load('pion-5')
        imageLoader.load('pion-6')       
            
    def nextPlayer(self):
        playerManager = self.app.getModule('playerManager')
        imageLoader = self.app.getModule('imageLoader')
        players = playerManager.getPlayers()
        currentIndex = 0 if self.currentPlayer == None else players.index(self.currentPlayer)
        nextIndex = currentIndex + 1
        image(imageLoader.get('pion-' + str(nextIndex)), 300 , 50 , 50, 50)
        
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
