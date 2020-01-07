from location import Location
from module import Module
from card_screen import CardScreen


class GameManager(Module):
    
    # locations of all good and bad cards
    goodCardLocation = [Location(1, 5), Location(1, 9), Location(1, 13), Location(1, 17), Location(1, 21), Location(2, 5), Location(2, 9), Location(2, 13), Location(2, 17), Location(2, 21), Location(3, 5), Location(3, 9),Location(3, 13), Location(3, 17), Location(3, 21), Location(4, 5), Location(4, 9), Location(4, 13), Location(4, 17), Location(4, 21), Location(5, 5), Location(5, 9), Location(5, 13), Location(5, 17), Location(5, 21), Location(6, 5), Location(6, 9), Location(6, 13), Location(6, 17), Location(6, 21)]
    badCardLocation = None
    minBoxesLocation = None
    addBoxesLocation = None
    warpsLocation = None
    breakPoints = None
    
    def getHandle(self):
        return 'gameManager'
    
    def checkWinLose(self):
        playerManager = self.app.getModule('playerManager')
        cardScreen = self.app.getModule('card')
        
        # Loop through players
        for player in playerManager.getPlayers():
            partner = player.getPartner()
            
            # get a goodCard if player stands on a goodCard box
            if player.getLocation() == self.goodCardLocation:
                cardScreen = self.app.getScreen('card')
                self.app.setCurrentScreen(cardScreen)                
            
            # get a badCard if player stands on a badCard box        
            elif player.getLocation() == self.badCardLocation:
                cardScreen = self.app.getScreen('card')
                self.app.setCurrentScreen(cardScreen)
            
            # minus 3 or 2 steps if player stands on a minusBox        
            elif player.getLocation() == self.minBoxesLocation:
                break
            
            # add 3 or 2 steos if player stands on a addBox        
            elif player.getLocation() == self.addBoxesLocation:
                break
                    
            # Ignore if team members are not on the same location
            if player.getLocation() != partner.getLocation():
                continue
                
            # Check if they are standing on a breakpoint
            if player.getLocation() == 41 or player.getLocation() == 85:
                print ('lose')
            else :
                print ('win')
                
    def minBoxes(self):
        playerManager = self.app.getModule('playerManager')
        if playerManager.maxPlayers == 4:
            self.minBoxesLocation = [Location(2, 12), Location(4, 12)]
        else:
            self.minBoxesLocation = [Location(3,12), Location(6,12)]
    
    def addBoxes(self):
        playerManager = self.app.getModule('playerManager')
        if playerManager.maxPlayers == 4:
            self.addBoxesLocation = [Location(1, 12), Location(3, 12)]
        else:
            self.addBoxesLocation = [Location(1,12), Location(2,12), Location(4,12), Location(5,12)]    
                
    def warpsLocation(self):
        playerManager = self.app.getModule('playerManager')
        if playerManager.maxPlayers == 4:
            self.warpsLocation = [Location(1, 6), Location(1, 18), Location(2, 6), Location(2, 18), Location(3, 6), Location(3, 18), Location(4, 6), Location(4, 18)]
        else:
            self.warpsLocation = [Location(1, 6), Location(1, 18), Location(2, 6), Location(2, 18), Location(3, 6), Location(3, 18), Location(4, 6), Location(4, 18), Location(5, 6), Location(5, 18), Location(6, 6), Location(6, 18)]
    
    def breakPoints(self):
        playerManager = self.app.getModule('playerManager') 
        if playerManager.maxPlayers == 4:
            self.breakPointsLocation = [Location(2,19), Location(4,19)]
        else:
            self.breakPointsLocation = [Location(3, 19), Location(6, 19)]
    
    def badCards(self):    
        # check where is a badCard
        playerManager = self.app.getModule('playerManager') 
        if playerManager.maxPlayers == 4:
            self.badCardsLocation = [Location(1, 3), Location(1, 7), Location(1, 11), Location(1, 15), Location(1, 19), Location(2, 3), Location(2, 7), Location(2, 11), Location(2, 15), Location(3, 3), Location(3, 7), Location(3, 11), Location(3, 15), Location(3, 19), Location(4, 3), Location(4, 7), Location(4, 11), Location(4, 15)]
        else:
            self.badCardsLocation = [Location(1, 3), Location(1, 7), Location(1, 11), Location(1, 15), Location(1, 19), Location(2, 3), Location(2, 7), Location(2, 11), Location(2, 15), Location(2, 19), Location(3, 3), Location(3, 7), Location(3, 11), Location(3, 15), Location(4, 3), Location(4, 7), Location(4, 11), Location(4, 15), Location(4, 19), Location(5, 3), Location(5, 7), Location(5, 11), Location(5, 15), Location(5, 19), Location(6, 3), Location(6, 7), Location(6, 11), Location(6, 15)]
