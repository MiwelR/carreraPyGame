import pygame, sys
from pygame.locals import *
import random

class Car():
    __customes = ('Audi', 'Viper', 'Police', 'Truck', 'Taxi')
    
    
    def __init__(self, x=0, y=0):
        ixCustome = random.randint(0, 4)
        
        self.custome = pygame.image.load("images/{}.png".format(self.__customes[ixCustome]))
        self.position = [x, y]
        self.name = ""
        
class Game():
    def __init__(self):
        self.__screen = pygame.display.set_mode((640, 480))
        self.__background = pygame.image.load("images/background.png")
        pygame.display.set_caption("Carrera de coches")

        self.car = Car(320, 240)
        
    def start(self):
        gameOver = False
        while not gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_UP:
                        # Mover hacia arriba car
                        self.car.position[1] -= 5
                        
                    elif event.key == K_DOWN:
                        # Mover hacia abajo car
                        self.car.position[1] += 5
                        
                    elif event.key == K_LEFT:
                        # Mover hacia la izquierda
                        self.car.position[0] -= 5
                        
                    elif event.key == K_RIGHT:
                        # Mover hacia la derecha
                        self.car.position[0] += 5
                        
                    else:
                        pass
                    
            self.__screen.blit(self.__background, (0, 0))
            self.__screen.blit(self.car.custome, self.car.position)
            
            pygame.display.flip()
            
if __name__ == '__main__':
    game = Game()
    pygame.init()
    game.start()
                    
        