import pygame
from Worms.game_config import *
from Worms.modeles.weapons.weapon import *
from Worms.modeles.weapons.grenade import *


class Player(pygame.sprite.Sprite):

    def __init__(self, x):
        self.rect = pygame.Rect(x, GameConfig.Y_GROUND - GameConfig.PLAYER_H, GameConfig.PLAYER_W, GameConfig.PLAYER_H)
        self.image = GameConfig.P1_IMG
        self.vx = 0
        self.vy = 0
        self.wpon = 0 # 0 = pas d'arme

    def draw(self, window):
        window.blit(self.image, self.rect.topleft)

    def on_ground(self):
        return self.rect.bottom == GameConfig.Y_GROUND # futur fonction qui a X associe le Y du sol

    def advanceState(self, next_move):
        fx = 0
        fy = 0
        if next_move.left:
            fx = -20
        if next_move.right:
            fx = 20
        if next_move.right and next_move.left:
            fx = 0
        if next_move.jump:
            fy = -100

        self.vx = fx * GameConfig.DT
        if self.on_ground():
            self.vy = fy * GameConfig.DT
        else:
            self.vy = self.vy + GameConfig.GRAVITY * GameConfig.DT

        x = self.rect.left
        vx_min = -x / GameConfig.DT
        vx_max = (GameConfig.WINDOW_W - GameConfig.PLAYER_W - x) / GameConfig.DT

        y = self.rect.top
        vy_max = (GameConfig.Y_GROUND - GameConfig.PLAYER_H - y) / GameConfig.DT

        self.vx = min(self.vx, vx_max)
        self.vx = max(self.vx, vx_min)

        self.vy = min(self.vy, vy_max)

        self.rect = self.rect.move(self.vx * GameConfig.DT, self.vy * GameConfig.DT)

    def lancer_pojectile(self):
        pojectil = Grenade()

