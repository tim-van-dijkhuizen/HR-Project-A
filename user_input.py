from module import Module

class UserInput(Module):

    
    user_input = ''

    def keyPressed():
    
        if keyCode == 8:
            user_input = user_input[0:-1] 
        
        else:
            user_input+= key0
