from game_config import GameConfig
import pygame

class Weapon(pygame.sprite.Sprite):
    def __init__(self, player):
        self.rect = pygame.Rect()
        self.rect.center = player.rect.center