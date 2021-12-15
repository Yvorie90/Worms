import pygame
from game_config import *

class Player(pygame.sprite.Sprite):

    def __init__(self, x):
        self.rect = pygame.Rect(x, GameConfig.Y_GROUND - GameConfig.PLAYER_H, GameConfig.PLAYER_W, GameConfig.PLAYER_H)
        self.image = GameConfig.P1_IMG

    def draw(self, window):
        window.blit(self.image, self.rect.topleft)

    def on_ground(self):
        return self.rect.bottom == GameConfig.Y_GROUND # futur fonction qui a X associe le Y du sol

    def advanceState(self, next_move):
        return 0


