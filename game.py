import pygame
from game_config import GameConfig





def gameloop(window):
    quit = False






if __name__ == '__main__':
    pygame.init()
    horloge = pygame.time.Clock()
    window = pygame.display.set_mode(GameConfig.WINDOW_W,GameConfig.WINDOW_H)
    pygame.display.set_caption("Worms du pauvre")
