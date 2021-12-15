import pygame
from game_state import *


def getNextMove():
    next_move = Move()

def gameloop(window, horloge):
    quit = False
    gameState = GameState()
    while not quit:
        horloge.tick(120)
        gameState.draw(window)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit = True

        #gameState.advanceState(getNextMove())
        pygame.time.delay(20)
        pygame.display.update()



if __name__ == '__main__':
    pygame.init()
    horloge = pygame.time.Clock()
    window = pygame.display.set_mode((GameConfig.WINDOW_W,GameConfig.WINDOW_H))
    pygame.display.set_caption("Worms du pauvre")
    GameConfig.init()
    #loop menu et restart
    gameloop(window, horloge)
