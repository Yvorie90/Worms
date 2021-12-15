import pygame
from game_state import *
from modeles.move import *

def getNextMove():
    next_move = Move()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        next_move.right = True
    if keys[pygame.K_LEFT]:
        next_move.left = True
    if keys[pygame.K_RETURN]:
        next_move.jump = True

    return next_move


def gameloop(window, horloge):
    quit = False
    gameState = GameState()
    while not quit:
        horloge.tick(120)
        gameState.draw(window)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit = True

        gameState.advanceState(getNextMove())
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
