import random
import pygame
from Ship import Ship
from Sky import Sky
from Bullet import Bullet

class Game:
    
    def __init__(self):

            self.witdh=800
            self.heigth=800
            self.mySky=Sky(self.witdh, self.heigth,1000)
            self.ship=Ship()
            self.bullet=Bullet()
            self.screen=pygame.display.set_mode((self.witdh, self.heigth))
            self.clock=pygame.time.Clock()
            self.fps=60
        #Descargar la hoja de imagenes
            self.sprites=pygame.image.load("Galaga sprites.png")
            self.shipsprite=pygame.Surface((64, 64)).convert()
            self.shipsprite.blit(self.sprites, (0,0), (250, 436, 64, 64))
            self.spritesbullet=pygame.image.load("bullet(1).png").convert()
            self.spritesbullet.set_colorkey(0,0)
    def checkKeys(self):
        keys=pygame.key.get_pressed() 
        if keys[pygame.K_q]: self.fps+=5
        elif keys[pygame.K_a]: self.fps-=5
        elif keys[pygame.K_RIGHT]: self.ship.direction="RIGTH"
        elif keys[pygame.K_LEFT]: self.ship.direction="LEFT"
        elif keys[pygame.K_w]: self.bullet.state="Shooting up"
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
                
                if self.ship.x > self.witdh-64 : self.ship.x=self.witdh-64
                if self.ship.x < self.witdh-790 : self.ship.x=self.witdh-790
                
                if self.bullet.ybullet > self.heigth:
                    self.bullet.ybullet=self.ship.y
                
                self.checkKeys() 
                self.ship.move()   
                self.mySky.move()
                self.bullet.shoot()
                x=self.ship.x
                y=self.heigth-100

                self.screen.blit(self.shipsprite, (x,y))
                self.screen.blit(self.spritesbullet, (x+6, self.bullet.ybullet-45))
                self.clock.tick(self.fps)
                
                
                pygame.display.flip()

                
myGame=Game()
myGame.run()
