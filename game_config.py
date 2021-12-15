import pygame

class GameConfig:
    WINDOW_H = 640
    WINDOW_W = 960
    Y_GROUND = 516
    GRAVITY = 9.81
    DT = 0.5
    PLAYER_W = 64
    PLAYER_H = 64



    def init():
        GameConfig.BG = pygame.image.load('assets/Background_1.png')
        GameConfig.P1_IMG = pygame.image.load("assets/Background_1.png")


