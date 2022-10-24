

class Ship:

    def __init__(self, x):
        self.direction="UP"
        self.x=x
        self.y=0

    def move(self):
        
        if self.direction=="LEFT":
           self.x-=1
        elif self.direction=="RIGTH":
            self.x+=1
        
        return (self.x)
    
   
        

            