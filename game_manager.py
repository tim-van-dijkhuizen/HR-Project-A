from module import Module

class GameManager(Module):
    
    def checkWinLose(self):
        playerManager = self.app.getModule('playerManager')
        
        # Loop through players
        for player in playerManager.getPlayers():
            partner = player.getPartner()
            
            # Ignore if team members are not on the same location
            if player.getLocation() != partner.getLocation():
                continue
                
            # Check if they are standing on a breakpoint
            if player.getLocation() == 41 or player.getLocation() == 85:
                print ('lose')
            else :
                print ('win')
