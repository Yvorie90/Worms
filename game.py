import pygame
from GameConfig import *
from GameState import *
from Move import *
from Mode import *

def get_next_move() :
    next_move = Move()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] :
        next_move.right = True
        Mode.fire_mode = False
    if keys[pygame.K_LEFT] :
        next_move.left = True
        Mode.fire_mode = False
    if keys[pygame.K_RETURN] :
        next_move.jump = True
        Mode.fire_mode = False
    if keys[pygame.K_SPACE]:
        next_move.fire = True
    if keys[pygame.K_DOWN]:
        next_move.arrow_right = True
        Mode.fire_mode = True
    if keys[pygame.K_UP]:
        next_move.arrow_left = True
        Mode.fire_mode = True
    if keys[pygame.K_a]:
        next_move.power_plus = True
    if keys[pygame.K_q]:
        next_move.power_minus = True

    return next_move


def gameloop(window) :
    gameOver = False
    gameState = GameState()

    while not gameOver :
        gameState.draw(window)
        gameState.player.draw(window)
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                gameOver = True
        next_move = get_next_move()
        gameState.advance_state(next_move, window)
        pygame.display.update()
        pygame.time.delay(20)

if __name__ == "__main__" :
    pygame.init()

    window = pygame.display.set_mode(
        (
            GameConfig.WINDOW_W,
            GameConfig.WINDOW_H
        )
    )
    pygame.display.set_caption("Worms")
    GameConfig.init()
    Player.init_sprites()
    gameloop(window)
    pygame.quit()
    quit()