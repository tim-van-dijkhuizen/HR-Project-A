import ui
from screen import Screen
from button import Button
from selectable_button import SelectableButton
from player_button import PlayerButton

class StartScreen(Screen):
    
    # Settings
    logoWidth = 400
    logoHeight = 300
    logoX = None
    logoY = None
    
    def getHandle(self):
        return 'start'
    
    def isDefault(self):
        return True
    
    def setup(self):
        self.logoX = width - self.logoWidth - ui.SPACING_LG
        self.logoY = ui.SPACING_LG + ui.SPACING_SM

    def draw(self):
        imageLoader = self.app.getModule('imageLoader')
        
        fill(ui.COLOR_TEXT)
        textSize(ui.TEXT_SIZE_XL)
        textAlign(LEFT)
        
        text('Teams', ui.SPACING_LG, ui.SPACING_LG)
        text('Spelers', ui.SPACING_LG, ui.SPACING_LG + ui.SPACING_SM + 80 + ui.SPACING_LG)
    
        image(imageLoader.get('logo'), self.logoX, self.logoY, self.logoWidth, self.logoHeight)
            
    def setMaxToFour(self):
        playerManager = self.app.getModule('playerManager')
        playerManager.setMaxPlayers(4)
        
    def setMaxToSix(self):
        playerManager = self.app.getModule('playerManager')
        playerManager.setMaxPlayers(6)
       
    def isStartDisabled(self):
        playerManager = self.app.getModule('playerManager')
        configInvalid = False

        # Make sure all locations are set
        for player in playerManager.getPlayers():
            if player.getLocation() != None:
                continue
            
            # Location not set, break!
            configInvalid = True
            break
            
        # Make sure a bot was selected
        if playerManager.botPlayer == None: 
            configInvalid = True
        
        return configInvalid
       
    def startGame(self):
        gameScreen = self.app.getScreen('game')
        gameManager = self.app.getModule('gameManager')
        turnManager = self.app.getModule('turnManager')
        botManager = self.app.getModule('botManager')
        currentPlayer = turnManager.currentPlayer
        
        # Prepare game and switch to game screen
        gameManager.setBoxLocations()
        gameManager.gameStarted = True
        self.app.setCurrentScreen(gameScreen)
        
        # Update bot if its the first player
        if currentPlayer != None and currentPlayer.isBot():
            botManager.handleBotTurn()
            turnManager.nextPlayer()
                      
    def getSubModules(self):
        modules = []
        playerManager = self.app.getModule('playerManager')
        
        modules.append([SelectableButton, {
            'x': ui.SPACING_LG,
            'y': ui.SPACING_LG + ui.SPACING_SM,
            'width': 225,
            'height': 80,
            'textSize': ui.TEXT_SIZE_LG,  
            'text': '2 teams',
            'group': 'maxPlayers',
            'selectedColor': ui.COLOR_RED_DARK,
            'onSelect': self.setMaxToFour,
            'default': True
        }])
        
        modules.append([SelectableButton, {
            'x': ui.SPACING_LG + 225 + ui.SPACING_XS,
            'y': ui.SPACING_LG + ui.SPACING_SM,
            'width': 225,
            'height': 80, 
            'textSize': ui.TEXT_SIZE_LG, 
            'text': '3 Teams',
            'group': 'maxPlayers',
            'selectedColor': ui.COLOR_RED_DARK,
            'onSelect': self.setMaxToSix
        }])
     
        modules.append([Button, {
            'x': self.logoX + self.logoWidth / 2 - 100,
            'y': self.logoY + self.logoHeight + ui.SPACING_SM,
            'width': 200,
            'height': 80,
            'textSize': ui.TEXT_SIZE_MD,  
            'text': 'START',
            'callback': self.startGame,
            'disabled': self.isStartDisabled
        }])
        
        playerButtonX = ui.SPACING_LG
        playerButtonY = ui.SPACING_LG + ui.SPACING_SM + 80 + ui.SPACING_LG + ui.SPACING_SM
        
        # Create PlayerButton modules
        players = playerManager.getAllPlayers()
        for i in range(1, len(players) + 1):
            modules.append([ PlayerButton, {
                'x': playerButtonX,
                'y': playerButtonY,
                'player': players[i - 1],
                'reverseAlignment': i % 2 != 0 
            } ])
            
            playerButtonX += 160 + ui.SPACING_XS
            
            if i % 2 == 0:
                playerButtonX = ui.SPACING_LG
                playerButtonY += 80 + ui.SPACING_XS
            
        return modules
