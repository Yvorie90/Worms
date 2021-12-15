from game_config import *
from modeles.player import *


class GameState:
    def __init__(self):
        self.player = Player(20)


    def draw(self, window):
        window.blit(GameConfig.BG, (0,0))
        self.player.draw(window)

    def advanceState(self,next_move):
        self.player.advanceState(next_move)