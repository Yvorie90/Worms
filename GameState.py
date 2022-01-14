import random

from Player import *
import math

class GameState :
    def __init__(self) :
        #list
        self.player = Player(20)
        self.weapon = None
        self.truc = False

        self.wind_direction = GameConfig.WIND_DIRECTION
        self.wind_power = GameConfig.WIND_POWER
        self.wind_arrow = GameConfig.ARROW_IMG

        self.wind_counter = 0

    def draw(self, window):
        window.blit(GameConfig.BACKGROUND_IMG, (0, 0))
        window.blit(self.wind_arrow, (0, 0))

    # Même code que dans Player
    def rot_center(self, image, angle):
        w, h = image.get_size()
        box = [pygame.math.Vector2(p) for p in [(0, 0), (w, 0), (w, -h), (0, -h)]]
        box_rotate = [p.rotate(angle) for p in box]
        pivot = pygame.math.Vector2(w / 2, -h / 2)
        pivot_rotate = pivot.rotate(angle)
        pivot_move = pivot_rotate - pivot
        min_box = (min(box_rotate, key=lambda p: p[0])[0], min(box_rotate, key=lambda p: p[1])[1])
        max_box = (max(box_rotate, key=lambda p: p[0])[0], max(box_rotate, key=lambda p: p[1])[1])
        origin = (0, 0)
        rotated_image = pygame.transform.rotate(image, angle)
        self.arrow_image = rotated_image
        # self.arrow_image.get_rect().move(origin)
        pygame.display.flip()

    def random_wind(self):
        randwind = random.randint(0, 1)
        randpowwind = random.randint(0, 1)
        if randwind == 0 and self.wind_direction < 360:
            self.wind_direction += random.randint(1, 100)
        if randwind == 1 and self.wind_direction > 0:
            self.wind_direction -= random.randint(1, 100)
            if self.wind_direction < 0:
                self.wind_direction = 0
        if randpowwind == 0 and self.wind_power < 100:
            self.wind_power += random.randint(1, 100)
            if self.wind_power > 100:
                self.wind_power = 100
        if randpowwind == 1 and self.wind_power > 0:
            self.wind_power -= random.randint(1, 100)
            if self.wind_power < 0:
                self.wind_power = 0

        self.wind_arrow = GameConfig.ARROW_IMG
        pygame.transform.rotate(self.wind_arrow, self.wind_direction - 45)
        # self.rot_center(self.wind_arrow, self.wind_direction - 45)


    def advance_state(self,next_move, window) :
        if self.wind_counter == 300:
            self.random_wind()
            self.wind_counter = 0
            print(self.wind_direction, self.wind_power)
        self.player.advance_state(next_move, window)
        if next_move.fire :
            self.truc = True
        if self.truc:

            if self.weapon == None :
                self.weapon = Grenade(self.player)
                self.weapon.advance_state(
                    math.sin((self.player.arrow_angle - 45) * (math.pi / 180)) * -self.player.progressBar.get_width(),
                    math.cos((self.player.arrow_angle - 45) * (math.pi / 180)) * -self.player.progressBar.get_width(),
                    math.sin((self.wind_direction - 45) * (math.pi / 180)) * -self.wind_power,
                    math.cos((self.wind_direction - 45) * (math.pi / 180)) * -self.wind_power
                )

            self.weapon.draw(window)
            self.weapon.advance_state(
                math.sin((self.wind_direction - 45) * (math.pi / 180)) * -self.wind_power,
                math.cos((self.wind_direction - 45) * (math.pi / 180)) * -self.wind_power,
                math.sin((self.wind_direction - 45) * (math.pi / 180)) * -self.wind_power,
                math.cos((self.wind_direction - 45) * (math.pi / 180)) * -self.wind_power
            )

            if not self.weapon.exist :
                self.weapon = None
                self.truc = False
        self.wind_counter += 1