import pygame

class GameConfig:
    #window
    WINDOW_H = 640
    WINDOW_W = 960
    #map
    Y_GROUND = 516
    #player
    GRAVITY = 9.81
    DT = 0.5
    PLAYER_W = 64
    PLAYER_H = 64



    def init():
        GameConfig.BG = pygame.image.load('assets/background.png')
        GameConfig.P1_IMG = pygame.image.load("assets/player/p.png")


