import pygame.image


class GameConfig :

    # Constantes du jeu

    # Initialisation de la classe

    def init():
        GameConfig.BACKGROUND_IMG = pygame.image.load("Ressources/Assets/background.png")
        GameConfig.WALK_RIGHT_IMG = [
            pygame.image.load('Ressources/Assets/R' + str(i) + '.png').convert_alpha() for i in range(1, 10)
        ]
        GameConfig.WALK_LEFT_IMG = [
            pygame.image.load('Ressources/Assets/L' + str(i) + '.png').convert_alpha() for i in range(1, 10)
        ]
        GameConfig.STANDING_IMG = [
            pygame.image.load('Ressources/Assets/standing.png').convert_alpha()
        ]
        GameConfig.WALK_RIGHT_MASKS = [
            pygame.mask.from_surface(im) for im in GameConfig.WALK_RIGHT_IMG
        ]
        GameConfig.WALK_LEFT_MASKS = [
            pygame.mask.from_surface(im) for im in GameConfig.WALK_LEFT_IMG
        ]
        GameConfig.STANDING_MASK = [
            pygame.mask.from_surface(GameConfig.STANDING_IMG[0])
        ]

    # Taille de l'écran

    WINDOW_H = 640
    WINDOW_W = 960

    # Ordonnée du joueur

    Y_PLATEFORM = 516

    # Définition du rectangle du joueur

    PLAYER_W = 64
    PLAYER_H = 64

    # Constantes déplacement joueur

    DT = 0.5
    FORCE_LEFT = -20
    FORCE_RIGHT = -FORCE_LEFT

    # Canstantes de saut

    GRAVITY = 9.81
    FORCE_JUMP = -100

    # Animations

    NB_FRAMES_PER_SPRITE_PLAYER = 2

    # Puissance

    MAX_POWER = 100

    # Flèche de tir

    ARROW_IMG = pygame.image.load("Ressources/Assets/Arrow.png")
    ARROW_ANGLE = 0

    # Grenade

    GRENADE_IMG = pygame.image.load("Ressources/Assets/R1.png")
    GRENADE_RANGE = 10
    GRENADE_DEGATS = 5
    GRENADE_H = 16
    GRENADE_W = 16

    # Progress Bar

    PROGRESS_BAR_IMG = pygame.image.load("Ressources/Assets/ProgressBarItem.png")


