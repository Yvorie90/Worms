from GameConfig import *
from Weapons import Weapons



class FusilAPompe(Weapons.Weapons):

    def __init__(self, player):
        self.rect = pygame.Rect(
            player.rect.right,
            player.rect.top,
            GameConfig.PLAYER_W,
            GameConfig.PLAYER_H
        )

        self.vx = 0
        self.vy = 0
        self.exist = True


        self.fragmentation = False

        self.range = GameConfig.GRENADE_RANGE
        self.degats = GameConfig.GRENADE_DEGATS
        self.image = GameConfig.GRENADE_IMG

        self.initfx = 0
        self.initfy = 0

    def on_ground(self) :
        return self.rect.bottom == GameConfig.Y_PLATEFORM

    def draw(self, window):
        window.blit(self.image, (self.rect.left, self.rect.top))

    def advance_state(self, fx, fy, wind_x, wind_y):
        if not fx == wind_x:
            self.initfx = fx
        if not fy == wind_y:
            self.initfy = fy

        self.vx = self.initfx
        self.vy = self.initfy
        # Vitesse
        if self.vx >= 100 and self.on_ground():
            self.exist = False


        else:
            self.exist = True
            # self.vy = self.vy + GameConfig.GRAVITY * GameConfig.DT
            self.vx = self.vx + fx * GameConfig.DT
        y = self.rect.top
        vy_max = (GameConfig.Y_PLATEFORM - GameConfig.PLAYER_H - y) / GameConfig.DT
        self.vy = min(self.vy, vy_max)
        # Position
        x = self.rect.left
        # vx_min = -x / GameConfig.DT
        # vx_max = (GameConfig.WINDOW_W - GameConfig.PLAYER_W - x) / GameConfig.DT
        # self.vx = min(self.vx, vx_max)
        # self.vx = max(self.vx, vx_min)
        self.rect = self.rect.move(self.vx * GameConfig.DT, self.vy * GameConfig.DT)