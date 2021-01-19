import pygame, sys
import random

class Runner():
    
    def __init__(self,x=0,y=0):
        self.custom = pygame.image.load('images/pngwing.com.png')
        self.custom = pygame.transform.flip(self.custom, True, False)
        self.custom = pygame.transform.rotozoom(self.custom,0,0.1) # self.custom.convert_alpha()
        self.position = [x,y]
        self.name = 'coche'
    
    def avanza(self):
        self.position [0] += random.randint(1,10)
        
class Game():
    runners = []
    __carTex = ('images/pngwing.com.png','images/pngwing.com.png','images/pngwing.com.png','images/pngwing.com.png')
    
    def __init__(self,width=640,height=480):
        self.__screen = pygame.display.set_mode((width,height))
        self.__background = pygame.image.load('images/background.png')
        self.__startLine = 2*(width/100)
        self.__finishLine = width-(20*(width/100))
        pygame.display.set_caption('Carrera de coches')
        
        self.__creaRunners(height/4)
        
        #firstRunner = Runner(self.__startLine,height/5)
        #firstRunner.name = 'Speedy'
        #self.runners.append(firstRunner)
      
    def competir(self):
        gameOver = False
        first = [-(self.__finishLine),'']
        while not gameOver:
            #comprobacion de eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT: #if event.type == pygame.
                    gameOver = True
                for runner in self.runners:
                    if runner.position[0] > first[0]:
                        first[0] = runner.position[0]
                        first[1] = runner.name
                    if first[0] >= self.__finishLine:
                        print('{} ha ganado!'.format(first[1]))
                        gameOver = True
                    runner.avanza()
                    self.__screen.blit(self.__background,(0,0)) #renderiza pantalla
                    self.__screen.blit(runner.custom,runner.position)
                    pygame.display.flip()

    def __creaRunners(self,posY):
        for i in range(4):
            newRunner = Runner(self.__startLine,posY*(i+1))
            newRunner.custom = pygame.image.load(self.__carTex[i])
            if self.__carTex[i] == 'images/pngwing.com.png':
                newRunner.custom = pygame.transform.flip(newRunner.custom, True, False)
                newRunner.custom = pygame.transform.rotozoom(newRunner.custom,0,0.12) # self.custom.convert_alpha()
            self.runners.append(newRunner)
         
if __name__ == '__main__':
    pygame.init()
    game = Game()
    game.competir()