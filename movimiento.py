import pygame, sys
from pygame.locals import *

class Runner():
    __carTex = ('coche','camaro','crazy','futuro','rosita')
    
    def __init__(self,x=0,y=0,tex=0):
        self.skin = pygame.image.load('images/{}.png'.format(self.__carTex[tex]))
        self.skin = pygame.transform.flip(self.skin, True, False)
        self.skin = pygame.transform.rotozoom(self.skin,0,0.16) # self.custom.convert_alpha()
        self.position = [x,y]
        self.name = self.__carTex[tex]
        
class Game():
    def __init__(self,width=640,height=480):
        self.__screen = pygame.display.set_mode((width,height))
        self.__background = pygame.image.load('images/background.png')
        self.__startLine = 2*(width/100)
        self.__finishLine = width-(20*(width/100))
        pygame.display.set_caption('Carrera de coches')
        
        self.default_car = Runner(self.__startLine,(height/2)-(height/10))
        
    def close(self):
        pygame.quit()
        sys.exit()
        
    def start(self):
        gameOver = False
        while not gameOver:
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT: #if event.type == pygame.
                    close(self)
                elif event.type == KEYDOWN:
                    if event.key == K_UP:
                        self.default_car.position [1] -= 5
                    elif event.key == K_DOWN:
                        self.default_car.position [1] += 5
                    elif event.key == K_LEFT:
                        self.default_car.position [0] -= 5
                    elif event.key == K_RIGHT:
                        self.default_car.position [0] += 5
                    else:
                        pass
            self.__screen.blit(self.__background,(0,0)) #renderiza pantalla
            self.__screen.blit(self.default_car.skin,self.default_car.position) #renderiza personaje
            pygame.display.flip()
            
if __name__ == '__main__':
    pygame.init()
    game = Game()
    game.start()