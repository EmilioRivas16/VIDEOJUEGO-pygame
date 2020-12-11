import pygame

class Pajaro(pygame.sprite.Sprite):
    def __init__(self,position):
        pygame.sprite.Sprite.__init__(self)
        # Declaración de la imagen del pájaro
        self.sheet = pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ENMEDIO.png").convert_alpha()
        # Se convierte la imagen para ser mostrada
        #self.image = self.sheet.subsurface(self.sheet.get_clip())
        # Se establecen las tres imagenes que haran la animacion
        self.images = [pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ARRIBA.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ENMEDIO.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ABAJO.png").convert_alpha()]

        self.current_image = 0
        self.image = pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ARRIBA.png").convert_alpha()
        # Creación del rectangulo de la imagen
        self.rect = self.image.get_rect()
        self.rect.topleft = position

    def update(self, direccion):


        # Se establece la velocidad a la que sube y cae el pajaro
        if direccion == 'UP':
            self.rect.y -= 10
        if direccion == 'DOWN':
            self.rect.y += 10

        # Aquí se establecen las barreras de arriba y abajo
        if self.rect.y <= 0:
            self.rect.y = 0
        if self.rect.y >= 522:
            self.rect.y = 522

        # Aquí está toda la magia del movimiento de las alas
        self.current_image = (self.current_image + 1) % 3
        self.image = self.images[self.current_image]

        #Esto se necesita para que todo lo que esta en la función update funcione
        self.image == self.sheet.subsurface(self.sheet.get_clip())


    def Movimiento_Pajaro(self, event):

        #Se establece que cuando se aprete la tecla espacio el pajaro suba
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.update('UP')

        #Se establece que cuando se suelte la tecla espacio el pajaro baje
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                self.update('DOWN')








class Pajaro2(pygame.sprite.Sprite):
    def __init__(self,position):
        pygame.sprite.Sprite.__init__(self)
        # Declaración de la imagen del pájaro
        self.sheet = pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ENMEDIO2.png").convert_alpha()
        # Se convierte la imagen para ser mostrada
        #self.image = self.sheet.subsurface(self.sheet.get_clip())
        # Se establecen las tres imagenes que haran la animacion
        self.images = [pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ARRIBA2.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ENMEDIO2.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ABAJO2.png").convert_alpha()]

        self.current_image = 0
        self.image = pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ARRIBA2.png").convert_alpha()
        # Creación del rectangulo de la imagen
        self.rect = self.image.get_rect()
        self.rect.topleft = position

    def update(self, direccion):


        # Se establece la velocidad a la que sube y cae el pajaro
        if direccion == 'UP':
            self.rect.y -= 10
        if direccion == 'DOWN':
            self.rect.y += 10

        # Aquí se establecen las barreras de arriba y abajo
        if self.rect.y <= 0:
            self.rect.y = 0
        if self.rect.y >= 522:
            self.rect.y = 522

        # Aquí está toda la magia del movimiento de las alas
        self.current_image = (self.current_image + 1) % 3
        self.image = self.images[self.current_image]

        #Esto se necesita para que todo lo que esta en la función update funcione
        self.image == self.sheet.subsurface(self.sheet.get_clip())


    def Movimiento_Pajaro(self, event):

        #Se establece que cuando se aprete la tecla espacio el pajaro suba
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.update('UP')

        #Se establece que cuando se suelte la tecla espacio el pajaro baje
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                self.update('DOWN')




class Pajaro3(pygame.sprite.Sprite):
    def __init__(self,position):
        pygame.sprite.Sprite.__init__(self)
        # Declaración de la imagen del pájaro
        self.sheet = pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ENMEDIO3.png").convert_alpha()
        # Se convierte la imagen para ser mostrada
        #self.image = self.sheet.subsurface(self.sheet.get_clip())
        # Se establecen las tres imagenes que haran la animacion
        self.images = [pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ARRIBA3.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ENMEDIO3.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ABAJO3.png").convert_alpha()]

        self.current_image = 0
        self.image = pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ARRIBA3.png").convert_alpha()
        # Creación del rectangulo de la imagen
        self.rect = self.image.get_rect()
        self.rect.topleft = position

    def update(self, direccion):


        # Se establece la velocidad a la que sube y cae el pajaro
        if direccion == 'UP':
            self.rect.y -= 10
        if direccion == 'DOWN':
            self.rect.y += 10

        # Aquí se establecen las barreras de arriba y abajo
        if self.rect.y <= 0:
            self.rect.y = 0
        if self.rect.y >= 522:
            self.rect.y = 522

        # Aquí está toda la magia del movimiento de las alas
        self.current_image = (self.current_image + 1) % 3
        self.image = self.images[self.current_image]

        #Esto se necesita para que todo lo que esta en la función update funcione
        self.image == self.sheet.subsurface(self.sheet.get_clip())


    def Movimiento_Pajaro(self, event):

        #Se establece que cuando se aprete la tecla espacio el pajaro suba
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.update('UP')

        #Se establece que cuando se suelte la tecla espacio el pajaro baje
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                self.update('DOWN')




class Pajaro4(pygame.sprite.Sprite):
    def __init__(self,position):
        pygame.sprite.Sprite.__init__(self)
        # Declaración de la imagen del pájaro
        self.sheet = pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ENMEDIO.png").convert_alpha()
        # Se convierte la imagen para ser mostrada
        #self.image = self.sheet.subsurface(self.sheet.get_clip())
        # Se establecen las tres imagenes que haran la animacion
        self.images = [pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ARRIBA.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ENMEDIO.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ABAJO.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ARRIBA.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ENMEDIO.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ABAJO.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ARRIBA.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ENMEDIO.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ABAJO.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ARRIBA.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ENMEDIO.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ABAJO.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ARRIBA.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ENMEDIO.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ABAJO.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ARRIBA.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ENMEDIO.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ABAJO.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ARRIBA.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ENMEDIO.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ABAJO.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ARRIBA.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ENMEDIO.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ABAJO.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ARRIBA2.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ENMEDIO2.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ABAJO2.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ARRIBA2.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ENMEDIO2.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ABAJO2.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ARRIBA2.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ENMEDIO2.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ABAJO2.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ARRIBA2.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ENMEDIO2.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ABAJO2.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ARRIBA2.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ENMEDIO2.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ABAJO2.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ARRIBA2.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ENMEDIO2.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ABAJO2.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ARRIBA2.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ENMEDIO2.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ABAJO2.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ARRIBA2.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ENMEDIO2.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ABAJO2.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ARRIBA3.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ENMEDIO3.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ABAJO3.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ARRIBA3.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ENMEDIO3.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ABAJO3.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ARRIBA3.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ENMEDIO3.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ABAJO3.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ARRIBA3.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ENMEDIO3.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ABAJO3.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ARRIBA3.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ENMEDIO3.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ABAJO3.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ARRIBA3.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ENMEDIO3.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ABAJO3.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ARRIBA3.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ENMEDIO3.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ABAJO3.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ARRIBA3.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ENMEDIO3.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ABAJO3.png").convert_alpha()]

        self.current_image = 0
        self.image = pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ARRIBA2.png").convert_alpha()
        # Creación del rectangulo de la imagen
        self.rect = self.image.get_rect()
        self.rect.topleft = position

    def update(self, direccion):


        # Se establece la velocidad a la que sube y cae el pajaro
        if direccion == 'UP':
            self.rect.y -= 10
        if direccion == 'DOWN':
            self.rect.y += 10

        # Aquí se establecen las barreras de arriba y abajo
        if self.rect.y <= 0:
            self.rect.y = 0
        if self.rect.y >= 522:
            self.rect.y = 522

        # Aquí está toda la magia del movimiento de las alas
        self.current_image = (self.current_image + 1) % 72
        self.image = self.images[self.current_image]

        #Esto se necesita para que todo lo que esta en la función update funcione
        self.image == self.sheet.subsurface(self.sheet.get_clip())


    def Movimiento_Pajaro(self, event):

        #Se establece que cuando se aprete la tecla espacio el pajaro suba
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.update('UP')

        #Se establece que cuando se suelte la tecla espacio el pajaro baje
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                self.update('DOWN')


class Pajaro5(pygame.sprite.Sprite):
    def __init__(self,position):
        pygame.sprite.Sprite.__init__(self)
        # Declaración de la imagen del pájaro
        self.sheet = pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ENMEDIO.png").convert_alpha()
        # Se convierte la imagen para ser mostrada
        #self.image = self.sheet.subsurface(self.sheet.get_clip())
        # Se establecen las tres imagenes que haran la animacion
        self.images = [pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ARRIBA.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ENMEDIO.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ABAJO.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ARRIBA.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ENMEDIO.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ABAJO.png").convert_alpha(),

                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ARRIBA2.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ENMEDIO2.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ABAJO2.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ARRIBA2.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ENMEDIO2.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ABAJO2.png").convert_alpha(),

                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ARRIBA3.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ENMEDIO3.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ABAJO3.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ARRIBA3.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ENMEDIO3.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ABAJO3.png").convert_alpha(),]

        self.current_image = 0
        self.image = pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ARRIBA2.png").convert_alpha()
        # Creación del rectangulo de la imagen
        self.rect = self.image.get_rect()
        self.rect.topleft = position

    def update(self, direccion):


        # Se establece la velocidad a la que sube y cae el pajaro
        if direccion == 'UP':
            self.rect.y -= 10
        if direccion == 'DOWN':
            self.rect.y += 10

        # Aquí se establecen las barreras de arriba y abajo
        if self.rect.y <= 0:
            self.rect.y = 0
        if self.rect.y >= 522:
            self.rect.y = 522

        # Aquí está toda la magia del movimiento de las alas
        self.current_image = (self.current_image + 1) % 18
        self.image = self.images[self.current_image]

        #Esto se necesita para que todo lo que esta en la función update funcione
        self.image == self.sheet.subsurface(self.sheet.get_clip())


    def Movimiento_Pajaro(self, event):

        #Se establece que cuando se aprete la tecla espacio el pajaro suba
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.update('UP')

        #Se establece que cuando se suelte la tecla espacio el pajaro baje
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                self.update('DOWN')


class Pajaro6(pygame.sprite.Sprite):
    def __init__(self,position):
        pygame.sprite.Sprite.__init__(self)
        # Declaración de la imagen del pájaro
        self.sheet = pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ENMEDIO.png").convert_alpha()
        # Se convierte la imagen para ser mostrada
        #self.image = self.sheet.subsurface(self.sheet.get_clip())
        # Se establecen las tres imagenes que haran la animacion
        self.images = [pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ARRIBA.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ENMEDIO.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ABAJO.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ARRIBA.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ENMEDIO.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ABAJO.png").convert_alpha(),

                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ARRIBA2.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ENMEDIO2.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ABAJO2.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ARRIBA2.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ENMEDIO2.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ABAJO2.png").convert_alpha(),

                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ARRIBA3.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ENMEDIO3.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ABAJO3.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ARRIBA3.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ENMEDIO3.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ABAJO3.png").convert_alpha(),]

        self.current_image = 0
        self.image = pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ARRIBA2.png").convert_alpha()
        # Creación del rectangulo de la imagen
        self.rect = self.image.get_rect()
        self.rect.topleft = position

    def update(self, direccion):

        # Aquí está toda la magia del movimiento de las alas
        self.current_image = (self.current_image + 1) % 18
        self.image = self.images[self.current_image]

        #Esto se necesita para que todo lo que esta en la función update funcione
        self.image == self.sheet.subsurface(self.sheet.get_clip())


    def Movimiento_Pajaro(self, event):

        #Se establece que cuando se aprete la tecla espacio el pajaro suba
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.update('UP')

        #Se establece que cuando se suelte la tecla espacio el pajaro baje
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                self.update('DOWN')


class Pajaro7(pygame.sprite.Sprite):
    def __init__(self,position):
        pygame.sprite.Sprite.__init__(self)
        # Declaración de la imagen del pájaro
        self.sheet = pygame.image.load("IMAGENES_VIDEOJUEGO/G2.png").convert_alpha()
        # Se convierte la imagen para ser mostrada
        #self.image = self.sheet.subsurface(self.sheet.get_clip())
        # Se establecen las tres imagenes que haran la animacion
        self.images = [pygame.image.load("IMAGENES_VIDEOJUEGO/G1.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/G2.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/G3.png").convert_alpha()]

        self.current_image = 0
        self.image = pygame.image.load("IMAGENES_VIDEOJUEGO/G3.png").convert_alpha()
        # Creación del rectangulo de la imagen
        self.rect = self.image.get_rect()
        self.rect.topleft = position

    def update(self, direccion):

        # Aquí está toda la magia del movimiento de las alas
        self.current_image = (self.current_image + 1) % 3
        self.image = self.images[self.current_image]

        #Esto se necesita para que todo lo que esta en la función update funcione
        self.image == self.sheet.subsurface(self.sheet.get_clip())


    def Movimiento_Pajaro(self, event):

        #Se establece que cuando se aprete la tecla espacio el pajaro suba
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.update('UP')

        #Se establece que cuando se suelte la tecla espacio el pajaro baje
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                self.update('DOWN')



class Pajaro8(pygame.sprite.Sprite):
    def __init__(self,position):
        pygame.sprite.Sprite.__init__(self)
        # Declaración de la imagen del pájaro
        self.sheet = pygame.image.load("IMAGENES_VIDEOJUEGO/G5.png").convert_alpha()
        # Se convierte la imagen para ser mostrada
        #self.image = self.sheet.subsurface(self.sheet.get_clip())
        # Se establecen las tres imagenes que haran la animacion
        self.images = [pygame.image.load("IMAGENES_VIDEOJUEGO/G4.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/G5.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/G6.png").convert_alpha()]

        self.current_image = 0
        self.image = pygame.image.load("IMAGENES_VIDEOJUEGO/G6.png").convert_alpha()
        # Creación del rectangulo de la imagen
        self.rect = self.image.get_rect()
        self.rect.topleft = position

    def update(self, direccion):

        # Aquí está toda la magia del movimiento de las alas
        self.current_image = (self.current_image + 1) % 3
        self.image = self.images[self.current_image]

        #Esto se necesita para que todo lo que esta en la función update funcione
        self.image == self.sheet.subsurface(self.sheet.get_clip())


    def Movimiento_Pajaro(self, event):

        #Se establece que cuando se aprete la tecla espacio el pajaro suba
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.update('UP')

        #Se establece que cuando se suelte la tecla espacio el pajaro baje
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                self.update('DOWN')



class Pajaro9(pygame.sprite.Sprite):
    def __init__(self,position):
        pygame.sprite.Sprite.__init__(self)
        # Declaración de la imagen del pájaro
        self.sheet = pygame.image.load("IMAGENES_VIDEOJUEGO/G8.png").convert_alpha()
        # Se convierte la imagen para ser mostrada
        #self.image = self.sheet.subsurface(self.sheet.get_clip())
        # Se establecen las tres imagenes que haran la animacion
        self.images = [pygame.image.load("IMAGENES_VIDEOJUEGO/G7.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/G8.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/G9.png").convert_alpha()]

        self.current_image = 0
        self.image = pygame.image.load("IMAGENES_VIDEOJUEGO/G9.png").convert_alpha()
        # Creación del rectangulo de la imagen
        self.rect = self.image.get_rect()
        self.rect.topleft = position

    def update(self, direccion):

        # Aquí está toda la magia del movimiento de las alas
        self.current_image = (self.current_image + 1) % 3
        self.image = self.images[self.current_image]

        #Esto se necesita para que todo lo que esta en la función update funcione
        self.image == self.sheet.subsurface(self.sheet.get_clip())


    def Movimiento_Pajaro(self, event):

        #Se establece que cuando se aprete la tecla espacio el pajaro suba
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.update('UP')

        #Se establece que cuando se suelte la tecla espacio el pajaro baje
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                self.update('DOWN')





class Pajaro1_fin(pygame.sprite.Sprite):
    def __init__(self,position):
        pygame.sprite.Sprite.__init__(self)
        # Declaración de la imagen del pájaro
        self.sheet = pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ENMEDIO.png").convert_alpha()
        # Se convierte la imagen para ser mostrada
        #self.image = self.sheet.subsurface(self.sheet.get_clip())
        # Se establecen las tres imagenes que haran la animacion
        self.images = [pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ARRIBA.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ENMEDIO.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ABAJO.png").convert_alpha()]

        self.current_image = 0
        self.image = pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ARRIBA.png").convert_alpha()
        # Creación del rectangulo de la imagen
        self.rect = self.image.get_rect()
        self.rect.topleft = position

    def update(self, direccion):



        # Aquí está toda la magia del movimiento de las alas
        self.current_image = (self.current_image + 1) % 3
        self.image = self.images[self.current_image]

        #Esto se necesita para que todo lo que esta en la función update funcione
        self.image == self.sheet.subsurface(self.sheet.get_clip())


    def Movimiento_Pajaro(self, event):

        #Se establece que cuando se aprete la tecla espacio el pajaro suba
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.update('UP')

        #Se establece que cuando se suelte la tecla espacio el pajaro baje
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                self.update('DOWN')








class Pajaro2_fin(pygame.sprite.Sprite):
    def __init__(self,position):
        pygame.sprite.Sprite.__init__(self)
        # Declaración de la imagen del pájaro
        self.sheet = pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ENMEDIO2.png").convert_alpha()
        # Se convierte la imagen para ser mostrada
        #self.image = self.sheet.subsurface(self.sheet.get_clip())
        # Se establecen las tres imagenes que haran la animacion
        self.images = [pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ARRIBA2.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ENMEDIO2.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ABAJO2.png").convert_alpha()]

        self.current_image = 0
        self.image = pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ARRIBA2.png").convert_alpha()
        # Creación del rectangulo de la imagen
        self.rect = self.image.get_rect()
        self.rect.topleft = position

    def update(self, direccion):



        # Aquí está toda la magia del movimiento de las alas
        self.current_image = (self.current_image + 1) % 3
        self.image = self.images[self.current_image]

        #Esto se necesita para que todo lo que esta en la función update funcione
        self.image == self.sheet.subsurface(self.sheet.get_clip())


    def Movimiento_Pajaro(self, event):

        #Se establece que cuando se aprete la tecla espacio el pajaro suba
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.update('UP')

        #Se establece que cuando se suelte la tecla espacio el pajaro baje
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                self.update('DOWN')




class Pajaro3_fin(pygame.sprite.Sprite):
    def __init__(self,position):
        pygame.sprite.Sprite.__init__(self)
        # Declaración de la imagen del pájaro
        self.sheet = pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ENMEDIO3.png").convert_alpha()
        # Se convierte la imagen para ser mostrada
        #self.image = self.sheet.subsurface(self.sheet.get_clip())
        # Se establecen las tres imagenes que haran la animacion
        self.images = [pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ARRIBA3.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ENMEDIO3.png").convert_alpha(),
                       pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ABAJO3.png").convert_alpha()]

        self.current_image = 0
        self.image = pygame.image.load("IMAGENES_VIDEOJUEGO/PAJARO_ALAS_ARRIBA3.png").convert_alpha()
        # Creación del rectangulo de la imagen
        self.rect = self.image.get_rect()
        self.rect.topleft = position

    def update(self, direccion):



        # Aquí está toda la magia del movimiento de las alas
        self.current_image = (self.current_image + 1) % 3
        self.image = self.images[self.current_image]

        #Esto se necesita para que todo lo que esta en la función update funcione
        self.image == self.sheet.subsurface(self.sheet.get_clip())


    def Movimiento_Pajaro(self, event):

        #Se establece que cuando se aprete la tecla espacio el pajaro suba
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.update('UP')

        #Se establece que cuando se suelte la tecla espacio el pajaro baje
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                self.update('DOWN')
