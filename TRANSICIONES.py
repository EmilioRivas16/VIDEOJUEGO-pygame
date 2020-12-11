import pygame

class RELOJ_TRAN_TUBOS_BOSS_NVL1():
    def __init__(self, position):
        self.sheet = pygame.image.load("IMAGENES_VIDEOJUEGO/RELOJ.png").convert_alpha()
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position

class RELOJ_TRAN_TUBOS_BOSS_NVL2():
    def __init__(self, position):
        self.sheet = pygame.image.load("IMAGENES_VIDEOJUEGO/RELOJ.png").convert_alpha()
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position

class RELOJ_TRAN_TUBOS_BOSS_NVL3():
    def __init__(self, position):
        self.sheet = pygame.image.load("IMAGENES_VIDEOJUEGO/RELOJ.png").convert_alpha()
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position

class RELOJ_TRAN_MENU_TUBOS():
    def __init__(self, position):
        self.sheet = pygame.image.load("IMAGENES_VIDEOJUEGO/1.png").convert_alpha()
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position
