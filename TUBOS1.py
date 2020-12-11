import pygame

class Tubos():
    def __init__(self,position):
        self.sheet = pygame.image.load("IMAGENES_VIDEOJUEGO/tubo_verde_abajo.png")
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.grados = 0

    def rotar(self):
        rotar = pygame.transform.rotate(self.sheet,self.grados)
        rect = rotar.get_rect()
        self.rect.center = rect.center
        self.grados += 0

class Tubos_Abajo(pygame.sprite.Sprite):
    def __init__(self,position):
        pygame.sprite.Sprite.__init__(self)
        self.sheet = pygame.image.load("IMAGENES_VIDEOJUEGO/TS1_ABAJO.png").convert_alpha()
        self.images = [pygame.image.load("IMAGENES_VIDEOJUEGO/TS1_ABAJO.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/TS1_ABAJO.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/TS2_ABAJO.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/TS2_ABAJO.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/TS3_ABAJO.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/TS3_ABAJO.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/TS4_ABAJO.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/TS4_ABAJO.png").convert_alpha()]
        self.current_image = 0
        self.image = pygame.image.load("IMAGENES_VIDEOJUEGO/TS4_ABAJO.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = position

    def update(self,event):
        self.current_image = (self.current_image + 1) % 8
        self.image = self.images[self.current_image]
        self.image == self.sheet.subsurface(self.sheet.get_clip())


class Tubos_Arriba(pygame.sprite.Sprite):
    def __init__(self,position):
        pygame.sprite.Sprite.__init__(self)
        self.sheet = pygame.image.load("IMAGENES_VIDEOJUEGO/TS1_ARRIBA.png").convert_alpha()
        self.images = [pygame.image.load("IMAGENES_VIDEOJUEGO/TS1_ARRIBA.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/TS1_ARRIBA.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/TS2_ARRIBA.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/TS2_ARRIBA.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/TS3_ARRIBA.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/TS3_ARRIBA.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/TS4_ARRIBA.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/TS4_ARRIBA.png").convert_alpha()]
        self.current_image = 0
        self.image = pygame.image.load("IMAGENES_VIDEOJUEGO/TS4_ARRIBA.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = position

    def update(self,event):
        self.current_image = (self.current_image + 1) % 8
        self.image = self.images[self.current_image]
        self.image == self.sheet.subsurface(self.sheet.get_clip())
