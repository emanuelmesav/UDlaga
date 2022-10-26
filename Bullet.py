from Ship import Ship

class Bullet:
    
    def __init__(self):
        self.ship=Ship()
        self.state="STOP"
        self.ybullet=self.ship.y
    
    def shoot(self):
        
        if self.state== "Shooting up":
            self.ybullet -=5
        elif self.state=="STOP":
            pass