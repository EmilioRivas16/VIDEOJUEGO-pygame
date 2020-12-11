import pygame

class Tubos_Abajo(pygame.sprite.Sprite):
    def __init__(self,position):
        pygame.sprite.Sprite.__init__(self)
        self.sheet = pygame.image.load("IMAGENES_VIDEOJUEGO/TS1_ABAJO3.png").convert_alpha()
        self.images = [pygame.image.load("IMAGENES_VIDEOJUEGO/TS1_ABAJO3.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/TS1_ABAJO3.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/TS2_ABAJO3.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/TS2_ABAJO3.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/TS3_ABAJO3.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/TS3_ABAJO3.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/TS4_ABAJO3.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/TS4_ABAJO3.png").convert_alpha()]
        self.current_image = 0
        self.image = pygame.image.load("IMAGENES_VIDEOJUEGO/TS4_ABAJO3.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = position

    def update(self,event):
        self.current_image = (self.current_image + 1) % 8
        self.image = self.images[self.current_image]
        self.image == self.sheet.subsurface(self.sheet.get_clip())


class Tubos_Arriba(pygame.sprite.Sprite):
    def __init__(self,position):
        pygame.sprite.Sprite.__init__(self)
        self.sheet = pygame.image.load("IMAGENES_VIDEOJUEGO/TS1_ARRIBA3.png").convert_alpha()
        self.images = [pygame.image.load("IMAGENES_VIDEOJUEGO/TS1_ARRIBA3.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/TS1_ARRIBA3.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/TS2_ARRIBA3.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/TS2_ARRIBA3.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/TS3_ARRIBA3.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/TS3_ARRIBA3.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/TS4_ARRIBA3.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/TS4_ARRIBA3.png").convert_alpha()]
        self.current_image = 0
        self.image = pygame.image.load("IMAGENES_VIDEOJUEGO/TS4_ARRIBA3.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = position

    def update(self,event):
        self.current_image = (self.current_image + 1) % 8
        self.image = self.images[self.current_image]
        self.image == self.sheet.subsurface(self.sheet.get_clip())
