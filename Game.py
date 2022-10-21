import random
import pygame
from Sky import Sky

class Game:
    
    def __init__(self):

            self.witdh=800
            self.heigth=800
            self.mySky=Sky(self.witdh, self.heigth,1000)
            self.screen=pygame.display.set_mode((self.witdh, self.heigth))
            self.clock=pygame.time.Clock()
            self.fps=60
        #Descargar la hoja de imagenes
            self.sprites=pygame.image.load("Galaga sprites.png")
            self.shipsprite=pygame.Surface((64, 64)).convert()
            self.shipsprite.blit(self.sprites, (0,0), (250, 436, 64, 64))

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
                    
                self.mySky.move()
                x=self.witdh/2
                y=self.heigth/2

                self.screen.blit(self.shipsprite, (x,y))
                self.clock.tick(self.fps)
                
                pygame.display.flip()

                
myGame=Game()
myGame.run()
