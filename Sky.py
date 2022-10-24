import random

class Sky:

    def __init__(self, width, heigth, quantity):
            
            self.stars=[]
            self.width=width
            self.heigth=heigth

            for i in range(quantity):#quantity
                x=random.randint(0,width)
                y=random.randint(0, heigth)
                self.stars.append([x, y])

    def move(self):
        for star in self.stars:
            star[1]+=1
            if star[1]>self.heigth:
                star[1]=0