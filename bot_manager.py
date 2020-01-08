from module import Module

from location import Location

class BotManager(Module):
    
    # Settings
    boardSize = 22
    
    # Current dice value
    diceValue = None
    
    # Whether the bot has finished this section
    positionsHit = 1
    
    # Whether the bot is on breakpoint
    breakPoint = False
    
    def getHandle(self):
        return 'botManager'
        
    def draw(self):
        playerManager = self.app.getModule('playerManager')
        
    def rollDice(self):
        self.diceValue = int(random(1, 7))   
    
    def handleBotTurn(self):
        playerManager = self.app.getModule('playerManager')
        
        # Team players
        botPlayer = playerManager.botPlayer
        botPartner = botPlayer.getPartner()
        
        # Roll dice
        self.rollDice()
        steps = self.diceValue
        
        if self.breakPoint and steps == 6:
            self.breakPoint = False
            print('breakPoint:', False)  
        elif not self.breakPoint:
            self.performSteps(steps, self.shouldGoClockwise())    
    
    def performSteps(self, steps, clockwise):
        playerManager = self.app.getModule('playerManager')
        player = playerManager.botPlayer
        location = player.getLocation()
        stepsLeft = steps
        
        # New section and position
        section = location.section
        position = location.position
        
        # Place steps
        while stepsLeft > 0:
            stepsLeft -= 1
            
            if clockwise:
                position += 1
                
                # Make sure we stay on the board
                if position > self.boardSize:
                    position = 1
            else:
                position -= 1
                
                # Make sure we stay on the board
                if position < 1:
                    position = self.boardSize
                    
            self.positionsHit += 1
                
            # Check if this is the end
            if position == 1 and stepsLeft >= 1:
                stepsLeft -= 1
                
                if clockwise:
                    section += 1
                    
                    # Reset section if we've reached the end
                    if section > playerManager.maxPlayers:
                        section = 1
                else:
                    section -= 1
            
                    # Reset section if we've reached the end
                    if section < 1:
                        section = playerManager.maxPlayers
                        
                # New section, reset this value
                self.positionsHit = 0
                        
        # Perform steps
        player.setLocation(Location(section, position))
     
    def shouldGoClockwise(self):
        playerManager = self.app.getModule('playerManager')
        botPlayer = playerManager.botPlayer
        
        # Get locations
        botLocation = botPlayer.getLocation()
        partnerLocation = botPlayer.getPartner().getLocation()
        
        # Get distances
        clockwise = self.calcDistance(botLocation, partnerLocation, True)
        counterClockwise = self.calcDistance(botLocation, partnerLocation, False)
        
        # Find the shortest route
        return clockwise <= counterClockwise
     
    # Decreases the distance between the bot and 
    # its partner by x amount of steps
    def decreaseDistance(self, steps):
        self.performSteps(steps, self.shouldGoClockwise())
        
    # Increases the distance between the bot and 
    # its partner by x amount of steps
    def increaseDistance(self, steps):
        self.performSteps(steps, not self.shouldGoClockwise())
     
    def calcDistance(self, botLocation, partnerLocation, clockwise):
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
            if partnerLocation.section == botLocation.section:
                # Counter clockwise - bot and partner on same section
                if partnerLocation.position <= botLocation.position:
                    # Counter clockwise - partner in front of bot
                    return botLocation.position - partnerLocation.position
                else:
                    # Counter clockwise - partner behind bot
                    return stepsToSectionEnd + self._getShortestRoute(partnerLocation.position)
            elif partnerLocation.section < botLocation.section:
                # Counter clockwise - partner in front of bot section
                sections = botLocation.section - partnerLocation.section - 1
                boardSteps = botLocation.section - partnerLocation.section
                result = stepsToSectionEnd + (sections * self.boardSize) + self._getShortestRoute(partnerLocation.position) + boardSteps
                return result
            else:
                # Counter clockwise - partner behind bot section
                distanceToStart = ((botLocation.section - 1) * self.boardSize)
                distanceToPartner = ((self.boardSize - partnerLocation.section) * self.boardSize) + self._getShortestRoute(partnerLocation.position)
                boardSteps = (playerManager.maxPlayers - partnerLocation.section) + botLocation.section
                result = stepsToSectionEnd + distanceToStart + distanceToPartner + boardSteps
                return result
           
    def _getStepsToSectionEnd(self, location, clockwise):
        clockwiseResult = (self.boardSize - location.position) + 1
        counterClockwiseResult = location.position - 1
        
        if clockwise:
            result = clockwiseResult
        else:
            result = counterClockwiseResult
            
        # Make sure we reach enough steps
        if self.positionsHit + result < self.boardSize:
            result = counterClockwiseResult if clockwise else clockwiseResult
            
        return result
        
    def _getShortestRoute(self, position):
        clockwise = position - 1
        counterClockwise = (self.boardSize + 1) - position
        return clockwise if clockwise <= counterClockwise else counterClockwise
             
    
