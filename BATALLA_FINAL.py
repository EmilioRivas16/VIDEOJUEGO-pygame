import pygame

class Boss1():
    def __init__(self,position):
        self.sheet = pygame.image.load("IMAGENES_VIDEOJUEGO/MARIO_VINTAGE_2.png")
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position

class Boss1_MUERTO():
    def __init__(self,position):
        self.sheet = pygame.image.load("IMAGENES_VIDEOJUEGO/MARIO_VINTAGE_2_MUERTO.png")
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position

class Boss2():
    def __init__(self,position):
        self.sheet = pygame.image.load("IMAGENES_VIDEOJUEGO/ROCA(VINTAGE)4.png")
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position

class Boss2_MUERTO():
    def __init__(self,position):
        self.sheet = pygame.image.load("IMAGENES_VIDEOJUEGO/ROCA_VINTAGE_4_MUERTO.png")
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position

class Boss3():
    def __init__(self,position):
        self.sheet = pygame.image.load("IMAGENES_VIDEOJUEGO/BOWSER(VINTAGE)3.png")
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position

class Boss3_MUERTO():
    def __init__(self,position):
        self.sheet = pygame.image.load("IMAGENES_VIDEOJUEGO/BOWSER_VINTAGE_3_MUERTO.png")
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position

class Boss3_VOLTEADO():
    def __init__(self,position):
        self.sheet = pygame.image.load("IMAGENES_VIDEOJUEGO/BOWSER_VOLTEADO.png")
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position

class PROYECTIL_MARIO():
    def __init__(self, position):
        self.sheet = pygame.image.load("IMAGENES_VIDEOJUEGO/bola_fuego4.png").convert_alpha()
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position

class PROYECTIL_MARIO_VOLTEADO():
    def __init__(self, position):
        self.sheet = pygame.image.load("IMAGENES_VIDEOJUEGO/bola_fuego4v.png").convert_alpha()
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position

class PROYECTIL_ROCA():
    def __init__(self, position):
        self.sheet = pygame.image.load("IMAGENES_VIDEOJUEGO/roca_proyectil.png").convert_alpha()
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position

class PROYECTIL_BOWSER():
    def __init__(self, position):
        self.sheet = pygame.image.load("IMAGENES_VIDEOJUEGO/FUEGO_BOWSER2.png").convert_alpha()
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position

class BUM():
    def __init__(self, position):
        self.sheet = pygame.image.load("IMAGENES_VIDEOJUEGO/bum.png").convert_alpha()
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position

class ASTEROIDE():
    def __init__(self, position):
        self.sheet = pygame.image.load("IMAGENES_VIDEOJUEGO/ASTEROIDE2.png").convert_alpha()
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position

class HONGO():
    def __init__(self, position):
        self.sheet = pygame.image.load("IMAGENES_VIDEOJUEGO/HONGO2.png").convert_alpha()
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position

class RELOJ_BATALLAFINAL():
    def __init__(self, position):
        self.sheet = pygame.image.load("IMAGENES_VIDEOJUEGO/RELOJ.png").convert_alpha()
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position
