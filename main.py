import pygame, sys
import random


class Car():
    __customes = ('Audi', 'Viper', 'Police', 'Truck', 'Taxi')
    
    def __init__(self, x=0, y=0):
        ixCustome = random.randint(0, 4)
        
        self.custome = pygame.image.load("images/{}.png".format(self.__customes[ixCustome]))
        self.position = [x, y]
        self.name = ""
        
    def avanzar(self):
        self.position[0] += random.randint(1, 2)


class Game():
    cars = []
    __posY = (120, 160, 200, 240, 280)
    __names = ("Audi", "Viper", "Police", "Truck", "Taxi")
    __startLine = 5
    __finishLine = 620
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((640, 480))
        self.__background = pygame.image.load("images/background.png")
        pygame.display.set_caption("Carrera de coches")
        
        for i in range (5):
            coche = Car(self.__startLine, self.__posY[i])
            coche.name = self.__names[i]
            self.cars.append(coche)
        
    def close(self):
        pygame.quit()
        sys.exit()
    
    def competir(self):
        gameOver = False
        while not gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = True
        
            for carActive in self.cars:
                carActive.avanzar()
                if carActive.position[0] >= self.__finishLine:
                    print("{} ha ganado!".format(carActive.name))
                    gameOver = True
            
            self.__screen.blit(self.__background, (0, 0))
            
            for car in self.cars:
                self.__screen.blit(car.custome, car.position)
           
            
            pygame.display.flip()
            
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.close()
        
        
if __name__ == '__main__':
    game = Game()
    pygame.init()
    game.competir()