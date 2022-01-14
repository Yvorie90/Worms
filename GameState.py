import random

from Player import *
import math

from Weapons.Bazooka import Bazooka
from Weapons.FusilAPompe import FusilAPompe


class GameState :
    def __init__(self) :
        self.player = Player(20)
        self.weapon = None
        self.truc = False

        self.wind_direction = GameConfig.WIND_DIRECTION
        self.wind_power = GameConfig.WIND_POWER

        self.wind_counter = 0

        self.explode = GameConfig.EXPLOSION

    def draw(self, window):
        window.blit(GameConfig.BACKGROUND_IMG, (0, 0))
        font = pygame.font.Font('Ressources/Assets/BradBunR.ttf', 20)
        text = "Wind direction : %d°" %self.wind_direction
        img = font.render(text, True, (0, 0, 0))
        displayRect = img.get_rect()
        displayRect.center = (79, 20)
        window.blit(img, displayRect)

        text = "Wind power : %d km/h" % (self.wind_power*5)
        img = font.render(text, True, (0, 0, 0))
        displayRect = img.get_rect()
        displayRect.center = (80, 40)
        window.blit(img, displayRect)


    def random_wind(self):
        randwind = random.randint(0, 1)
        randpowwind = random.randint(0, 1)
        if randwind == 0 and self.wind_direction < 360:
            self.wind_direction += random.randint(1, 100)
        if randwind == 1 and self.wind_direction > 0:
            self.wind_direction -= random.randint(1, 100)
            if self.wind_direction < 0:
                self.wind_direction = 0
        if randpowwind == 0 and self.wind_power < 30:
            self.wind_power += random.randint(1, 5)
            if self.wind_power > 100:
                self.wind_power = 100
        if randpowwind == 1 and self.wind_power > 0:
            self.wind_power -= random.randint(1, 5)
            if self.wind_power < 0:
                self.wind_power = 0




    def advance_state(self,next_move, window) :
        if self.wind_counter == 300:
            self.random_wind()
            self.wind_counter = 0
            print(self.wind_direction, self.wind_power)
        self.player.advance_state(next_move)
        if next_move.fire :
            self.truc = True
        if next_move.grenade:
            self.truc = False
            self.weapon = None
            self.weapon = Grenade(self.player)
        if next_move.bazooka:
            self.truc = False
            self.weapon = None
            self.weapon = Bazooka(self.player)
        if next_move.pompe:
            self.truc = False
            self.weapon = None
            self.weapon = FusilAPompe(self.player)
        if self.truc:
            if not self.weapon == None:
                if self.weapon.vx == 0 :
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
                    x = self.weapon.rect.copy().left
                    y = self.weapon.rect.copy().top
                    window.blit(self.explode, (x - 50, y - 70))
                    self.weapon = None
                    self.truc = False
            else:
                print("Choisissez une arme avant de tirer !")
                self.truc = False

        self.wind_counter += 1