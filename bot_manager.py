from module import Module

from location import Location

class BotManager(Module):
    
    # Settings
    boardSize = 4
    
    # Current dice value
    diceValue = None
    
    def getHandle(self):
        return 'botManager'
    
    def setup(self):
        playerManager = self.app.getModule('playerManager')
        
        #print('test1:', self._calcDistance(Location(1, 4), Location(1, 1), False)) # 3
        #print('test1:', self._calcDistance(Location(4, 3), Location(4, 2), False)) # 3
        
        #print('test2:', self._calcDistance(Location(1, 2), Location(1, 3), False)) # 3
        #print('test2:', self._calcDistance(Location(3, 1), Location(3, 4), False)) # 3
        
        #print('test3:', self._calcDistance(Location(1, 2), Location(3, 4), False))
        #print('test3:', self._calcDistance(Location(3, 1), Location(4, 3), False))
        
        #print('test4:', self._calcDistance(Location(3, 2), Location(1, 4), False))
        #print('test4:', self._calcDistance(Location(4, 1), Location(3, 3), False))
        
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
          
    def _calcDistance(self, botLocation, partnerLocation, clockwise):
        playerManager = self.app.getModule('playerManager')
        boardSize = self.boardSize * playerManager.maxPlayers
        
        # Find steps to the end of the section
        stepsToSectionEnd = self._getStepsToSectionEnd(botLocation, clockwise)
        
        if clockwise:
            if partnerLocation.section == botLocation.section:
                # Clockwise bot and partner on same section
                if partnerLocation.position >= botLocation.position:
                    # Clockwise - partner in front of bot
                    return partnerLocation.position - botLocation.position
                else:
                    # Clockwise - partner behind bot
                    return stepsToSectionEnd + self._getShortestRoute(partnerLocation.position)
            elif partnerLocation.section > botLocation.section:
                # Clockwise - partner in front of bot section
                sections = partnerLocation.section - botLocation.section - 1
                boardSteps = partnerLocation.section - botLocation.section
                result = stepsToSectionEnd + (sections * self.boardSize) + self._getShortestRoute(partnerLocation.position) + boardSteps
                return result
            else:
                # Clockwise - partner behind bot section
                distanceToStart = ((playerManager.maxPlayers - botLocation.section) * self.boardSize)
                distanceToPartner = ((partnerLocation.section - 1) * self.boardSize) + self._getShortestRoute(partnerLocation.position)
                boardSteps = (playerManager.maxPlayers - botLocation.section) + partnerLocation.section
                result = stepsToSectionEnd + distanceToStart + distanceToPartner + boardSteps
                return result
        else:
            # Counter clockwise - bot and partner on same section
            if partnerLocation.position <= botLocation.position:
                # Counter clockwise - partner in front of bot
                return botLocation.position - partnerLocation.position
            else:
                # Counter clockwise - partner behind bot
                return stepsToSectionEnd + self._getShortestRoute(partnerLocation.position)
           
    def _getStepsToSectionEnd(self, location, clockwise):
        if clockwise:
            return (self.boardSize - location.position) + 1
        else:
            return location.position - 1
        
    def _getShortestRoute(self, position):
        clockwise = position - 1
        counterClockwise = (self.boardSize + 1) - position
        return clockwise if clockwise <= counterClockwise else counterClockwise
    
    def _getDirection(self, current, target):
        clockwise = self._calcDistance(current, target, True)
        counterClockwise = self._calcDistance(current, target, False)
        
        if clockwise <= counterClockwise:
            return True
        else:
            return False
             
    
