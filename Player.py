import math

import pygame
from GameConfig import *
from Mode import *
from Weapons.Grenade import *


class Player(pygame.sprite.Sprite) :

    LEFT = -1
    RIGHT = 1
    NONE = 0


    def __init__(self, x) :
        self.rect = pygame.Rect(
            x,
            GameConfig.Y_PLATEFORM - GameConfig.PLAYER_H,
            GameConfig.PLAYER_W,
            GameConfig.PLAYER_H
        )

        self.sprite_count = 0
        self.direction = Player.NONE

        self.image = Player.IMAGES[self.direction][
            self.sprite_count//GameConfig.NB_FRAMES_PER_SPRITE_PLAYER
        ]
        self.arrow_image = GameConfig.ARROW_IMG
        self.vx = 0
        self.vy = 0

        self.mask = Player.MASKS[self.direction][
            self.sprite_count//GameConfig.NB_FRAMES_PER_SPRITE_PLAYER
        ]

        self.arrow_angle = GameConfig.ARROW_ANGLE

        self.progressBar = GameConfig.PROGRESS_BAR_IMG



    def init_sprites():
        Player.IMAGES = {
            Player.LEFT: GameConfig.WALK_LEFT_IMG,
            Player.RIGHT: GameConfig.WALK_RIGHT_IMG,
            Player.NONE: GameConfig.STANDING_IMG,
        }
        Player.MASKS = {
            Player.LEFT: GameConfig.WALK_LEFT_MASKS,
            Player.RIGHT: GameConfig.WALK_RIGHT_MASKS,
            Player.NONE: GameConfig.STANDING_MASK,
        }


    def draw(self, window) :
        window.blit(self.image, (self.rect.left + 35, self.rect.top))
        if Mode.fire_mode:
            window.blit(self.arrow_image, (self.rect.centerx - int((self.arrow_image.get_width() / 2) - 35),
                                           self.rect.centery - int(self.arrow_image.get_height()) / 2))
            window.blit(self.progressBar, (self.rect.left, self.rect.bottom + 10))



    def on_ground(self) :
        return self.rect.bottom == GameConfig.Y_PLATEFORM

    def rot_center(self, image, angle):
        w, h = image.get_size()
        box = [pygame.math.Vector2(p) for p in [(0, 0), (w, 0), (w, -h), (0, -h)]]
        box_rotate = [p.rotate(angle) for p in box]
        pivot = pygame.math.Vector2(w / 2, -h / 2)
        pivot_rotate = pivot.rotate(angle)
        pivot_move = pivot_rotate - pivot
        min_box = (min(box_rotate, key=lambda p: p[0])[0], min(box_rotate, key=lambda p: p[1])[1])
        max_box = (max(box_rotate, key=lambda p: p[0])[0], max(box_rotate, key=lambda p: p[1])[1])
        origin = (self.rect.left + min_box[0] - pivot_move[0], self.rect.top - max_box[1] + pivot_move[1])
        rotated_image = pygame.transform.rotate(image, angle)
        self.arrow_image = rotated_image
        self.arrow_image.get_rect().move(origin)
        pygame.display.flip()

    def advance_state(self, next_move, window):
        # Acceleration
        fx = 0
        fy = 0
        if next_move.left:
            fx = GameConfig.FORCE_LEFT
            self.direction = Player.LEFT
        elif next_move.right:
            fx = GameConfig.FORCE_RIGHT
            self.direction = Player.RIGHT
        else:
            self.direction = Player.NONE
        if next_move.arrow_left:
            self.arrow_image = GameConfig.ARROW_IMG
            self.arrow_angle += 4
            self.rot_center(self.arrow_image, self.arrow_angle)
        if next_move.power_plus:
            if self.progressBar.get_width() < self.arrow_image.get_width():
                self.progressBar = pygame.transform.scale(self.progressBar,
                                                            (self.progressBar.get_width() + 5,
                                                            self.progressBar.get_height()))
        if next_move.power_minus:
            if self.progressBar.get_width() > 10:
                self.progressBar = pygame.transform.scale(self.progressBar,
                                                            (self.progressBar.get_width() - 5,
                                                            self.progressBar.get_height()))
        if next_move.arrow_right:
            self.arrow_image = GameConfig.ARROW_IMG
            self.arrow_angle -= 4
            self.rot_center(self.arrow_image, self.arrow_angle)
        self.sprite_count += 1
        if self.sprite_count >= GameConfig.NB_FRAMES_PER_SPRITE_PLAYER*len(Player.IMAGES[self.direction]):
            self.sprite_count = 0
        self.image = Player.IMAGES[self.direction][
            self.sprite_count // GameConfig.NB_FRAMES_PER_SPRITE_PLAYER
        ]
        self.mask = Player.MASKS[self.direction][
            self.sprite_count // GameConfig.NB_FRAMES_PER_SPRITE_PLAYER
        ]

        if next_move.jump:
            fy = GameConfig.FORCE_JUMP
        # Vitesse
        self.vx = fx * GameConfig.DT
        if self.on_ground():
            self.vy = fy*GameConfig.DT
        else :
            self.vy = self.vy+GameConfig.GRAVITY*GameConfig.DT
        y = self.rect.top
        vy_max = (GameConfig.Y_PLATEFORM-GameConfig.PLAYER_H-y)/GameConfig.DT
        self.vy = min(self.vy,vy_max)
        # Position
        x = self.rect.left
        vx_min = -x / GameConfig.DT
        vx_max = (GameConfig.WINDOW_W - GameConfig.PLAYER_W - x) / GameConfig.DT
        self.vx = min(self.vx, vx_max)
        self.vx = max(self.vx, vx_min)
        self.rect = self.rect.move(self.vx * GameConfig.DT, self.vy * GameConfig.DT)
