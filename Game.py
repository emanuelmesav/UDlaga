import random
import pygame
from Ship import Ship
from Sky import Sky

class Game:
    
    def __init__(self):

            self.witdh=800
            self.heigth=800
            self.mySky=Sky(self.witdh, self.heigth,1000)
            self.ship=Ship(self.witdh/2)
            self.screen=pygame.display.set_mode((self.witdh, self.heigth))
            self.clock=pygame.time.Clock()
            self.fps=60
        #Descargar la hoja de imagenes
            self.sprites=pygame.image.load("Galaga sprites.png")
            self.shipsprite=pygame.Surface((64, 64)).convert()
            self.shipsprite.blit(self.sprites, (0,0), (250, 436, 64, 64))
    
    def checkKeys(self):
        keys=pygame.key.get_pressed() 
        if keys[pygame.K_q]: self.fps+=5
        elif keys[pygame.K_a]: self.fps-=5
        elif keys[pygame.K_RIGHT]: self.ship.direction="RIGTH"
        elif keys[pygame.K_LEFT]: self.ship.direction="LEFT"
        else:
            self.ship.direction="STOP"

    def run(self):

            pygame.init()

            control=True
            while control:

                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        pygame.quit()
                
                self.screen.fill((0,0,0))
            
                #Show the sky
                for star in self.mySky.stars:
                    r=random.randint(0,255)
                    g=random.randint(0,255)
                    b=random.randint(0,255)
                    pygame.draw.circle(self.screen, (r,g,b), star, 1)
                
                self.checkKeys() 
                self.ship.move()   
                self.mySky.move()
                x=self.ship.x
                y=self.heigth-100

                self.screen.blit(self.shipsprite, (x,y))
                self.clock.tick(self.fps)
                
                
                pygame.display.flip()

                
myGame=Game()
myGame.run()
