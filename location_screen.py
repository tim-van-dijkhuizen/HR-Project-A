import ui
from screen import Screen
from button import Button
from location_button  import LocationButton
from location import Location

class LocationScreen(Screen):
    
    # Button offset
    buttonOffset = 145
    
    # Settings
    boardWidth = 794
    boardHeight = 500
    
    # The player to edit the location for
    fromScreen = None
    player = None
    
    def getHandle(self):
        return 'location'
        
    def setup(self):
        # TODO: This is really dirty...
        self.boardX = width / 2 - (self.boardWidth / 3.2)
        self.boardY = height / 2 - (self.boardHeight / 2)
            
    def draw(self):
        playerManager = self.app.getModule('playerManager')
        imageLoader = self.app.getModule('imageLoader')
        
        if self.player == None or self.fromScreen == None:
            raise ValueError('Variables player and fromScreen must be set')
        
        # Background
        background(ui.COLOR_RED_LIGHT)
        
        # Board image
        if playerManager.maxPlayers == 6:
           boardImage = imageLoader.get('board-players6')
        else:
            boardImage = imageLoader.get('board-players4')
            
        image(boardImage, self.boardX, self.boardY, self.boardWidth, self.boardHeight)
            
    def goBack(self):
        self.app.setCurrentScreen(self.fromScreen)
        self.fromScreen = None
        self.player = None
            
        
    def getSubModules(self):
        return [
            [ Button, {
                'x': ui.SPACING_MD,
                'y': ui.SPACING_MD,
                'width': 100,
                'height': 50,
                'color': ui.COLOR_RED_DARK,
                'text':'Terug',
                'textColor': ui.COLOR_TEXT,
                'textSize': ui.TEXT_SIZE_MD,
                'callback': self.goBack }
            ],
            
            [ LocationButton, { 'x': 735, 'y': 275, 'maxPlayers': 4, 'location': Location(1, 1) } ],
            [ LocationButton, { 'x': 705, 'y': 250, 'maxPlayers': 4, 'location': Location(1, 2) } ],
            [ LocationButton, { 'x': 678, 'y': 236, 'maxPlayers': 4, 'location': Location(1, 3) } ],
            [ LocationButton, { 'x': 657, 'y': 210, 'maxPlayers': 4, 'location': Location(1, 4) } ],
            [ LocationButton, { 'x': 635, 'y': 189, 'maxPlayers': 4, 'location': Location(1, 5) } ],
            [ LocationButton, { 'x': 615, 'y': 166, 'maxPlayers': 4, 'location': Location(1, 6) } ],
            [ LocationButton, { 'x': 615, 'y': 134, 'maxPlayers': 4, 'location': Location(1, 7) } ],
            [ LocationButton, { 'x': 628, 'y': 105, 'maxPlayers': 4, 'location': Location(1, 8) } ],
            [ LocationButton, { 'x': 658, 'y': 93, 'maxPlayers': 4, 'location': Location(1, 9) } ],
            [ LocationButton, { 'x': 688, 'y': 82, 'maxPlayers': 4, 'location': Location(1, 10) } ],
            [ LocationButton, { 'x': 715, 'y': 93, 'maxPlayers': 4, 'location': Location(1, 11) } ],
            [ LocationButton, { 'x': 735, 'y': 120, 'maxPlayers': 4, 'location': Location(1, 12) } ],
            [ LocationButton, { 'x': 750, 'y': 93, 'maxPlayers': 4, 'location': Location(1, 13) } ],
            [ LocationButton, { 'x': 780, 'y': 82, 'maxPlayers': 4, 'location': Location(1, 14) } ],
            [ LocationButton, { 'x': 810, 'y': 93, 'maxPlayers': 4, 'location': Location(1, 15) } ],
            [ LocationButton, { 'x': 838, 'y': 108, 'maxPlayers': 4, 'location': Location(1, 16) } ],
            [ LocationButton, { 'x': 852, 'y': 137, 'maxPlayers': 4, 'location': Location(1, 17) } ],
            [ LocationButton, { 'x': 852, 'y': 166, 'maxPlayers': 4, 'location': Location(1, 18) } ],
            [ LocationButton, { 'x': 830, 'y': 189, 'maxPlayers': 4, 'location': Location(1, 19) } ],
            [ LocationButton, { 'x': 810, 'y': 212, 'maxPlayers': 4, 'location': Location(1, 20) } ],
            [ LocationButton, { 'x': 791, 'y': 236, 'maxPlayers': 4, 'location': Location(1, 21) } ],
            [ LocationButton, { 'x': 765, 'y': 250, 'maxPlayers': 4, 'location': Location(1, 22) } ],
            
            [ LocationButton, { 'x': 779, 'y': 312, 'maxPlayers': 4, 'location': Location(2, 1) } ],
            [ LocationButton, { 'x': 803, 'y': 282, 'maxPlayers': 4, 'location': Location(2, 2) } ],
            [ LocationButton, { 'x': 818, 'y': 255, 'maxPlayers': 4, 'location': Location(2, 3) } ], 
            [ LocationButton, { 'x': 840, 'y': 235, 'maxPlayers': 4, 'location': Location(2, 4) } ],
            [ LocationButton, { 'x': 863, 'y': 213, 'maxPlayers': 4, 'location': Location(2, 5) } ], 
            [ LocationButton, { 'x': 888, 'y': 192, 'maxPlayers': 4, 'location': Location(2, 6) } ],
            [ LocationButton, { 'x': 918, 'y': 192, 'maxPlayers': 4, 'location': Location(2, 7) } ],
            [ LocationButton, { 'x': 948, 'y': 204, 'maxPlayers': 4, 'location': Location(2, 8) } ],
            [ LocationButton, { 'x': 960, 'y': 235, 'maxPlayers': 4, 'location': Location(2, 9) } ],
            [ LocationButton, { 'x': 970, 'y': 265, 'maxPlayers': 4, 'location': Location(2, 10) } ],
            [ LocationButton, { 'x': 957, 'y': 295, 'maxPlayers': 4, 'location': Location(2, 11) } ],
            [ LocationButton, { 'x': 930, 'y': 310, 'maxPlayers': 4, 'location': Location(2, 12) } ],
            [ LocationButton, { 'x': 957, 'y': 328, 'maxPlayers': 4, 'location': Location(2, 13) } ],
            [ LocationButton, { 'x': 970, 'y': 357, 'maxPlayers': 4, 'location': Location(2, 14) } ],
            [ LocationButton, { 'x': 960, 'y': 387, 'maxPlayers': 4, 'location': Location(2, 15) } ],
            [ LocationButton, { 'x': 945, 'y': 415, 'maxPlayers': 4, 'location': Location(2, 16) } ],
            [ LocationButton, { 'x': 915, 'y': 432, 'maxPlayers': 4, 'location': Location(2, 17) } ],
            [ LocationButton, { 'x': 885, 'y': 432, 'maxPlayers': 4, 'location': Location(2, 18) } ],
            [ LocationButton, { 'x': 863, 'y': 410, 'maxPlayers': 4, 'location': Location(2, 19) } ],
            [ LocationButton, { 'x': 840, 'y': 389, 'maxPlayers': 4, 'location': Location(2, 20) } ],
            [ LocationButton, { 'x': 818, 'y': 368, 'maxPlayers': 4, 'location': Location(2, 21) } ],
            [ LocationButton, { 'x': 802, 'y': 342, 'maxPlayers': 4, 'location': Location(2, 22) } ],
            
            [ LocationButton, { 'x': 735, 'y': 353, 'maxPlayers': 4, 'location': Location(3, 1) } ],
            [ LocationButton, { 'x': 765, 'y': 378, 'maxPlayers': 4, 'location': Location(3, 2) } ],
            [ LocationButton, { 'x': 791, 'y': 393, 'maxPlayers': 4, 'location': Location(3, 3) } ],
            [ LocationButton, { 'x': 812, 'y': 415, 'maxPlayers': 4, 'location': Location(3, 4) } ],
            [ LocationButton, { 'x': 832, 'y': 438, 'maxPlayers': 4, 'location': Location(3, 5) } ],
            [ LocationButton, { 'x': 852, 'y': 466, 'maxPlayers': 4, 'location': Location(3, 6) } ],
            [ LocationButton, { 'x': 852, 'y': 496, 'maxPlayers': 4, 'location': Location(3, 7) } ],
            [ LocationButton, { 'x': 840, 'y': 524, 'maxPlayers': 4, 'location': Location(3, 8) } ],
            [ LocationButton, { 'x': 810, 'y': 538, 'maxPlayers': 4, 'location': Location(3, 9) } ],
            [ LocationButton, { 'x': 780, 'y': 548, 'maxPlayers': 4, 'location': Location(3, 10) } ],
            [ LocationButton, { 'x': 753, 'y': 536, 'maxPlayers': 4, 'location': Location(3, 11) } ],
            [ LocationButton, { 'x': 735, 'y': 510, 'maxPlayers': 4, 'location': Location(3, 12) } ],
            [ LocationButton, { 'x': 719, 'y': 536, 'maxPlayers': 4, 'location': Location(3, 13) } ],
            [ LocationButton, { 'x': 688, 'y': 548, 'maxPlayers': 4, 'location': Location(3, 14) } ],
            [ LocationButton, { 'x': 660, 'y': 534, 'maxPlayers': 4, 'location': Location(3, 15) } ],
            [ LocationButton, { 'x': 630, 'y': 521, 'maxPlayers': 4, 'location': Location(3, 16) } ],
            [ LocationButton, { 'x': 616, 'y': 494, 'maxPlayers': 4, 'location': Location(3, 17) } ],
            [ LocationButton, { 'x': 616, 'y': 462, 'maxPlayers': 4, 'location': Location(3, 18) } ],
            [ LocationButton, { 'x': 638, 'y': 440, 'maxPlayers': 4, 'location': Location(3, 19) } ],
            [ LocationButton, { 'x': 657, 'y': 415, 'maxPlayers': 4, 'location': Location(3, 20) } ],
            [ LocationButton, { 'x': 678, 'y': 393, 'maxPlayers': 4, 'location': Location(3, 21) } ],
            [ LocationButton, { 'x': 705, 'y': 378, 'maxPlayers': 4, 'location': Location(3, 22) } ],
            
            [ LocationButton, { 'x': 692, 'y': 312, 'maxPlayers': 4, 'location': Location(4, 1) } ],
            [ LocationButton, { 'x': 669, 'y': 342, 'maxPlayers': 4, 'location': Location(4, 2) } ],
            [ LocationButton, { 'x': 655, 'y': 368, 'maxPlayers': 4, 'location': Location(4, 3) } ],
            [ LocationButton, { 'x': 630, 'y': 389, 'maxPlayers': 4, 'location': Location(4, 4) } ],
            [ LocationButton, { 'x': 606, 'y': 410, 'maxPlayers': 4, 'location': Location(4, 5) } ],
            [ LocationButton, { 'x': 583, 'y': 432, 'maxPlayers': 4, 'location': Location(4, 6) } ],
            [ LocationButton, { 'x': 553, 'y': 432, 'maxPlayers': 4, 'location': Location(4, 7) } ],
            [ LocationButton, { 'x': 525, 'y': 420, 'maxPlayers': 4, 'location': Location(4, 8) } ],
            [ LocationButton, { 'x': 510, 'y': 390, 'maxPlayers': 4, 'location': Location(4, 9) } ],
            [ LocationButton, { 'x': 497, 'y': 360, 'maxPlayers': 4, 'location': Location(4, 10) } ],
            [ LocationButton, { 'x': 512, 'y': 330, 'maxPlayers': 4, 'location': Location(4, 11) } ],
            [ LocationButton, { 'x': 542, 'y': 314, 'maxPlayers': 4, 'location': Location(4, 12) } ],
            [ LocationButton, { 'x': 512, 'y': 298, 'maxPlayers': 4, 'location': Location(4, 13) } ],
            [ LocationButton, { 'x': 500, 'y': 267, 'maxPlayers': 4, 'location': Location(4, 14) } ],
            [ LocationButton, { 'x': 512, 'y': 238, 'maxPlayers': 4, 'location': Location(4, 15) } ],
            [ LocationButton, { 'x': 525, 'y': 208, 'maxPlayers': 4, 'location': Location(4, 16) } ],
            [ LocationButton, { 'x': 553, 'y': 195, 'maxPlayers': 4, 'location': Location(4, 17) } ],
            [ LocationButton, { 'x': 583, 'y': 195, 'maxPlayers': 4, 'location': Location(4, 18) } ],
            [ LocationButton, { 'x': 606, 'y': 215, 'maxPlayers': 4, 'location': Location(4, 19) } ],
            [ LocationButton, { 'x': 630, 'y': 235, 'maxPlayers': 4, 'location': Location(4, 20) } ],
            [ LocationButton, { 'x': 655, 'y': 256, 'maxPlayers': 4, 'location': Location(4, 21) } ],
            [ LocationButton, { 'x': 669, 'y': 282, 'maxPlayers': 4, 'location': Location(4, 22) } ],
            
            #left up
            [ LocationButton, { 'x': 735 - 147.5, 'y': 275, 'maxPlayers': 6, 'location': Location(1, 1) } ],
            [ LocationButton, { 'x': 705 - 147.5, 'y': 250, 'maxPlayers': 6, 'location': Location(1, 2) } ],
            [ LocationButton, { 'x': 678 - 147.5, 'y': 236, 'maxPlayers': 6, 'location': Location(1, 3) } ],
            [ LocationButton, { 'x': 655 - 147.5, 'y': 210, 'maxPlayers': 6, 'location': Location(1, 4) } ],
            [ LocationButton, { 'x': 635 - 147.5, 'y': 189, 'maxPlayers': 6, 'location': Location(1, 5) } ],
            [ LocationButton, { 'x': 615 - 147.5, 'y': 163, 'maxPlayers': 6, 'location': Location(1, 6) } ],
            [ LocationButton, { 'x': 615 - 147.5, 'y': 131, 'maxPlayers': 6, 'location': Location(1, 7) } ],
            [ LocationButton, { 'x': 628 - 147.5, 'y': 105, 'maxPlayers': 6, 'location': Location(1, 8) } ],
            [ LocationButton, { 'x': 658 - 147.5, 'y': 90, 'maxPlayers': 6, 'location': Location(1, 9), } ],
            [ LocationButton, { 'x': 688 - 147.5, 'y': 79, 'maxPlayers': 6, 'location': Location(1, 10) } ],
            [ LocationButton, { 'x': 716 - 147.5, 'y': 90, 'maxPlayers': 6, 'location': Location(1, 11) } ],
            [ LocationButton, { 'x': 735 - 147.5, 'y': 120, 'maxPlayers': 6, 'location': Location(1, 12) } ],
            [ LocationButton, { 'x': 750 - 147.5, 'y': 90, 'maxPlayers': 6, 'location': Location(1, 13) } ],
            [ LocationButton, { 'x': 780 - 147.5, 'y': 79, 'maxPlayers': 6, 'location': Location(1, 14) } ],
            [ LocationButton, { 'x': 812 - 147.5, 'y': 90, 'maxPlayers': 6, 'location': Location(1, 15) } ],
            [ LocationButton, { 'x': 840 - 147.5, 'y': 106, 'maxPlayers': 6, 'location': Location(1, 16) } ],
            [ LocationButton, { 'x': 854 - 147.5, 'y': 137, 'maxPlayers': 6, 'location': Location(1, 17) } ],
            [ LocationButton, { 'x': 854 - 147.5, 'y': 166, 'maxPlayers': 6, 'location': Location(1, 18) } ],
            [ LocationButton, { 'x': 833 - 147.5, 'y': 183, 'maxPlayers': 6, 'location': Location(1, 19) } ],
            [ LocationButton, { 'x': 812 - 147.5, 'y': 210, 'maxPlayers': 6, 'location': Location(1, 20) } ],
            [ LocationButton, { 'x': 791 - 147.5, 'y': 236, 'maxPlayers': 6, 'location': Location(1, 21) } ],
            [ LocationButton, { 'x': 765 - 147.5, 'y': 250, 'maxPlayers': 6, 'location': Location(1, 22) } ], 
            #right up
            [ LocationButton, { 'x': 735 + 142, 'y': 275, 'maxPlayers': 6, 'location': Location(2, 1) } ],
            [ LocationButton, { 'x': 705 + 142, 'y': 249, 'maxPlayers': 6, 'location': Location(2, 2) } ],
            [ LocationButton, { 'x': 676 + 142, 'y': 232, 'maxPlayers': 6, 'location': Location(2, 3) } ],
            [ LocationButton, { 'x': 655 + 142, 'y': 210, 'maxPlayers': 6, 'location': Location(2, 4) } ],
            [ LocationButton, { 'x': 632 + 142, 'y': 189, 'maxPlayers': 6, 'location': Location(2, 5) } ],
            [ LocationButton, { 'x': 612 + 142, 'y': 160, 'maxPlayers': 6, 'location': Location(2, 6) } ],
            [ LocationButton, { 'x': 612 + 142, 'y': 132, 'maxPlayers': 6, 'location': Location(2, 7) } ],
            [ LocationButton, { 'x': 625 + 142, 'y': 99, 'maxPlayers': 6, 'location': Location(2, 8) } ],
            [ LocationButton, { 'x': 655 + 142, 'y': 91, 'maxPlayers': 6, 'location': Location(2, 9) } ],
            [ LocationButton, { 'x': 688 + 142, 'y': 79, 'maxPlayers': 6, 'location': Location(2, 10) } ],
            [ LocationButton, { 'x': 715 + 142, 'y': 91, 'maxPlayers': 6, 'location': Location(2, 11) } ],
            [ LocationButton, { 'x': 733 + 142, 'y': 118, 'maxPlayers': 6, 'location': Location(2, 12) } ],
            [ LocationButton, { 'x': 750 + 142, 'y': 91, 'maxPlayers': 6, 'location': Location(2, 13) } ],
            [ LocationButton, { 'x': 780 + 142, 'y': 79, 'maxPlayers': 6, 'location': Location(2, 14) } ],
            [ LocationButton, { 'x': 810 + 142, 'y': 91, 'maxPlayers': 6, 'location': Location(2, 15) } ],
            [ LocationButton, { 'x': 838 + 142, 'y': 100, 'maxPlayers': 6, 'location': Location(2, 16) } ],
            [ LocationButton, { 'x': 852 + 142, 'y': 137, 'maxPlayers': 6, 'location': Location(2, 17) } ],
            [ LocationButton, { 'x': 852 + 142, 'y': 166, 'maxPlayers': 6, 'location': Location(2, 18) } ],
            [ LocationButton, { 'x': 830 + 142, 'y': 189, 'maxPlayers': 6, 'location': Location(2, 19) } ],
            [ LocationButton, { 'x': 810 + 142, 'y': 212, 'maxPlayers': 6, 'location': Location(2, 20) } ],
            [ LocationButton, { 'x': 791 + 142, 'y': 236, 'maxPlayers': 6, 'location': Location(2, 21) } ],
            [ LocationButton, { 'x': 765 + 142, 'y': 249, 'maxPlayers': 6, 'location': Location(2, 22) } ], 
            #right
            [ LocationButton, { 'x': 779 + self.buttonOffset, 'y': 312, 'maxPlayers': 6, 'location': Location(3, 1) } ],
            [ LocationButton, { 'x': 800 + self.buttonOffset, 'y': 282, 'maxPlayers': 6, 'location': Location(3, 2) } ],
            [ LocationButton, { 'x': 816 + self.buttonOffset, 'y': 255, 'maxPlayers': 6, 'location': Location(3, 3) } ], 
            [ LocationButton, { 'x': 840 + self.buttonOffset, 'y': 235, 'maxPlayers': 6, 'location': Location(3, 4) } ],
            [ LocationButton, { 'x': 863 + self.buttonOffset, 'y': 215, 'maxPlayers': 6, 'location': Location(3, 5) } ], 
            [ LocationButton, { 'x': 888 + self.buttonOffset, 'y': 192, 'maxPlayers': 6, 'location': Location(3, 6) } ],
            [ LocationButton, { 'x': 918 + self.buttonOffset, 'y': 192, 'maxPlayers': 6, 'location': Location(3, 7) } ],
            [ LocationButton, { 'x': 948 + self.buttonOffset, 'y': 204, 'maxPlayers': 6, 'location': Location(3, 8) } ],
            [ LocationButton, { 'x': 960 + self.buttonOffset, 'y': 235, 'maxPlayers': 6, 'location': Location(3, 9) } ],
            [ LocationButton, { 'x': 973 + self.buttonOffset, 'y': 265, 'maxPlayers': 6, 'location': Location(3, 10) } ],
            [ LocationButton, { 'x': 957 + self.buttonOffset, 'y': 295, 'maxPlayers': 6, 'location': Location(3, 11) } ],
            [ LocationButton, { 'x': 930 + self.buttonOffset, 'y': 312, 'maxPlayers': 6, 'location': Location(3, 12) } ],
            [ LocationButton, { 'x': 957 + self.buttonOffset, 'y': 327, 'maxPlayers': 6, 'location': Location(3, 13) } ],
            [ LocationButton, { 'x': 970 + self.buttonOffset, 'y': 357, 'maxPlayers': 6, 'location': Location(3, 14) } ],
            [ LocationButton, { 'x': 960 + self.buttonOffset, 'y': 387, 'maxPlayers': 6, 'location': Location(3, 15) } ],
            [ LocationButton, { 'x': 945 + self.buttonOffset, 'y': 415, 'maxPlayers': 6, 'location': Location(3, 16) } ],
            [ LocationButton, { 'x': 915 + self.buttonOffset, 'y': 432, 'maxPlayers': 6, 'location': Location(3, 17) } ],
            [ LocationButton, { 'x': 885 + self.buttonOffset, 'y': 432, 'maxPlayers': 6, 'location': Location(3, 18) } ],
            [ LocationButton, { 'x': 863 + self.buttonOffset, 'y': 410, 'maxPlayers': 6, 'location': Location(3, 19) } ],
            [ LocationButton, { 'x': 840 + self.buttonOffset, 'y': 389, 'maxPlayers': 6, 'location': Location(3, 20) } ],
            [ LocationButton, { 'x': 816 + self.buttonOffset, 'y': 368, 'maxPlayers': 6, 'location': Location(3, 21) } ],
            [ LocationButton, { 'x': 800 + self.buttonOffset, 'y': 342, 'maxPlayers': 6, 'location': Location(3, 22) } ],
            
            # right down
            [ LocationButton, { 'x': 736 + 142, 'y': 350, 'maxPlayers': 6, 'location': Location(4, 1) } ],
            [ LocationButton, { 'x': 706 + 142, 'y': 377, 'maxPlayers': 6, 'location': Location(4, 2) } ],
            [ LocationButton, { 'x': 681 + 142, 'y': 392, 'maxPlayers': 6, 'location': Location(4, 3) } ],
            [ LocationButton, { 'x': 657 + 145, 'y': 415, 'maxPlayers': 6, 'location': Location(4, 4) } ],
            [ LocationButton, { 'x': 637 + 145, 'y': 440, 'maxPlayers': 6, 'location': Location(4, 5) } ],
            [ LocationButton, { 'x': 617 + 142, 'y': 466, 'maxPlayers': 6, 'location': Location(4, 6) } ],
            [ LocationButton, { 'x': 617 + 142, 'y': 494, 'maxPlayers': 6, 'location': Location(4, 7) } ],
            [ LocationButton, { 'x': 633 + 142, 'y': 523, 'maxPlayers': 6, 'location': Location(4, 8) } ],
            [ LocationButton, { 'x': 658 + 145, 'y': 540, 'maxPlayers': 6, 'location': Location(4, 9) } ],
            [ LocationButton, { 'x': 688 + 145, 'y': 550, 'maxPlayers': 6, 'location': Location(4, 10) } ],
            [ LocationButton, { 'x': 717 + 145, 'y': 535, 'maxPlayers': 6, 'location': Location(4, 11) } ],
            [ LocationButton, { 'x': 736 + 145, 'y': 510, 'maxPlayers': 6, 'location': Location(4, 12) } ],
            [ LocationButton, { 'x': 754 + 145, 'y': 535, 'maxPlayers': 6, 'location': Location(4, 13) } ],
            [ LocationButton, { 'x': 780 + 145, 'y': 550, 'maxPlayers': 6, 'location': Location(4, 14) } ],
            [ LocationButton, { 'x': 811 + 145, 'y': 540, 'maxPlayers': 6, 'location': Location(4, 15) } ],
            [ LocationButton, { 'x': 840 + 145, 'y': 525, 'maxPlayers': 6, 'location': Location(4, 16) } ],
            [ LocationButton, { 'x': 854 + 145, 'y': 494, 'maxPlayers': 6, 'location': Location(4, 17) } ],
            [ LocationButton, { 'x': 854 + 145, 'y': 466, 'maxPlayers': 6, 'location': Location(4, 18) } ],
            [ LocationButton, { 'x': 832 + 145, 'y': 440, 'maxPlayers': 6, 'location': Location(4, 19) } ],
            [ LocationButton, { 'x': 812 + 145, 'y': 415, 'maxPlayers': 6, 'location': Location(4, 20) } ],
            [ LocationButton, { 'x': 791 + 145, 'y': 392, 'maxPlayers': 6, 'location': Location(4, 21) } ],
            [ LocationButton, { 'x': 765 + 145, 'y': 377, 'maxPlayers': 6, 'location': Location(4, 22) } ],
            #left down
            [ LocationButton, { 'x': 736 - 145, 'y': 352, 'maxPlayers': 6, 'location': Location(5, 1) } ],
            [ LocationButton, { 'x': 705 - 145, 'y': 378, 'maxPlayers': 6, 'location': Location(5, 2) } ],
            [ LocationButton, { 'x': 678 - 145, 'y': 390, 'maxPlayers': 6, 'location': Location(5, 3) } ],
            [ LocationButton, { 'x': 656 - 145, 'y': 416, 'maxPlayers': 6, 'location': Location(5, 4) } ],
            [ LocationButton, { 'x': 637 - 145, 'y': 440, 'maxPlayers': 6, 'location': Location(5, 5) } ],
            [ LocationButton, { 'x': 617 - 145, 'y': 466, 'maxPlayers': 6, 'location': Location(5, 6) } ],
            [ LocationButton, { 'x': 617 - 145, 'y': 494, 'maxPlayers': 6, 'location': Location(5, 7) } ],
            [ LocationButton, { 'x': 628 - 145, 'y': 525, 'maxPlayers': 6, 'location': Location(5, 8) } ],
            [ LocationButton, { 'x': 658 - 145, 'y': 540, 'maxPlayers': 6, 'location': Location(5, 9) } ],
            [ LocationButton, { 'x': 688 - 145, 'y': 550, 'maxPlayers': 6, 'location': Location(5, 10) } ],
            [ LocationButton, { 'x': 720 - 145, 'y': 535, 'maxPlayers': 6, 'location': Location(5, 11) } ],
            [ LocationButton, { 'x': 738 - 145, 'y': 510, 'maxPlayers': 6, 'location': Location(5, 12) } ],
            [ LocationButton, { 'x': 755 - 145, 'y': 535, 'maxPlayers': 6, 'location': Location(5, 13) } ],
            [ LocationButton, { 'x': 785 - 145, 'y': 550, 'maxPlayers': 6, 'location': Location(5, 14) } ],
            [ LocationButton, { 'x': 814 - 145, 'y': 540, 'maxPlayers': 6, 'location': Location(5, 15) } ],
            [ LocationButton, { 'x': 849 - 145, 'y': 528, 'maxPlayers': 6, 'location': Location(5, 16) } ],
            [ LocationButton, { 'x': 859 - 145, 'y': 494, 'maxPlayers': 6, 'location': Location(5, 17) } ],
            [ LocationButton, { 'x': 859 - 145, 'y': 466, 'maxPlayers': 6, 'location': Location(5, 18) } ],
            [ LocationButton, { 'x': 837 - 145, 'y': 438, 'maxPlayers': 6, 'location': Location(5, 19) } ],
            [ LocationButton, { 'x': 821 - 145, 'y': 418, 'maxPlayers': 6, 'location': Location(5, 20) } ],
            [ LocationButton, { 'x': 795 - 145, 'y': 390, 'maxPlayers': 6, 'location': Location(5, 21) } ],
            [ LocationButton, { 'x': 765 - 145, 'y': 378, 'maxPlayers': 6, 'location': Location(5, 22) } ],
            # left 
            [ LocationButton, { 'x': 692 - self.buttonOffset, 'y': 317, 'maxPlayers': 6, 'location': Location(6, 1) } ],
            [ LocationButton, { 'x': 669 - self.buttonOffset, 'y': 347, 'maxPlayers': 6, 'location': Location(6, 2) } ],
            [ LocationButton, { 'x': 652 - self.buttonOffset, 'y': 375, 'maxPlayers': 6, 'location': Location(6, 3) } ],
            [ LocationButton, { 'x': 630 - self.buttonOffset, 'y': 396, 'maxPlayers': 6, 'location': Location(6, 4) } ],
            [ LocationButton, { 'x': 606 - self.buttonOffset, 'y': 416, 'maxPlayers': 6, 'location': Location(6, 5) } ],
            [ LocationButton, { 'x': 583 - self.buttonOffset, 'y': 437, 'maxPlayers': 6, 'location': Location(6, 6) } ],
            [ LocationButton, { 'x': 553 - self.buttonOffset, 'y': 437, 'maxPlayers': 6, 'location': Location(6, 7) } ],
            [ LocationButton, { 'x': 525 - self.buttonOffset, 'y': 423, 'maxPlayers': 6, 'location': Location(6, 8) } ],
            [ LocationButton, { 'x': 510 - self.buttonOffset, 'y': 393, 'maxPlayers': 6, 'location': Location(6, 9) } ],
            [ LocationButton, { 'x': 497 - self.buttonOffset, 'y': 363, 'maxPlayers': 6, 'location': Location(6, 10) } ],
            [ LocationButton, { 'x': 512 - self.buttonOffset, 'y': 333, 'maxPlayers': 6, 'location': Location(6, 11) } ],
            [ LocationButton, { 'x': 542 - self.buttonOffset, 'y': 318, 'maxPlayers': 6, 'location': Location(6, 12) } ],
            [ LocationButton, { 'x': 512 - self.buttonOffset, 'y': 300, 'maxPlayers': 6, 'location': Location(6, 13) } ],
            [ LocationButton, { 'x': 500 - self.buttonOffset, 'y': 270, 'maxPlayers': 6, 'location': Location(6, 14) } ],
            [ LocationButton, { 'x': 512 - self.buttonOffset, 'y': 240, 'maxPlayers': 6, 'location': Location(6, 15) } ],
            [ LocationButton, { 'x': 525 - self.buttonOffset, 'y': 208, 'maxPlayers': 6, 'location': Location(6, 16) } ],
            [ LocationButton, { 'x': 553 - self.buttonOffset, 'y': 196, 'maxPlayers': 6, 'location': Location(6, 17) } ],
            [ LocationButton, { 'x': 583 - self.buttonOffset, 'y': 196, 'maxPlayers': 6, 'location': Location(6, 18) } ],
            [ LocationButton, { 'x': 606 - self.buttonOffset, 'y': 217, 'maxPlayers': 6, 'location': Location(6, 19) } ],
            [ LocationButton, { 'x': 630 - self.buttonOffset, 'y': 237, 'maxPlayers': 6, 'location': Location(6, 20) } ],
            [ LocationButton, { 'x': 655 - self.buttonOffset, 'y': 258, 'maxPlayers': 6, 'location': Location(6, 21) } ],
            [ LocationButton, { 'x': 670 - self.buttonOffset, 'y': 287, 'maxPlayers': 6, 'location': Location(6, 22) } ],
        ]
