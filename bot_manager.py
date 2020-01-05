from module import Module

class BotManager(Module):
    
    diceValue = None
    clockwise = True
    
    def getHandle(self):
        return 'botManager'
    
    def setup(self):
        playerManager = self.app.getModule('playerManager')
        
        print(self._calcDistance(16, 5, True))
        print(self._calcDistance(16, 5, False))
        
    def draw(self):
        playerManager = self.app.getModule('playerManager')
        
    def rollDice(self):
        self.diceValue = random(1, 7)   
    
    def handleBotTurn(self):
        playerManager = self.app.getModule('playerManager')
        
        # Team players
        botPlayer = playerManager.botPlayer
        botPartner = botPlayer.getPartner()
        
        # Roll dice
        self.rollDice()
        steps = self.diceValue
        
        # Team locations
        botLocation = botPlayer.getLocation()
        partnerLocation = botPartner.getLocation()

        # Update direction
        self._updateDirection(botLocation, partnerLocation)

        if botLocation > partnerLocation:
            botLocation = botLocation - steps
            botPlayer.setLocation(botLocation)
        else:
            botLocation = steps + botLocation
            botPlayer.setLocation(botLocation)
          
    def _calcDistance(self, botPlayer, partnerPlayer, clockwise):
        playerManager = self.app.getModule('playerManager')
        boardSize = 4 * playerManager.maxPlayers
        
        if clockwise:
            if partnerPlayer >= botPlayer:
                return partnerPlayer - botPlayer
            else:
                toEnd = boardSize - botPlayer
                return toEnd + partnerPlayer
        else:
            if partnerPlayer < botPlayer:
                return botPlayer - partnerPlayer
            else:
                toPartner = boardSize - partnerPlayer
                return toPartner + botPlayer
        
            
            
    def _updateDirection(self, botPlayer, partnerPlayer):
        clockwise = self._calcDistance(botPlayer, partnerPlayer, True)
        counterClockwise = self._calcDistance(botPlayer, partnerPlayer, False)
        
        if clockwise <= counterClockwise:
            self.clockwise = True
        else:
            self.clockwise = False
             
    
