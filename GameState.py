from Player import *
import math

class GameState :
    def __init__(self) :
        #list
        self.player = Player(20)
        self.weapon = None
        self.truc = False

    def draw(self, window):
        window.blit(GameConfig.BACKGROUND_IMG, (0, 0))


    def advance_state(self,next_move, window) :
        self.player.advance_state(next_move, window)
        if next_move.fire :
            self.truc = True
        if self.truc:

            if self.weapon == None :
                self.weapon = Grenade(self.player)
                self.weapon.advance_state(
                    math.sin((self.player.arrow_angle - 45) * (math.pi / 180)) * -self.player.progressBar.get_width(),
                    math.cos((self.player.arrow_angle - 45) * (math.pi / 180)) * -self.player.progressBar.get_width()
                )

            self.weapon.draw(window)
            self.weapon.advance_state(0,0)

            if not self.weapon.exist :
                self.weapon = None
                self.truc = False
