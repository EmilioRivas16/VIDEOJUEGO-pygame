import pygame

class Planeta1():
    def __init__(self,position):
        self.sheet = pygame.image.load("IMAGENES_VIDEOJUEGO/planeta_1.png").convert_alpha()
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position
class Planeta2():
    def __init__(self,position):
        self.sheet = pygame.image.load("IMAGENES_VIDEOJUEGO/planeta_2.png").convert_alpha()
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position
class Planeta3():
    def __init__(self,position):
        self.sheet = pygame.image.load("IMAGENES_VIDEOJUEGO/planeta_3.png").convert_alpha()
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position
class Planeta4():
    def __init__(self,position):
        self.sheet = pygame.image.load("IMAGENES_VIDEOJUEGO/planeta_4.png").convert_alpha()
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position
class Planeta5():
    def __init__(self,position):
        self.sheet = pygame.image.load("IMAGENES_VIDEOJUEGO/planeta_5.png").convert_alpha()
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position
class Planeta6():
    def __init__(self,position):
        self.sheet = pygame.image.load("IMAGENES_VIDEOJUEGO/planeta_6.png").convert_alpha()
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position
class Planeta7():
    def __init__(self,position):
        self.sheet = pygame.image.load("IMAGENES_VIDEOJUEGO/planeta_7.png").convert_alpha()
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position
class Planeta8():
    def __init__(self,position):
        self.sheet = pygame.image.load("IMAGENES_VIDEOJUEGO/planeta_8.png").convert_alpha()
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position




class Pajaro1_Menu(pygame.sprite.Sprite):
    def __init__(self,position):
        pygame.sprite.Sprite.__init__(self)
        self.sheet = pygame.image.load("IMAGENES_VIDEOJUEGO/8.png").convert_alpha()
        self.images = [pygame.image.load("IMAGENES_VIDEOJUEGO/7.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/8.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/9.png").convert_alpha()]
        self.current_image = 0
        self.image = pygame.image.load("IMAGENES_VIDEOJUEGO/7.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = position

    def UPDATE(self, event):
        self.current_image = (self.current_image + 1) % 3
        self.image = self.images[self.current_image]
        self.image == self.sheet.subsurface(self.sheet.get_clip())

class Pajaro2_Menu(pygame.sprite.Sprite):
    def __init__(self,position):
        pygame.sprite.Sprite.__init__(self)
        self.sheet = pygame.image.load("IMAGENES_VIDEOJUEGO/5.png").convert_alpha()
        self.images = [pygame.image.load("IMAGENES_VIDEOJUEGO/4.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/5.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/6.png").convert_alpha()]
        self.current_image = 0
        self.image = pygame.image.load("IMAGENES_VIDEOJUEGO/4.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = position

    def UPDATE(self, event):
        self.current_image = (self.current_image + 1) % 3
        self.image = self.images[self.current_image]
        self.image == self.sheet.subsurface(self.sheet.get_clip())

class Pajaro3_Menu(pygame.sprite.Sprite):
    def __init__(self,position):
        pygame.sprite.Sprite.__init__(self)
        self.sheet = pygame.image.load("IMAGENES_VIDEOJUEGO/11.png").convert_alpha()
        self.images = [pygame.image.load("IMAGENES_VIDEOJUEGO/10.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/11.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/12.png").convert_alpha()]
        self.current_image = 0
        self.image = pygame.image.load("IMAGENES_VIDEOJUEGO/10.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = position

    def UPDATE(self, event):
        self.current_image = (self.current_image + 1) % 3
        self.image = self.images[self.current_image]
        self.image == self.sheet.subsurface(self.sheet.get_clip())

class Pajaro4_Menu(pygame.sprite.Sprite):
    def __init__(self,position):
        pygame.sprite.Sprite.__init__(self)
        self.sheet = pygame.image.load("IMAGENES_VIDEOJUEGO/14.png").convert_alpha()
        self.images = [pygame.image.load("IMAGENES_VIDEOJUEGO/13.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/14.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/15.png").convert_alpha()]
        self.current_image = 0
        self.image = pygame.image.load("IMAGENES_VIDEOJUEGO/13.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = position

    def UPDATE(self, event):
        self.current_image = (self.current_image + 1) % 3
        self.image = self.images[self.current_image]
        self.image == self.sheet.subsurface(self.sheet.get_clip())

class Pajaro5_Menu(pygame.sprite.Sprite):
    def __init__(self,position):
        pygame.sprite.Sprite.__init__(self)
        self.sheet = pygame.image.load("IMAGENES_VIDEOJUEGO/17.png").convert_alpha()
        self.images = [pygame.image.load("IMAGENES_VIDEOJUEGO/16.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/17.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/18.png").convert_alpha()]
        self.current_image = 0
        self.image = pygame.image.load("IMAGENES_VIDEOJUEGO/16.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = position

    def UPDATE(self, event):
        self.current_image = (self.current_image + 1) % 3
        self.image = self.images[self.current_image]
        self.image == self.sheet.subsurface(self.sheet.get_clip())

class Pajaro6_Menu(pygame.sprite.Sprite):
    def __init__(self,position):
        pygame.sprite.Sprite.__init__(self)
        self.sheet = pygame.image.load("IMAGENES_VIDEOJUEGO/20.png").convert_alpha()
        self.images = [pygame.image.load("IMAGENES_VIDEOJUEGO/19.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/20.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/21.png").convert_alpha()]
        self.current_image = 0
        self.image = pygame.image.load("IMAGENES_VIDEOJUEGO/19.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = position

    def UPDATE(self, event):
        self.current_image = (self.current_image + 1) % 3
        self.image = self.images[self.current_image]
        self.image == self.sheet.subsurface(self.sheet.get_clip())
