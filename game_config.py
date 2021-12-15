import pygame

class GameConfig:
    WINDOW_W = 640
    WINDOW_H = 960
    Y_GROUND = 516
    GRAVITY = 9.81
    DT = 0.5


    def init():
        GameConfig.BG = pygame.image.load('assets/...')


