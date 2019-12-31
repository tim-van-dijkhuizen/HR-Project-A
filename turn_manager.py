import ui
from module import Module
from button import Button

class TurnManager(Module):
    
    # All active players
    currentPlayer = None
    nextPicture = 1
    
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
        
    def draw(self):
        imageLoader = self.app.getModule('imageLoader')
        image(imageLoader.get('pion-' + str(self.nextPicture)), 300 , 50 , 50, 50)
            
    def nextPlayer(self):
        playerManager = self.app.getModule('playerManager')
        
        players = playerManager.getPlayers()
        currentIndex = 0 if self.currentPlayer == None else players.index(self.currentPlayer)
        nextIndex = currentIndex + 1
        self.nextPicture = self.nextPicture + 1
        
        # hier geeft die aan welke picture nu aan de beurt is
        if self.nextPicture == len(players):
            self.nextPicture = len(players)
        elif self.nextPicture > len(players):
            self.nextPicture = 1
        
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
