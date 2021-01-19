import pygame, sys
import random

class Runner():
    __carTex = ('coche','camaro','crazy','futuro','rosita')
      
    def __init__(self,x=0,y=0,tex=0):
        self.skin = pygame.image.load('images/{}.png'.format(self.__carTex[tex]))
        self.skin = pygame.transform.flip(self.skin, True, False)
        self.skin = pygame.transform.rotozoom(self.skin,0,0.16) # self.custom.convert_alpha()
        self.position = [x,y]
        self.name = self.__carTex[tex]
    
    def avanza(self):
        self.position [0] += random.randint(1,10)
        
class Game():
    runners = []
    players = 4
    __carTex = ('camaro','crazy','futuro','rosita','coche')
    
    def __init__(self,width=640,height=480):
        self.__screen = pygame.display.set_mode((width,height))
        self.__background = pygame.image.load('images/background.png')
        self.__startLine = 2*(width/100)
        self.__finishLine = width-(20*(width/100))
        pygame.display.set_caption('Carrera de coches')
        
        self.default_car = Runner(self.__startLine,(height/2)-(height/10))
        
        for i in range(self.players):
            newRunner = Runner(self.__startLine,((height/(self.players+1))*(i+1))-(height/10),i+1)
            self.runners.append(newRunner)
            
    def close(self):
        pygame.quit()
        sys.exit()
        
    def competir(self):
        timer_event = pygame.USEREVENT + 1
        pygame.time.set_timer(timer_event,1)
        gameOver = False
        
        while not gameOver:
            #comprobacion de eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT: #if event.type == pygame.
                    gameOver = True
                if event.type == timer_event and not gameOver:
                    self.__screen.blit(self.__background,(0,0)) #renderiza pantalla
                    #self.__screen.blit(self.default_car.skin,self.default_car.position)
                    #self.default_car.avanza()
                    for runner in self.runners:
                        self.__screen.blit(runner.skin,runner.position)
                        if runner.position[0] < self.__finishLine and not gameOver:
                            runner.avanza()
                        if runner.position[0] >= self.__finishLine and not gameOver:
                            print('{} ha ganado!'.format(runner.name))
                            gameOver = True
                pygame.display.flip()
                
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: #if event.type == pygame.
                    self.close()
              
if __name__ == '__main__':
    pygame.init()
    game = Game()
    game.competir()