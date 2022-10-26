
class Ship:

    def __init__(self):
        self.direction="UP"
        self.x=368
        self.y=710

    def move(self):
        
        if self.direction=="LEFT":
           self.x-=1
        elif self.direction=="RIGTH":
            self.x+=1
        elif self.direction=="STOP":
            pass
        
        return (self.x)
    
   
        

            