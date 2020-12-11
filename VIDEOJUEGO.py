import pygame
import random
import sys
import TUBOS1
import TUBOS2
import TUBOS3
import JEFE1
import JEFE2
import JEFE3
import BATALLA_FINAL
import MENU
import FLAPPY
import TRANSICIONES
from pygame import mixer
from pygame.locals import *
import time



pygame.init()

# Declaracion de pantalla
pantalla_x = 1280
pantalla_y = 568
clock = pygame.time.Clock()
screen = pygame.display.set_mode((pantalla_x, pantalla_y))

# Caption de la ventana
icon = pygame.image.load("imagenes_videojuego/PAJARO_LOGO.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("Flappy-Space-Bros")

# Fondos
bg_menu = pygame.image.load("IMAGENES_VIDEOJUEGO/FONDO_MENU.png").convert()
bg_1 = pygame.image.load("IMAGENES_VIDEOJUEGO/FONDO1.png").convert()
bg_2 = pygame.image.load("IMAGENES_VIDEOJUEGO/FONDO2.png").convert()
bg_3 = pygame.image.load("IMAGENES_VIDEOJUEGO/FONDO3.png").convert()
bg_4 = pygame.image.load("IMAGENES_VIDEOJUEGO/FONDO5.png").convert()
bg_espacial = pygame.image.load("IMAGENES_VIDEOJUEGO/FONDO_ESPACIAL2.png").convert()
bg_espacial2 = pygame.image.load("IMAGENES_VIDEOJUEGO/FONDO_ESPACIAL3.png").convert()
bg_espacial3 = pygame.image.load("IMAGENES_VIDEOJUEGO/FONDO_ESPACIAL5.png").convert()
bg_transicion = pygame.image.load("IMAGENES_VIDEOJUEGO/FONDO_ESPACIO_MENU_JUEGO.png").convert()

bg_5 = pygame.image.load("IMAGENES_VIDEOJUEGO/FONDO4.png").convert()
bg_batallafinal = pygame.image.load("IMAGENES_VIDEOJUEGO/AGUJERO_NEGRO2.jpg").convert()
bg_espacial6 = pygame.image.load("IMAGENES_VIDEOJUEGO/FONDO_ESPACIAL6.png").convert()
corneta_izq = pygame.image.load("IMAGENES_VIDEOJUEGO/corneta1.png").convert_alpha()
corneta_der = pygame.image.load("IMAGENES_VIDEOJUEGO/corneta2.png").convert_alpha()
victory = pygame.image.load("IMAGENES_VIDEOJUEGO/victory.png").convert_alpha()
royale = pygame.image.load("IMAGENES_VIDEOJUEGO/royale.png").convert_alpha()
theend = pygame.image.load("IMAGENES_VIDEOJUEGO/theend.png").convert_alpha()

Flappy1_fin = FLAPPY.Pajaro1_fin((-60, 75))
Flappy2_fin = FLAPPY.Pajaro2_fin((-60, 275))
Flappy3_fin = FLAPPY.Pajaro3_fin((-60, 475))

Flappy5 = FLAPPY.Pajaro5((140, pantalla_y//2 - 50))
Flappy6 = FLAPPY.Pajaro5((140, pantalla_y//2 - 50))
Flappy13 = FLAPPY.Pajaro5((140, pantalla_y//2 - 50))

Flappy7 = FLAPPY.Pajaro7((100, pantalla_y//2 - 60))
Flappy8 = FLAPPY.Pajaro8((100, pantalla_y//2 - 250))
Flappy9 = FLAPPY.Pajaro9((100, pantalla_y//2 + 120))

Flappy10 = FLAPPY.Pajaro7((100, pantalla_y//2 - 60))
Flappy11 = FLAPPY.Pajaro8((100, pantalla_y//2 - 250))
Flappy12 = FLAPPY.Pajaro9((100, pantalla_y//2 + 120))

BOSS1_BF = BATALLA_FINAL.Boss1((1278,50))
BOSS2_BF = BATALLA_FINAL.Boss2((1280,440))
BOSS3_BF = BATALLA_FINAL.Boss3((1275,210))
BOSS3_FINAL = BATALLA_FINAL.Boss3((1110,210))

BOSS3_VOLTEADO = BATALLA_FINAL.Boss3_VOLTEADO((1115,210))

BOSS1_MUERTO = BATALLA_FINAL.Boss1_MUERTO((1170,50))
BOSS2_MUERTO = BATALLA_FINAL.Boss2_MUERTO((1170,440))
BOSS3_MUERTO = BATALLA_FINAL.Boss3_MUERTO((1140,210))


ASTEROIDE = BATALLA_FINAL.ASTEROIDE((180,520))
HONGO = BATALLA_FINAL.HONGO((1110,50))
NUBE = pygame.image.load("IMAGENES_VIDEOJUEGO/NUBE.png").convert_alpha()

PROYECTIL1_1 = BATALLA_FINAL.PROYECTIL_MARIO((1234,10))
PROYECTIL2_1 = BATALLA_FINAL.PROYECTIL_ROCA((1275,440))
PROYECTIL3_1 = BATALLA_FINAL.PROYECTIL_BOWSER((1278,224))
PROYECTIL1_2 = BATALLA_FINAL.PROYECTIL_MARIO((1234,10))
PROYECTIL2_2 = BATALLA_FINAL.PROYECTIL_ROCA((1275,440))
PROYECTIL3_2 = BATALLA_FINAL.PROYECTIL_BOWSER((1278,224))
PROYECTIL1_3 = BATALLA_FINAL.PROYECTIL_MARIO((1234,10))
PROYECTIL2_3 = BATALLA_FINAL.PROYECTIL_ROCA((1275,440))
PROYECTIL3_3 = BATALLA_FINAL.PROYECTIL_BOWSER((1278,224))

PROYECTIL1_4 = BATALLA_FINAL.PROYECTIL_MARIO((1050,10))
PROYECTIL2_4 = BATALLA_FINAL.PROYECTIL_ROCA((1080,440))
PROYECTIL3_4 = BATALLA_FINAL.PROYECTIL_BOWSER((1050,224))
PROYECTIL1_5 = BATALLA_FINAL.PROYECTIL_MARIO((1050,10))
PROYECTIL2_5 = BATALLA_FINAL.PROYECTIL_ROCA((1080,440))
PROYECTIL3_5 = BATALLA_FINAL.PROYECTIL_BOWSER((1050,224))

PROYECTIL2_6 = BATALLA_FINAL.PROYECTIL_ROCA((1080,440))
PROYECTIL3_6 = BATALLA_FINAL.PROYECTIL_BOWSER((1050,224))

PROYECTIL1_6 = BATALLA_FINAL.PROYECTIL_MARIO((1050,10))
PROYECTIL3_7 = BATALLA_FINAL.PROYECTIL_BOWSER((1050,224))

PROYECTIL1_7 = BATALLA_FINAL.PROYECTIL_MARIO((1050,10))
PROYECTIL2_7 = BATALLA_FINAL.PROYECTIL_ROCA((1080,440))

PROYECTIL3_8 = BATALLA_FINAL.PROYECTIL_BOWSER((1050,224))

PROYECTIL1_8 = BATALLA_FINAL.PROYECTIL_MARIO((1050,10))
PROYECTIL2_8 = BATALLA_FINAL.PROYECTIL_ROCA((1080,440))
PROYECTIL3_9 = BATALLA_FINAL.PROYECTIL_BOWSER((1050,224))
PROYECTIL1_9 = BATALLA_FINAL.PROYECTIL_MARIO((1050,10))
PROYECTIL2_9 = BATALLA_FINAL.PROYECTIL_ROCA((1080,440))

PROYECTIL3_10 = BATALLA_FINAL.PROYECTIL_BOWSER((1050,224))
PROYECTIL3_11 = BATALLA_FINAL.PROYECTIL_BOWSER((1050,224))
PROYECTIL3_12 = BATALLA_FINAL.PROYECTIL_BOWSER((1050,224))

PROYECTIL1_8_v = BATALLA_FINAL.PROYECTIL_MARIO_VOLTEADO((200,10))
PROYECTIL1_9_v = BATALLA_FINAL.PROYECTIL_MARIO_VOLTEADO((200,10))

BUM1 = BATALLA_FINAL.BUM((0,0))
BUM2 = BATALLA_FINAL.BUM((0,0))
BUM3 = BATALLA_FINAL.BUM((0,0))

RELOJ_BATALLAFINAL = BATALLA_FINAL.RELOJ_BATALLAFINAL((0,0))
BATALLAFINAL = True

# Elementos pantalla menu
NOMBRE = pygame.image.load("IMAGENES_VIDEOJUEGO/NOMBRE(LOGO).png").convert_alpha()
TUBO_DERECHA = pygame.image.load("IMAGENES_VIDEOJUEGO/Tubo_Rojo_Punta_Derecha.png").convert_alpha()
TUBO_IZQUIERDA = pygame.image.load("IMAGENES_VIDEOJUEGO/Tubo_Rojo_Punta_Izquierda.png").convert_alpha()
TUBO_CENTRO = pygame.image.load("IMAGENES_VIDEOJUEGO/Tubo_Rojo_Centro.png").convert_alpha()
TUBO_ARRIBA1 = pygame.image.load("IMAGENES_VIDEOJUEGO/Tubo_Arriba1.png").convert_alpha()
TUBO_ARRIBA2 = pygame.image.load("IMAGENES_VIDEOJUEGO/Tubo_Arriba2.png").convert_alpha()
TUBO_ABAJO1 = pygame.image.load("IMAGENES_VIDEOJUEGO/Tubo_Abajo1.png").convert_alpha()
TUBO_ABAJO2 = pygame.image.load("IMAGENES_VIDEOJUEGO/Tubo_Abajo2.png").convert_alpha()
PSTS = pygame.image.load("IMAGENES_VIDEOJUEGO/Press_Space_To_Start.png").convert_alpha()
FONDO_VIDAS1p = pygame.image.load("IMAGENES_VIDEOJUEGO/fondo_vidas.png").convert_alpha()
FONDO_VIDAS1g = pygame.image.load("IMAGENES_VIDEOJUEGO/fondo_vidas2.png").convert_alpha()
FONDO_VIDAS2p = pygame.image.load("IMAGENES_VIDEOJUEGO/fondo_vidas3.png").convert_alpha()
FONDO_VIDAS2g = pygame.image.load("IMAGENES_VIDEOJUEGO/fondo_vidas4.png").convert_alpha()
FONDO_VIDAS3p = pygame.image.load("IMAGENES_VIDEOJUEGO/fondo_vidas5.png").convert_alpha()
FONDO_VIDAS3g = pygame.image.load("IMAGENES_VIDEOJUEGO/fondo_vidas6.png").convert_alpha()
FONDO_VIDAS4p = pygame.image.load("IMAGENES_VIDEOJUEGO/fondo_vidas7.png").convert_alpha()
FONDO_VIDAS4g = pygame.image.load("IMAGENES_VIDEOJUEGO/fondo_vidas8.png").convert_alpha()

planetamenu1 = MENU.Planeta1((0, 0))
planetamenu2 = MENU.Planeta2((0, 490))
planetamenu3 = MENU.Planeta3((1200, 490))
planetamenu4 = MENU.Planeta4((1200, 0))
planetamenu5 = MENU.Planeta5((0, 262))
planetamenu6 = MENU.Planeta6((609.5, 490))
planetamenu7 = MENU.Planeta7((1200, 262))
planetamenu8 = MENU.Planeta8((609.5, 0))

PAJARO1 = MENU.Pajaro1_Menu((280, 310))
PAJARO3 = MENU.Pajaro3_Menu((210, 390))
PAJARO5 = MENU.Pajaro5_Menu((340, 390))
PAJARO2 = MENU.Pajaro2_Menu((920, 310))
PAJARO4 = MENU.Pajaro4_Menu((990, 390))
PAJARO6 = MENU.Pajaro6_Menu((860, 390))


RELOJ = JEFE1.RELOJ((1280,234))
RELOJ_2 = JEFE1.RELOJ((1280,234))
RELOJ_3 = JEFE1.RELOJ((1280,234))
RELOJ2 = JEFE1.RELOJ2((0,0))
RELOJ2_2 = JEFE1.RELOJ2((0,0))
RELOJ2_3 = JEFE1.RELOJ2((0,0))
RELOJ3 = JEFE1.RELOJ2((0,0))
RELOJ4 = JEFE1.RELOJ2((0,0))
RELOJ5 = JEFE1.RELOJ2((0,0))

# Bolas de fuego boss 1
bola_fuego1 = JEFE1.BOLA_FUEGO1((1130,60))
ver_bola_fuego1 = False
mover_bola_fuego1 = False
BUM = JEFE1.BUM((155,80))
PRIMERA_FB = True

bola_fuego2 = JEFE1.BOLA_FUEGO2((1130,170))
ver_bola_fuego2 = False
mover_bola_fuego2 = False
BUM2 = JEFE1.BUM2((155,190))
SEGUNDA_FB = False
MUSICA_FB_2 = True

bola_fuego3 = JEFE1.BOLA_FUEGO3((1130,280))
ver_bola_fuego3 = False
mover_bola_fuego3 = False
BUM3 = JEFE1.BUM3((155,300))
TERCERA_FB = False
MUSICA_FB_3 = True

bola_fuego4 = JEFE1.BOLA_FUEGO4((1130,390))
ver_bola_fuego4 = False
mover_bola_fuego4 = False
BUM4 = JEFE1.BUM4((155,410))
CUARTA_FB = False
MUSICA_FB_4 = True

bola_fuego5 = JEFE1.BOLA_FUEGO5((1130,280))
ver_bola_fuego5 = False
mover_bola_fuego5 = False
BUM5 = JEFE1.BUM5((155,300))
QUINTA_FB = False
MUSICA_FB_5 = True

bola_fuego6 = JEFE1.BOLA_FUEGO6((1130,170))
ver_bola_fuego6 = False
mover_bola_fuego6 = False
BUM6 = JEFE1.BUM6((155,190))
SEXTA_FB = False
MUSICA_FB_6 = True

bola_fuego7 = JEFE1.BOLA_FUEGO7((1130,60))
ver_bola_fuego7 = False
mover_bola_fuego7 = False
BUM7 = JEFE1.BUM7((155,80))
SEPTIMA_FB = False
MUSICA_FB_7 = True

bola_fuego8 = JEFE1.BOLA_FUEGO8((1130,170))
ver_bola_fuego8 = False
mover_bola_fuego8 = False
BUM8 = JEFE1.BUM8((155,190))
OCTAVA_FB = False
MUSICA_FB_8 = True

bola_fuego9 = JEFE1.BOLA_FUEGO9((1130,280))
ver_bola_fuego9 = False
mover_bola_fuego9 = False
BUM9 = JEFE1.BUM9((155,300))
NOVENA_FB = False
MUSICA_FB_9 = True

bola_fuego10 = JEFE1.BOLA_FUEGO10((1130,390))
ver_bola_fuego10 = False
mover_bola_fuego10 = False
BUM10 = JEFE1.BUM9((155,410))
DECIMA_FB = False
MUSICA_FB_10 = True

bola_fuego11 = JEFE1.BOLA_FUEGO11((1130,280))
ver_bola_fuego11 = False
mover_bola_fuego11 = False
BUM11 = JEFE1.BUM8((155,300))
ONCEAVA_FB = False
MUSICA_FB_11 = True

bola_fuego12 = JEFE1.BOLA_FUEGO12((1130,170))
ver_bola_fuego12 = False
mover_bola_fuego12 = False
BUM12 = JEFE1.BUM12((155,190))
DOCEAVA_FB = False
MUSICA_FB_12 = True

bola_fuego13 = JEFE1.BOLA_FUEGO13((1130,60))
ver_bola_fuego13 = False
mover_bola_fuego13 = False
BUM13 = JEFE1.BUM13((155,80))
TRECEAVA_FB = False
MUSICA_FB_13 = True

bola_fuego14 = JEFE1.BOLA_FUEGO14((1070,205))
ver_bola_fuego14 = False
mover_bola_fuego14 = False
BUM14 = JEFE1.BUM14((155,260))
MUSICA_FB_14 = True

bola_fuego15 = JEFE1.BOLA_FUEGO15((1070,50))
ver_bola_fuego15 = False
mover_bola_fuego15 = False
BUM15 = JEFE1.BUM15((155,105))
MUSICA_FB_15 = True

bola_fuego16 = JEFE1.BOLA_FUEGO16((1070,360))
ver_bola_fuego16 = False
mover_bola_fuego16 = False
BUM16 = JEFE1.BUM16((155,415))
MUSICA_FB_16 = True

bola_fuego17 = JEFE1.BOLA_FUEGO17((1070,205))
ver_bola_fuego17 = False
mover_bola_fuego17 = False
BUM17 = JEFE1.BUM17((155,260))
MUSICA_FB_17 = True

bola_fuego18 = JEFE1.BOLA_FUEGO18((1070,50))
ver_bola_fuego18 = False
mover_bola_fuego18 = False
BUM18 = JEFE1.BUM18((155,105))
MUSICA_FB_18 = True

bola_fuego19 = JEFE1.BOLA_FUEGO19((1070,360))
ver_bola_fuego19 = False
mover_bola_fuego19 = False
BUM19 = JEFE1.BUM19((155,415))
MUSICA_FB_19 = True

FB_GRANDE1 = True
FB_GRANDE2 = False
FB_GRANDE3 = False
FB_GRANDE4 = False
FB_GRANDE5 = False
FB_GRANDE6 = False

ACT_MOV_FB = True
ACT_MOV_BOSS = True
MOV_BOSS = True
DESACTIVAR = True
MOV_ABAJO = True
DESACTIVAR2 = True
DESACTIVAR3 = True
JEFE1_TOTAL = False
FBS = False


# Bolas de fuego boss 2

bola_fuego1_2 = JEFE2.BOLA_FUEGO1_2((1120,60))
ver_bola_fuego1_2 = False
mover_bola_fuego1_2 = False
BUM1_2 = JEFE2.BUM((155,80))
PRIMERA_FB2 = True

bola_fuego2_2 = JEFE2.BOLA_FUEGO2_2((1120,170))
ver_bola_fuego2_2 = False
mover_bola_fuego2_2 = False
BUM2_2 = JEFE2.BUM((155,190))
SEGUNDA_FB2 = False
MUSICA_FB_2_2 = True

bola_fuego3_2 = JEFE2.BOLA_FUEGO3_2((1120,280))
ver_bola_fuego3_2 = False
mover_bola_fuego3_2 = False
BUM3_2 = JEFE2.BUM((155,300))
TERCERA_FB2 = False
MUSICA_FB_3_2 = True

bola_fuego4_2 = JEFE2.BOLA_FUEGO4_2((1120,390))
ver_bola_fuego4_2 = False
mover_bola_fuego4_2 = False
BUM4_2 = JEFE2.BUM((155,410))
CUARTA_FB2 = False
MUSICA_FB_4_2 = True

bola_fuego5_2 = JEFE2.BOLA_FUEGO5_2((1120,280))
ver_bola_fuego5_2 = False
mover_bola_fuego5_2 = False
BUM5_2 = JEFE2.BUM((155,300))
QUINTA_FB2 = False
MUSICA_FB_5_2 = True

bola_fuego6_2 = JEFE2.BOLA_FUEGO6_2((1120,170))
ver_bola_fuego6_2 = False
mover_bola_fuego6_2 = False
BUM6_2 = JEFE2.BUM((155,190))
SEXTA_FB2 = False
MUSICA_FB_6_2 = True

bola_fuego7_2 = JEFE2.BOLA_FUEGO7_2((1120,60))
ver_bola_fuego7_2 = False
mover_bola_fuego7_2 = False
BUM7_2 = JEFE2.BUM((155,80))
SEPTIMA_FB2 = False
MUSICA_FB_7_2 = True

bola_fuego8_2 = JEFE2.BOLA_FUEGO8_2((1120,170))
ver_bola_fuego8_2 = False
mover_bola_fuego8_2 = False
BUM8_2 = JEFE2.BUM((155,190))
OCTAVA_FB2 = False
MUSICA_FB_8_2 = True

bola_fuego9_2 = JEFE2.BOLA_FUEGO9_2((1120,280))
ver_bola_fuego9_2 = False
mover_bola_fuego9_2 = False
BUM9_2 = JEFE2.BUM((155,300))
NOVENA_FB2 = False
MUSICA_FB_9_2 = True

bola_fuego10_2 = JEFE2.BOLA_FUEGO10_2((1120,390))
ver_bola_fuego10_2 = False
mover_bola_fuego10_2 = False
BUM10_2 = JEFE2.BUM((155,410))
DECIMA_FB2 = False
MUSICA_FB_10_2 = True

bola_fuego11_2 = JEFE2.BOLA_FUEGO11_2((1120,280))
ver_bola_fuego11_2 = False
mover_bola_fuego11_2 = False
BUM11_2 = JEFE2.BUM((155,300))
ONCEAVA_FB2 = False
MUSICA_FB_11_2 = True

bola_fuego12_2 = JEFE2.BOLA_FUEGO12_2((1120,170))
ver_bola_fuego12_2 = False
mover_bola_fuego12_2 = False
BUM12_2 = JEFE2.BUM((155,190))
DOCEAVA_FB2 = False
MUSICA_FB_12_2 = True

bola_fuego13_2 = JEFE2.BOLA_FUEGO13_2((1120,60))
ver_bola_fuego13_2 = False
mover_bola_fuego13_2 = False
BUM13_2 = JEFE2.BUM((155,80))
TRECEAVA_FB2 = False
MUSICA_FB_13_2 = True

bola_fuego14_2 = JEFE2.BOLA_FUEGO14_2((1070,205))
ver_bola_fuego14_2 = False
mover_bola_fuego14_2 = False
BUM14_2 = JEFE2.BUM((155,260))
MUSICA_FB_14_2 = True

bola_fuego15_2 = JEFE2.BOLA_FUEGO15_2((1070,50))
ver_bola_fuego15_2 = False
mover_bola_fuego15_2 = False
BUM15_2 = JEFE2.BUM((155,105))
MUSICA_FB_15_2 = True

bola_fuego16_2 = JEFE2.BOLA_FUEGO16_2((1070,360))
ver_bola_fuego16_2 = False
mover_bola_fuego16_2 = False
BUM16_2 = JEFE2.BUM((155,415))
MUSICA_FB_16_2 = True

bola_fuego17_2 = JEFE2.BOLA_FUEGO17_2((1070,205))
ver_bola_fuego17_2 = False
mover_bola_fuego17_2 = False
BUM17_2 = JEFE2.BUM((155,260))
MUSICA_FB_17_2 = True

bola_fuego18_2 = JEFE2.BOLA_FUEGO18_2((1070,50))
ver_bola_fuego18_2 = False
mover_bola_fuego18_2 = False
BUM18_2 = JEFE2.BUM((155,105))
MUSICA_FB_18_2 = True

bola_fuego19_2 = JEFE2.BOLA_FUEGO19_2((1070,360))
ver_bola_fuego19_2 = False
mover_bola_fuego19_2 = False
BUM19_2 = JEFE2.BUM((155,415))
MUSICA_FB_19_2 = True

FB_GRANDE1_2 = True
FB_GRANDE2_2 = False
FB_GRANDE3_2 = False
FB_GRANDE4_2 = False
FB_GRANDE5_2 = False
FB_GRANDE6_2 = False

ACT_MOV_FB_2 = True
ACT_MOV_BOSS_2 = True
MOV_BOSS_2 = True
DESACTIVAR_2 = True
MOV_ABAJO_2 = True
DESACTIVAR2_2 = True
DESACTIVAR3_2 = True
JEFE2_TOTAL = False
FBS2 = False



bola_fuego1_3 = JEFE3.BOLA_FUEGO1_3((1040,60))
ver_bola_fuego1_3 = False
mover_bola_fuego1_3 = False
BUM1_3 = JEFE3.BUM((155,80))
PRIMERA_FB3 = True

bola_fuego2_3 = JEFE3.BOLA_FUEGO2_3((1040,170))
ver_bola_fuego2_3 = False
mover_bola_fuego2_3 = False
BUM2_3 = JEFE3.BUM((155,190))
SEGUNDA_FB3 = False
MUSICA_FB_2_3 = True

bola_fuego3_3 = JEFE3.BOLA_FUEGO3_3((1040,280))
ver_bola_fuego3_3 = False
mover_bola_fuego3_3 = False
BUM3_3 = JEFE3.BUM((155,300))
TERCERA_FB3 = False
MUSICA_FB_3_3 = True

bola_fuego4_3 = JEFE3.BOLA_FUEGO4_3((1040,390))
ver_bola_fuego4_3 = False
mover_bola_fuego4_3 = False
BUM4_3 = JEFE3.BUM((155,410))
CUARTA_FB3 = False
MUSICA_FB_4_3 = True

bola_fuego5_3 = JEFE3.BOLA_FUEGO5_3((1040,230))
ver_bola_fuego5_3 = False
mover_bola_fuego5_3 = False
BUM5_3 = JEFE3.BUM((155,300))
QUINTA_FB3 = False
MUSICA_FB_5_3 = True

bola_fuego6_3 = JEFE3.BOLA_FUEGO6_3((1040,120))
ver_bola_fuego6_3 = False
mover_bola_fuego6_3 = False
BUM6_3 = JEFE3.BUM((155,190))
SEXTA_FB3 = False
MUSICA_FB_6_3 = True

bola_fuego7_3 = JEFE3.BOLA_FUEGO7_3((1040,60))
ver_bola_fuego7_3 = False
mover_bola_fuego7_3 = False
BUM7_3 = JEFE3.BUM((155,80))
SEPTIMA_FB3 = False
MUSICA_FB_7_3 = True

bola_fuego8_3 = JEFE3.BOLA_FUEGO8_3((1040,220))
ver_bola_fuego8_3 = False
mover_bola_fuego8_3 = False
BUM8_3 = JEFE3.BUM((155,190))
OCTAVA_FB3 = False
MUSICA_FB_8_3 = True

bola_fuego9_3 = JEFE3.BOLA_FUEGO9_3((1040,330))
ver_bola_fuego9_3 = False
mover_bola_fuego9_3 = False
BUM9_3 = JEFE3.BUM((155,300))
NOVENA_FB3 = False
MUSICA_FB_9_3 = True

bola_fuego10_3 = JEFE3.BOLA_FUEGO10_3((1040,390))
ver_bola_fuego10_3 = False
mover_bola_fuego10_3 = False
BUM10_3 = JEFE3.BUM((155,410))
DECIMA_FB3 = False
MUSICA_FB_10_3 = True

bola_fuego11_3 = JEFE3.BOLA_FUEGO11_3((1040,130))
ver_bola_fuego11_3 = False
mover_bola_fuego11_3 = False
BUM11_3 = JEFE3.BUM((155,300))
ONCEAVA_FB3 = False
MUSICA_FB_11_3 = True

bola_fuego12_3 = JEFE3.BOLA_FUEGO12_3((1040,50))
ver_bola_fuego12_3 = False
mover_bola_fuego12_3 = False
BUM12_3 = JEFE3.BUM((155,190))
DOCEAVA_FB3 = False
MUSICA_FB_12_3 = True

bola_fuego13_3 = JEFE3.BOLA_FUEGO13_3((1040,160))
ver_bola_fuego13_3 = False
mover_bola_fuego13_3 = False
BUM13_3 = JEFE3.BUM((155,80))
TRECEAVA_FB3 = False
MUSICA_FB_13_3 = True

bola_fuego14_3 = JEFE3.BOLA_FUEGO14_3((1010,205))
ver_bola_fuego14_3 = False
mover_bola_fuego14_3 = False
BUM14_3 = JEFE3.BUM((155,260))
MUSICA_FB_14_3 = True

bola_fuego15_3 = JEFE3.BOLA_FUEGO15_3((1010,50))
ver_bola_fuego15_3 = False
mover_bola_fuego15_3 = False
BUM15_3 = JEFE3.BUM((155,105))
MUSICA_FB_15_3 = True

bola_fuego16_3 = JEFE3.BOLA_FUEGO16_3((1010,360))
ver_bola_fuego16_3 = False
mover_bola_fuego16_3 = False
BUM16_3 = JEFE3.BUM((155,415))
MUSICA_FB_16_3 = True

bola_fuego17_3 = JEFE3.BOLA_FUEGO17_3((1010,205))
ver_bola_fuego17_3 = False
mover_bola_fuego17_3 = False
BUM17_3 = JEFE3.BUM((155,260))
MUSICA_FB_17_3 = True

bola_fuego18_3 = JEFE3.BOLA_FUEGO18_3((1010,50))
ver_bola_fuego18_3 = False
mover_bola_fuego18_3 = False
BUM18_3 = JEFE3.BUM((155,105))
MUSICA_FB_18_3 = True

bola_fuego19_3 = JEFE3.BOLA_FUEGO19_3((1010,360))
ver_bola_fuego19_3 = False
mover_bola_fuego19_3 = False
BUM19_3 = JEFE3.BUM((155,415))
MUSICA_FB_19_3 = True



FB_GRANDE1_3 = True
FB_GRANDE2_3 = False
FB_GRANDE3_3 = False
FB_GRANDE4_3 = False
FB_GRANDE5_3 = False
FB_GRANDE6_3 = False

ACT_MOV_FB_3 = True
ACT_MOV_BOSS_3 = True
MOV_BOSS_3 = True
DESACTIVAR_3 = True
MOV_ABAJO_3 = True
DESACTIVAR2_3 = True
DESACTIVAR3_3 = True
JEFE3_TOTAL = False
FBS3 = False






# RELOJ TRANSICIONES
RELOJ_TRAN_TUBOS_BOSS_NVL1 = TRANSICIONES.RELOJ_TRAN_TUBOS_BOSS_NVL1((0,0))
RELOJ_TRAN_TUBOS_BOSS_NVL2 = TRANSICIONES.RELOJ_TRAN_TUBOS_BOSS_NVL2((0,0))
RELOJ_TRAN_TUBOS_BOSS_NVL3 = TRANSICIONES.RELOJ_TRAN_TUBOS_BOSS_NVL3((0,0))
RELOJ_TRAN_MENU_TUBOS1 = TRANSICIONES.RELOJ_TRAN_MENU_TUBOS((0,0))

# Pajaro de juego
Flappy = FLAPPY.Pajaro((140, pantalla_y//2 - 50))
Flappy2 = FLAPPY.Pajaro2((140, pantalla_y//2 - 50))
Flappy3 = FLAPPY.Pajaro3((140, pantalla_y//2 - 50))
Flappy4 = FLAPPY.Pajaro4((140, pantalla_y//2 - 50))


#Tubos
tubo_abajo1 = TUBOS1.Tubos_Abajo((1400,360))
tubo_abajo2 = TUBOS1.Tubos_Abajo((2000,410))
tubo_abajo3 = TUBOS1.Tubos_Abajo((2600,310))
tubo_abajo4 = TUBOS1.Tubos_Abajo((3200,410))
tubo_abajo5 = TUBOS1.Tubos_Abajo((3800,360))
tubo_abajo6 = TUBOS1.Tubos_Abajo((4400,410))
tubo_abajo7 = TUBOS1.Tubos_Abajo((5000,310))
tubo_abajo8 = TUBOS1.Tubos_Abajo((5600,410))
tubo_abajo9 = TUBOS1.Tubos_Abajo((6200,310))
tubo_abajo10 = TUBOS1.Tubos_Abajo((6800,360))

tubo_arriba1 = TUBOS1.Tubos_Arriba((1400,-230))
tubo_arriba2 = TUBOS1.Tubos_Arriba((2000,-180))
tubo_arriba3 = TUBOS1.Tubos_Arriba((2600,-280))
tubo_arriba4 = TUBOS1.Tubos_Arriba((3200,-180))
tubo_arriba5 = TUBOS1.Tubos_Arriba((3800,-230))
tubo_arriba6 = TUBOS1.Tubos_Arriba((4400,-180))
tubo_arriba7 = TUBOS1.Tubos_Arriba((5000,-280))
tubo_arriba8 = TUBOS1.Tubos_Arriba((5600,-180))
tubo_arriba9 = TUBOS1.Tubos_Arriba((6200,-280))
tubo_arriba10 = TUBOS1.Tubos_Arriba((6800,-230))

tubo_abajo11 = TUBOS2.Tubos_Abajo((1400,360))
tubo_abajo12 = TUBOS2.Tubos_Abajo((2000,410))
tubo_abajo13 = TUBOS2.Tubos_Abajo((2600,310))
tubo_abajo14 = TUBOS2.Tubos_Abajo((3200,410))
tubo_abajo15 = TUBOS2.Tubos_Abajo((3800,360))
tubo_abajo16 = TUBOS2.Tubos_Abajo((4400,410))
tubo_abajo17 = TUBOS2.Tubos_Abajo((5000,310))
tubo_abajo18 = TUBOS2.Tubos_Abajo((5600,410))
tubo_abajo19 = TUBOS2.Tubos_Abajo((6200,310))
tubo_abajo20 = TUBOS2.Tubos_Abajo((6800,360))

tubo_arriba11 = TUBOS2.Tubos_Arriba((1400,-230))
tubo_arriba12 = TUBOS2.Tubos_Arriba((2000,-180))
tubo_arriba13 = TUBOS2.Tubos_Arriba((2600,-280))
tubo_arriba14 = TUBOS2.Tubos_Arriba((3200,-180))
tubo_arriba15 = TUBOS2.Tubos_Arriba((3800,-230))
tubo_arriba16 = TUBOS2.Tubos_Arriba((4400,-180))
tubo_arriba17 = TUBOS2.Tubos_Arriba((5000,-280))
tubo_arriba18 = TUBOS2.Tubos_Arriba((5600,-180))
tubo_arriba19 = TUBOS2.Tubos_Arriba((6200,-280))
tubo_arriba20 = TUBOS2.Tubos_Arriba((6800,-230))

tubo_abajo21 = TUBOS3.Tubos_Abajo((1400,360))
tubo_abajo22 = TUBOS3.Tubos_Abajo((2000,410))
tubo_abajo23 = TUBOS3.Tubos_Abajo((2600,310))
tubo_abajo24 = TUBOS3.Tubos_Abajo((3200,410))
tubo_abajo25 = TUBOS3.Tubos_Abajo((3800,360))
tubo_abajo26 = TUBOS3.Tubos_Abajo((4400,410))
tubo_abajo27 = TUBOS3.Tubos_Abajo((5000,310))
tubo_abajo28 = TUBOS3.Tubos_Abajo((5600,410))
tubo_abajo29 = TUBOS3.Tubos_Abajo((6200,310))
tubo_abajo30 = TUBOS3.Tubos_Abajo((6800,360))

tubo_arriba21 = TUBOS3.Tubos_Arriba((1400,-230))
tubo_arriba22 = TUBOS3.Tubos_Arriba((2000,-180))
tubo_arriba23 = TUBOS3.Tubos_Arriba((2600,-280))
tubo_arriba24 = TUBOS3.Tubos_Arriba((3200,-180))
tubo_arriba25 = TUBOS3.Tubos_Arriba((3800,-230))
tubo_arriba26 = TUBOS3.Tubos_Arriba((4400,-180))
tubo_arriba27 = TUBOS3.Tubos_Arriba((5000,-280))
tubo_arriba28 = TUBOS3.Tubos_Arriba((5600,-180))
tubo_arriba29 = TUBOS3.Tubos_Arriba((6200,-280))
tubo_arriba30 = TUBOS3.Tubos_Arriba((6800,-230))

ver1 = True
ver2 = True
ver3 = True
ver4 = True
ver5 = True
ver6 = True
ver7 = True
ver8 = True
ver9 = True
ver10 = True
ver11 = True
ver12 = True
ver13 = True
ver14 = True
ver15 = True
ver16 = True
ver17 = True
ver18 = True
ver19 = True
ver20 = True
ver21 = True
ver22 = True
ver23 = True
ver24 = True
ver25 = True
ver26 = True
ver27 = True
ver28 = True
ver29 = True
ver30 = True
ver31 = True
ver_paj = True
ver_paj2 = True
ver_nubes = True
ver_nubes2 = True
act_ir_izq1 = False
act_ir_izq2 = False
act_ir_izq3 = False
act_ir_izq4 = False
act_ir_izq5 = False
ver_boss1 = True
ver_boss2 = True
ver_boss3 = True
ver_boss1_muerto = False
ver_boss2_muerto = False
mov_der_bow_fb1 = False
mov_der_bow_fb2 = False
mov_der_bow_fb3 = False
mov_projects = True
ver_boss3_vivo = True
ver_flappys_gigantes = True
ver_victoria = True


BOSS1 = JEFE1.Boss1((1280,234))
STOP_BOSS1 = False
STOP_BOSS2 = False

BOSS2 = JEFE2.Boss2((1280,234))
STOP_BOSS3 = False
STOP_BOSS4 = False

BOSS3 = JEFE3.Boss3((1298,234))
STOP_BOSS5 = False
STOP_BOSS6 = False

# Elementos extras
color_azul = (11, 16, 132)
color_negro = (0, 0, 0)
screen_rect = screen.get_rect()
FONT = pygame.font.SysFont("Bauhaus 93", 32)
VIDAS = 10
NIVEL = 0
MENU = True
JUEGO = False
PLANETA1 = True
PLANETA2 = True
PLANETA3 = True
PLANETA4 = True
PLANETA5 = True
PLANETA6 = True
PLANETA7 = True
PLANETA8 = True
FPS60 = 60
FPS30 = 30
grados = 0

mover_izq = False
act_mover_izq = True
oscilar_boss = True
act_oscilar_boss = False

mover_izq2 = False
act_mover_izq2 = True
oscilar_boss2 = True
act_oscilar_boss2 = False

act_mover_izq3 = True
oscilar_boss3 = True
act_oscilar_boss3 = False
mover_izq3 = False

activar_tubos = True
activar_tubos2 = True
activar_tubos3 = True
transicionador_tubos_boss_1 = True
transicionador_tubos_boss_2 = True
transicionador_tubos_boss_3 = True
transicion_menu_tubos = False
pygame.mixer.set_num_channels(60)
x = 0
x2 = 0
x3 = 0
x4 = 0
x5 = 0
game_over = pygame.image.load("IMAGENES_VIDEOJUEGO/GAME_OVER.png").convert()
mov_flap_der = False
mov_flap_izq = True
mov_flap_izq2 = True
mov_flap_izq3 = True


# Inicialización
while True:

    mixer.music.load("MUSICA/MUSICA_MENU.wav")
    mixer.music.set_volume(.03)
    mixer.music.play(-1)

    # Pantalla menu
    while MENU:

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
                MENU = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    MENU = False
                    JUEGO = True
                    transicion_menu_tubos = True
                    mixer.music.load("MUSICA/TRAN_MENU_JUEGO.wav")
                    mixer.music.set_volume(.1)
                    mixer.music.play(-1)




        screen.fill((0,0,0))
        screen.blit(bg_menu,[0,0])
        screen.blit(NOMBRE,[125,85])
        screen.blit(TUBO_DERECHA,[1040,115])
        screen.blit(TUBO_IZQUIERDA,[180,115])
        screen.blit(TUBO_CENTRO,[259,117])
        screen.blit(TUBO_DERECHA,[1040,258])
        screen.blit(TUBO_IZQUIERDA,[180,258])
        screen.blit(TUBO_CENTRO,[259,260])
        screen.blit(TUBO_ARRIBA1,[180,150])
        screen.blit(TUBO_ABAJO1,[180,173])
        screen.blit(TUBO_ARRIBA2,[1090,150])
        screen.blit(TUBO_ABAJO2,[1090,173])
        screen.blit(PSTS,[450,334])
        PAJARO1.UPDATE(event)
        screen.blit(PAJARO1.image, PAJARO1.rect)
        PAJARO2.UPDATE(event)
        screen.blit(PAJARO2.image, PAJARO2.rect)
        PAJARO3.UPDATE(event)
        screen.blit(PAJARO3.image, PAJARO3.rect)
        PAJARO4.UPDATE(event)
        screen.blit(PAJARO4.image, PAJARO4.rect)
        PAJARO5.UPDATE(event)
        screen.blit(PAJARO5.image, PAJARO5.rect)
        PAJARO6.UPDATE(event)
        screen.blit(PAJARO6.image, PAJARO6.rect)
        screen.blit(planetamenu1.image, planetamenu1.rect)
        screen.blit(planetamenu2.image, planetamenu2.rect)
        screen.blit(planetamenu3.image, planetamenu3.rect)
        screen.blit(planetamenu4.image, planetamenu4.rect)
        screen.blit(planetamenu5.image, planetamenu5.rect)
        screen.blit(planetamenu6.image, planetamenu6.rect)
        screen.blit(planetamenu7.image, planetamenu7.rect)
        screen.blit(planetamenu8.image, planetamenu8.rect)

        # Validacion de posiciones
        if planetamenu1.rect.y == 0 and planetamenu1.rect.x == 0 \
           and planetamenu2.rect.y == 490 and planetamenu2.rect.x == 0 \
           and planetamenu3.rect.y == 490 and planetamenu3.rect.x == 1200 \
           and planetamenu4.rect.y == 0 and planetamenu4.rect.x == 1200:
            PLANETA1 = False
            PLANETA2 = True
            PLANETA3 = True
            PLANETA4 = True
        if planetamenu1.rect.y == 490 and planetamenu1.rect.x == 0 \
           and planetamenu2.rect.y == 490 and planetamenu2.rect.x == 1200 \
           and planetamenu3.rect.y == 0 and planetamenu3.rect.x == 1200 \
           and planetamenu4.rect.y == 0 and planetamenu4.rect.x == 0:
            PLANETA1 = True
            PLANETA2 = False
            PLANETA3 = True
            PLANETA4 = True
        if planetamenu1.rect.y == 490 and planetamenu1.rect.x == 1200 \
           and planetamenu2.rect.y == 0 and planetamenu2.rect.x == 1200 \
           and planetamenu3.rect.y == 0 and planetamenu3.rect.x == 0 \
           and planetamenu4.rect.y == 490 and planetamenu4.rect.x == 0:
            PLANETA1 = True
            PLANETA2 = True
            PLANETA3 = False
            PLANETA4 = True
        if planetamenu1.rect.y == 0 and planetamenu1.rect.x == 1200 \
           and planetamenu2.rect.y == 0 and planetamenu2.rect.x == 0 \
           and planetamenu3.rect.y == 490 and planetamenu3.rect.x == 0 \
           and planetamenu4.rect.y == 490 and planetamenu4.rect.x == 1200:
            PLANETA1 = True
            PLANETA2 = True
            PLANETA3 = True
            PLANETA4 = False


        if planetamenu5.rect.y == 262 and planetamenu5.rect.x == 0:
            PLANETA5 = False
            PLANETA6 = True
            PLANETA7 = True
            PLANETA8 = True
        if planetamenu5.rect.y == 0 and planetamenu5.rect.x == 0 \
           and planetamenu6.rect.y == 490 and planetamenu6.rect.x == 0 \
           and planetamenu7.rect.y == 490 and planetamenu7.rect.x == 1200 \
           and planetamenu8.rect.y == 0 and planetamenu8.rect.x == 1200:
            PLANETA5 = False
            PLANETA6 = True
            PLANETA7 = True
            PLANETA8 = True
        if planetamenu5.rect.y == 490 and planetamenu5.rect.x == 0 \
           and planetamenu6.rect.y == 490 and planetamenu6.rect.x == 1200 \
           and planetamenu7.rect.y == 0 and planetamenu7.rect.x == 1200 \
           and planetamenu8.rect.y == 0 and planetamenu8.rect.x == 0:
            PLANETA5 = True
            PLANETA6 = False
            PLANETA7 = True
            PLANETA8 = True
        if planetamenu5.rect.y == 490 and planetamenu5.rect.x == 1200 \
           and planetamenu6.rect.y == 0 and planetamenu6.rect.x == 1200 \
           and planetamenu7.rect.y == 0 and planetamenu7.rect.x == 0 \
           and planetamenu8.rect.y == 490 and planetamenu8.rect.x == 0:
            PLANETA5 = True
            PLANETA6 = True
            PLANETA7 = False
            PLANETA8 = True
        if planetamenu5.rect.y == 0 and planetamenu5.rect.x == 1200 \
           and planetamenu6.rect.y == 0 and planetamenu6.rect.x == 0 \
           and planetamenu7.rect.y == 490 and planetamenu7.rect.x == 0 \
           and planetamenu8.rect.y == 490 and planetamenu8.rect.x == 1200:
            PLANETA5 = True
            PLANETA2 = True
            PLANETA7 = True
            PLANETA8 = False

        # Validación de velocidad y movimiento
        if PLANETA1 == False:
            planetamenu1.rect.y += 5
            planetamenu2.rect.x += 12
            planetamenu3.rect.y -= 5
            planetamenu4.rect.x -= 12
        if PLANETA2 == False:
            planetamenu1.rect.x += 12
            planetamenu2.rect.y -= 5
            planetamenu3.rect.x -= 12
            planetamenu4.rect.y += 5
        if PLANETA3 == False:
            planetamenu1.rect.y -= 5
            planetamenu2.rect.x -= 12
            planetamenu3.rect.y += 5
            planetamenu4.rect.x += 12
        if PLANETA4 == False:
            planetamenu1.rect.x -= 12
            planetamenu2.rect.y += 5
            planetamenu3.rect.x += 12
            planetamenu4.rect.y -= 5

        if PLANETA5 == False:
            planetamenu5.rect.y += 5
            planetamenu6.rect.x += 12
            planetamenu7.rect.y -= 5
            planetamenu8.rect.x -= 12
        if PLANETA6 == False:
            planetamenu5.rect.x += 12
            planetamenu6.rect.y -= 5
            planetamenu7.rect.x -= 12
            planetamenu8.rect.y += 5
        if PLANETA7 == False:
            planetamenu5.rect.y -= 5
            planetamenu6.rect.x -= 12
            planetamenu7.rect.y += 5
            planetamenu8.rect.x += 12
        if PLANETA8 == False:
            planetamenu5.rect.x -= 12
            planetamenu6.rect.y += 5
            planetamenu7.rect.x += 12
            planetamenu8.rect.y -= 5

        # Validación de las barreras
        if planetamenu1.rect.y <= 0:
            planetamenu1.rect.y = 0
        if planetamenu1.rect.y >= 490:
            planetamenu1.rect.y = 490
        if planetamenu1.rect.x <= 0:
            planetamenu1.rect.x = 0
        if planetamenu1.rect.x >= 1200:
            planetamenu1.rect.x = 1200
        if planetamenu2.rect.y <= 0:
            planetamenu2.rect.y = 0
        if planetamenu2.rect.y >= 490:
            planetamenu2.rect.y = 490
        if planetamenu2.rect.x <= 0:
            planetamenu2.rect.x = 0
        if planetamenu2.rect.x >= 1200:
            planetamenu2.rect.x = 1200
        if planetamenu3.rect.y <= 0:
            planetamenu3.rect.y = 0
        if planetamenu3.rect.y >= 490:
            planetamenu3.rect.y = 490
        if planetamenu3.rect.x <= 0:
            planetamenu3.rect.x = 0
        if planetamenu3.rect.x >= 1200:
            planetamenu3.rect.x = 1200
        if planetamenu4.rect.y <= 0:
            planetamenu4.rect.y = 0
        if planetamenu4.rect.y >= 490:
            planetamenu4.rect.y = 490
        if planetamenu4.rect.x <= 0:
            planetamenu4.rect.x = 0
        if planetamenu4.rect.x >= 1200:
            planetamenu4.rect.x = 1200
        if planetamenu5.rect.y <= 0:
            planetamenu5.rect.y = 0
        if planetamenu5.rect.y >= 490:
            planetamenu5.rect.y = 490
        if planetamenu5.rect.x <= 0:
            planetamenu5.rect.x = 0
        if planetamenu5.rect.x >= 1200:
            planetamenu5.rect.x = 1200
        if planetamenu6.rect.y <= 0:
            planetamenu6.rect.y = 0
        if planetamenu6.rect.y >= 490:
            planetamenu6.rect.y = 490
        if planetamenu6.rect.x <= 0:
            planetamenu6.rect.x = 0
        if planetamenu6.rect.x >= 1200:
            planetamenu6.rect.x = 1200
        if planetamenu7.rect.y <= 0:
            planetamenu7.rect.y = 0
        if planetamenu7.rect.y >= 490:
            planetamenu7.rect.y = 490
        if planetamenu7.rect.x <= 0:
            planetamenu7.rect.x = 0
        if planetamenu7.rect.x >= 1200:
            planetamenu7.rect.x = 1200
        if planetamenu8.rect.y <= 0:
            planetamenu8.rect.y = 0
        if planetamenu8.rect.y >= 490:
            planetamenu8.rect.y = 490
        if planetamenu8.rect.x <= 0:
            planetamenu8.rect.x = 0
        if planetamenu8.rect.x >= 1200:
            planetamenu8.rect.x = 1200

        pygame.display.flip()
        clock.tick(FPS60)


    # Pantalla juego
    while JUEGO:

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
                JUEGO = False

        if transicion_menu_tubos == True:
            RELOJ_TRAN_MENU_TUBOS1.rect.x += 1
            if RELOJ_TRAN_MENU_TUBOS1.rect.x >= 1:
                x_relativa2 = x2 % bg_transicion.get_rect().width
                screen.blit(bg_transicion,[x_relativa2 - bg_transicion.get_rect().width ,0])
                if x_relativa2 < pantalla_x:
                    screen.blit(bg_transicion,(x_relativa2,0))
                if RELOJ_TRAN_MENU_TUBOS1.rect.x >= 20:
                    x2 -= 3
                if RELOJ_TRAN_MENU_TUBOS1.rect.x >= 30:
                    x2 -= 3
                if RELOJ_TRAN_MENU_TUBOS1.rect.x >= 40:
                    x2 -= 3
                if RELOJ_TRAN_MENU_TUBOS1.rect.x >= 50:
                    x2 -= 3
                if RELOJ_TRAN_MENU_TUBOS1.rect.x >= 60:
                    x2 -= 3
                if RELOJ_TRAN_MENU_TUBOS1.rect.x >= 70:
                    x2 -= 3
                if RELOJ_TRAN_MENU_TUBOS1.rect.x >= 80:
                    x2 -= 3
                if RELOJ_TRAN_MENU_TUBOS1.rect.x >= 90:
                    x2 -= 3
                if RELOJ_TRAN_MENU_TUBOS1.rect.x >= 100:
                    x2 -= 3
                if RELOJ_TRAN_MENU_TUBOS1.rect.x >= 110:
                    x2 -= 3
                if RELOJ_TRAN_MENU_TUBOS1.rect.x >= 120:
                    x2 -= 3
                if RELOJ_TRAN_MENU_TUBOS1.rect.x >= 130:
                    x2 -= 3
                if RELOJ_TRAN_MENU_TUBOS1.rect.x >= 140:
                    x2 -= 3
                if RELOJ_TRAN_MENU_TUBOS1.rect.x >= 150:
                    x2 -= 3
                if RELOJ_TRAN_MENU_TUBOS1.rect.x >= 160:
                    x2 -= 3
                if RELOJ_TRAN_MENU_TUBOS1.rect.x >= 170:
                    x2 -= 3
                if RELOJ_TRAN_MENU_TUBOS1.rect.x >= 180:
                    x2 -= 3
                if RELOJ_TRAN_MENU_TUBOS1.rect.x >= 190:
                    x2 -= 3
                if RELOJ_TRAN_MENU_TUBOS1.rect.x >= 200:
                    x2 -= 3
                if RELOJ_TRAN_MENU_TUBOS1.rect.x >= 210:
                    x2 -= 3
                if RELOJ_TRAN_MENU_TUBOS1.rect.x >= 220:
                    x2 -= 3


            if RELOJ_TRAN_MENU_TUBOS1.rect.x == 230:
                transicion_menu_tubos = False
                NIVEL = 1
            if RELOJ_TRAN_MENU_TUBOS1.rect.x == 220:
                mixer.music.load("MUSICA/MUSICA_JUEGO.wav")
                mixer.music.set_volume(.03)
                mixer.music.play(-1)



        if VIDAS > 0:
            if NIVEL == 1:

                screen.blit(bg_1,[0,0])
                screen.blit(Flappy.image, Flappy.rect)
                Flappy.Movimiento_Pajaro(event)

                if activar_tubos == True:

                    screen.blit(tubo_abajo1.image, tubo_abajo1.rect)
                    tubo_abajo1.update(event)
                    tubo_abajo1.rect.x -= 10
                    screen.blit(tubo_abajo2.image, tubo_abajo2.rect)
                    tubo_abajo2.update(event)
                    tubo_abajo2.rect.x -= 10
                    screen.blit(tubo_abajo3.image, tubo_abajo3.rect)
                    tubo_abajo3.update(event)
                    tubo_abajo3.rect.x -= 10
                    screen.blit(tubo_abajo4.image, tubo_abajo4.rect)
                    tubo_abajo4.update(event)
                    tubo_abajo4.rect.x -= 10
                    screen.blit(tubo_abajo5.image, tubo_abajo5.rect)
                    tubo_abajo5.update(event)
                    tubo_abajo5.rect.x -= 10
                    screen.blit(tubo_abajo6.image, tubo_abajo6.rect)
                    tubo_abajo6.update(event)
                    tubo_abajo6.rect.x -= 10
                    screen.blit(tubo_abajo7.image, tubo_abajo7.rect)
                    tubo_abajo7.update(event)
                    tubo_abajo7.rect.x -= 10
                    screen.blit(tubo_abajo8.image, tubo_abajo8.rect)
                    tubo_abajo8.update(event)
                    tubo_abajo8.rect.x -= 10
                    screen.blit(tubo_abajo9.image, tubo_abajo9.rect)
                    tubo_abajo9.update(event)
                    tubo_abajo9.rect.x -= 10
                    screen.blit(tubo_abajo10.image, tubo_abajo10.rect)
                    tubo_abajo10.update(event)
                    tubo_abajo10.rect.x -= 10
                    screen.blit(tubo_arriba1.image, tubo_arriba1.rect)
                    tubo_arriba1.update(event)
                    tubo_arriba1.rect.x -= 10
                    screen.blit(tubo_arriba2.image, tubo_arriba2.rect)
                    tubo_arriba2.update(event)
                    tubo_arriba2.rect.x -= 10
                    screen.blit(tubo_arriba3.image, tubo_arriba3.rect)
                    tubo_arriba3.update(event)
                    tubo_arriba3.rect.x -= 10
                    screen.blit(tubo_arriba4.image, tubo_arriba4.rect)
                    tubo_arriba4.update(event)
                    tubo_arriba4.rect.x -= 10
                    screen.blit(tubo_arriba5.image, tubo_arriba5.rect)
                    tubo_arriba5.update(event)
                    tubo_arriba5.rect.x -= 10
                    screen.blit(tubo_arriba6.image, tubo_arriba6.rect)
                    tubo_arriba6.update(event)
                    tubo_arriba6.rect.x -= 10
                    screen.blit(tubo_arriba7.image, tubo_arriba7.rect)
                    tubo_arriba7.update(event)
                    tubo_arriba7.rect.x -= 10
                    screen.blit(tubo_arriba8.image, tubo_arriba8.rect)
                    tubo_arriba8.update(event)
                    tubo_arriba8.rect.x -= 10
                    screen.blit(tubo_arriba9.image, tubo_arriba9.rect)
                    tubo_arriba9.update(event)
                    tubo_arriba9.rect.x -= 10
                    screen.blit(tubo_arriba10.image, tubo_arriba10.rect)
                    tubo_arriba10.update(event)
                    tubo_arriba10.rect.x -= 10


                    if tubo_abajo1.rect.colliderect(Flappy.rect):
                        VIDAS -= 1
                        screen.blit(BUM.image, Flappy.rect)
                        Flappy.rect.y = 250
                        Flappy.rect.x = 300
                        pygame.mixer.Channel(2).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                        pygame.mixer.Channel(2).set_volume(.15)
                    if tubo_arriba1.rect.colliderect(Flappy.rect):
                        VIDAS -= 1
                        screen.blit(BUM.image, Flappy.rect)
                        Flappy.rect.y = 250
                        Flappy.rect.x = 300
                        pygame.mixer.Channel(2).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                        pygame.mixer.Channel(2).set_volume(.15)
                    if tubo_abajo2.rect.colliderect(Flappy.rect):
                        VIDAS -= 1
                        screen.blit(BUM.image, Flappy.rect)
                        Flappy.rect.y = 300
                        Flappy.rect.x = 300
                        pygame.mixer.Channel(2).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                        pygame.mixer.Channel(2).set_volume(.15)
                    if tubo_arriba2.rect.colliderect(Flappy.rect):
                        VIDAS -= 1
                        screen.blit(BUM.image, Flappy.rect)
                        Flappy.rect.y = 300
                        Flappy.rect.x = 300
                        pygame.mixer.Channel(2).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                        pygame.mixer.Channel(2).set_volume(.15)
                    if tubo_abajo3.rect.colliderect(Flappy.rect):
                        VIDAS -= 1
                        screen.blit(BUM.image, Flappy.rect)
                        Flappy.rect.y = 200
                        Flappy.rect.x = 300
                        pygame.mixer.Channel(2).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                        pygame.mixer.Channel(2).set_volume(.15)
                    if tubo_arriba3.rect.colliderect(Flappy.rect):
                        VIDAS -= 1
                        screen.blit(BUM.image, Flappy.rect)
                        Flappy.rect.y = 200
                        Flappy.rect.x = 300
                        pygame.mixer.Channel(2).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                        pygame.mixer.Channel(2).set_volume(.15)
                    if tubo_abajo4.rect.colliderect(Flappy.rect):
                        VIDAS -= 1
                        screen.blit(BUM.image, Flappy.rect)
                        Flappy.rect.y = 300
                        Flappy.rect.x = 300
                        pygame.mixer.Channel(2).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                        pygame.mixer.Channel(2).set_volume(.15)
                    if tubo_arriba4.rect.colliderect(Flappy.rect):
                        VIDAS -= 1
                        screen.blit(BUM.image, Flappy.rect)
                        Flappy.rect.y = 300
                        Flappy.rect.x = 300
                        pygame.mixer.Channel(2).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                        pygame.mixer.Channel(2).set_volume(.15)
                    if tubo_abajo5.rect.colliderect(Flappy.rect):
                        VIDAS -= 1
                        screen.blit(BUM.image, Flappy.rect)
                        Flappy.rect.y = 250
                        Flappy.rect.x = 300
                        pygame.mixer.Channel(2).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                        pygame.mixer.Channel(2).set_volume(.15)
                    if tubo_arriba5.rect.colliderect(Flappy.rect):
                        VIDAS -= 1
                        screen.blit(BUM.image, Flappy.rect)
                        Flappy.rect.y = 250
                        Flappy.rect.x = 300
                        pygame.mixer.Channel(2).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                        pygame.mixer.Channel(2).set_volume(.15)
                    if tubo_abajo6.rect.colliderect(Flappy.rect):
                        VIDAS -= 1
                        screen.blit(BUM.image, Flappy.rect)
                        Flappy.rect.y = 300
                        Flappy.rect.x = 300
                        pygame.mixer.Channel(2).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                        pygame.mixer.Channel(2).set_volume(.15)
                    if tubo_arriba6.rect.colliderect(Flappy.rect):
                        VIDAS -= 1
                        screen.blit(BUM.image, Flappy.rect)
                        Flappy.rect.y = 300
                        Flappy.rect.x = 300
                        pygame.mixer.Channel(2).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                        pygame.mixer.Channel(2).set_volume(.15)
                    if tubo_abajo7.rect.colliderect(Flappy.rect):
                        VIDAS -= 1
                        screen.blit(BUM.image, Flappy.rect)
                        Flappy.rect.y = 200
                        Flappy.rect.x = 300
                        pygame.mixer.Channel(2).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                        pygame.mixer.Channel(2).set_volume(.15)
                    if tubo_arriba7.rect.colliderect(Flappy.rect):
                        VIDAS -= 1
                        screen.blit(BUM.image, Flappy.rect)
                        Flappy.rect.y = 200
                        Flappy.rect.x = 300
                        pygame.mixer.Channel(2).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                        pygame.mixer.Channel(2).set_volume(.15)
                    if tubo_abajo8.rect.colliderect(Flappy.rect):
                        VIDAS -= 1
                        screen.blit(BUM.image, Flappy.rect)
                        Flappy.rect.y = 300
                        Flappy.rect.x = 300
                        pygame.mixer.Channel(2).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                        pygame.mixer.Channel(2).set_volume(.15)
                    if tubo_arriba8.rect.colliderect(Flappy.rect):
                        VIDAS -= 1
                        screen.blit(BUM.image, Flappy.rect)
                        Flappy.rect.y = 300
                        Flappy.rect.x = 300
                        pygame.mixer.Channel(2).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                        pygame.mixer.Channel(2).set_volume(.15)
                    if tubo_abajo9.rect.colliderect(Flappy.rect):
                        VIDAS -= 1
                        screen.blit(BUM.image, Flappy.rect)
                        Flappy.rect.y = 200
                        Flappy.rect.x = 300
                        pygame.mixer.Channel(2).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                        pygame.mixer.Channel(2).set_volume(.15)
                    if tubo_arriba9.rect.colliderect(Flappy.rect):
                        VIDAS -= 1
                        screen.blit(BUM.image, Flappy.rect)
                        Flappy.rect.y = 200
                        Flappy.rect.x = 300
                        pygame.mixer.Channel(2).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                        pygame.mixer.Channel(2).set_volume(.15)
                    if tubo_abajo10.rect.colliderect(Flappy.rect):
                        VIDAS -= 1
                        screen.blit(BUM.image, Flappy.rect)
                        Flappy.rect.y = 250
                        Flappy.rect.x = 300
                        pygame.mixer.Channel(2).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                        pygame.mixer.Channel(2).set_volume(.15)
                    if tubo_arriba10.rect.colliderect(Flappy.rect):
                        VIDAS -= 1
                        screen.blit(BUM.image, Flappy.rect)
                        Flappy.rect.y = 250
                        Flappy.rect.x = 300
                        pygame.mixer.Channel(2).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                        pygame.mixer.Channel(2).set_volume(.15)



                    Flappy.rect.x -= 5
                    if Flappy.rect.x <= 140:
                        Flappy.rect.x = 140




                if transicionador_tubos_boss_1 == True:
                    RELOJ_TRAN_TUBOS_BOSS_NVL1.rect.x += 1
                    if RELOJ_TRAN_TUBOS_BOSS_NVL1.rect.x == 700:
                        activar_tubos = False
                    if RELOJ_TRAN_TUBOS_BOSS_NVL1.rect.x == 635:
                        JEFE1_TOTAL = True

                RELOJ3.rect.x += 1
                if RELOJ3.rect.x >= 740:
                    x_relativa = x % bg_espacial.get_rect().width
                    screen.blit(bg_espacial,[x_relativa - bg_espacial.get_rect().width ,0])
                    if x_relativa < pantalla_x:
                        screen.blit(bg_espacial,(x_relativa,0))
                    x -= 30
                    screen.blit(Flappy.image, Flappy.rect)
                    screen.blit(BOSS1.image, BOSS1.rect)
                    if RELOJ3.rect.x >= 1300:
                        x -= 10
                        mov_flap_der = True
                        if mov_flap_der == True:
                            Flappy.rect.x += 7
                    if RELOJ3.rect.x >= 1310:
                        x -= 10
                    if RELOJ3.rect.x >= 1320:
                        x -= 10
                    if RELOJ3.rect.x >= 1330:
                        x -= 10
                    if RELOJ3.rect.x >= 1340:
                        x -= 10
                    if RELOJ3.rect.x >= 1350:
                        x -= 10
                    if RELOJ3.rect.x >= 1475:
                        NIVEL = 2
                        mov_flap_der = False
                        pygame.mixer.Channel(39).play(pygame.mixer.Sound("MUSICA/LIVE_UP2.wav"))
                        pygame.mixer.Channel(39).set_volume(.02)



                if JEFE1_TOTAL == True:

                    screen.blit(BOSS1.image, BOSS1.rect)
                    FBS = True

                    if act_mover_izq == True:

                        if BOSS1.rect.y == 234:
                            mover_izq = True
                            if mover_izq == True:
                                BOSS1.rect.x -= 1
                        if BOSS1.rect.x <= 1210:
                            mover_izq = False
                            BOSS1.rect.x = 1210
                            act_oscilar_boss = True


                    if act_oscilar_boss == True:

                        PRIMERAFB = True

                        if BOSS1.rect.x == 1210:

                            act_mover_izq = False
                            if BOSS1.rect.y <= 0:
                                BOSS1.rect.y = 0
                                oscilar_boss = False
                            if BOSS1.rect.y >= 470:
                                BOSS1.rect.y = 470
                                oscilar_boss = True
                            if oscilar_boss == False:
                                BOSS1.rect.y += 6
                            elif oscilar_boss == True:
                                BOSS1.rect.y -= 6

                    if FBS == True:

                        if PRIMERA_FB == True:
                            if BOSS1.rect.y == 0:
                                ver_bola_fuego1 = True
                            if ver_bola_fuego1 == True:
                                if BOSS1.rect.y == 0 and BOSS1.rect.x == 1210:
                                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("MUSICA/FIREBALL.wav"))
                                    pygame.mixer.Channel(1).set_volume(.15)
                                screen.blit(bola_fuego1.image, bola_fuego1.rect)
                                mover_bola_fuego1 = True
                                SEGUNDA_FB = True
                                if mover_bola_fuego1 == True:
                                    bola_fuego1.rect.x -= 15
                                    if bola_fuego1.rect.colliderect(Flappy.rect):
                                        VIDAS -= 1
                                        ver_bola_fuego1 = False
                                        screen.blit(BUM.image, Flappy.rect)
                                        pygame.mixer.Channel(2).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                                        pygame.mixer.Channel(2).set_volume(.15)

                        if SEGUNDA_FB == True:
                            RELOJ.rect.x -= 1
                            if RELOJ.rect.x == 1255:
                                ver_bola_fuego2 = True
                            if ver_bola_fuego2 == True:
                                if MUSICA_FB_2 == True:
                                    pygame.mixer.Channel(3).play(pygame.mixer.Sound("MUSICA/FIREBALL.wav"))
                                    pygame.mixer.Channel(3).set_volume(.15)
                                screen.blit(bola_fuego2.image, bola_fuego2.rect)
                                mover_bola_fuego2 = True
                                TERCERA_FB = True
                                if mover_bola_fuego2 == True:
                                    MUSICA_FB_2 = False
                                    bola_fuego2.rect.x -= 15
                                    if bola_fuego2.rect.colliderect(Flappy.rect):
                                        VIDAS -= 1
                                        ver_bola_fuego2 = False
                                        screen.blit(BUM2.image, Flappy.rect)
                                        pygame.mixer.Channel(4).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                                        pygame.mixer.Channel(4).set_volume(.15)

                        if TERCERA_FB == True:
                            if RELOJ.rect.x == 1230:
                                ver_bola_fuego3 = True
                            if ver_bola_fuego3 == True:
                                if MUSICA_FB_3 == True:
                                    pygame.mixer.Channel(5).play(pygame.mixer.Sound("MUSICA/FIREBALL.wav"))
                                    pygame.mixer.Channel(5).set_volume(.15)
                                screen.blit(bola_fuego3.image, bola_fuego3.rect)
                                mover_bola_fuego3 = True
                                CUARTA_FB = True
                                if mover_bola_fuego3 == True:
                                    MUSICA_FB_3 = False
                                    bola_fuego3.rect.x -= 15
                                    if bola_fuego3.rect.colliderect(Flappy.rect):
                                        VIDAS -= 1
                                        ver_bola_fuego3 = False
                                        screen.blit(BUM3.image, Flappy.rect)
                                        pygame.mixer.Channel(6).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                                        pygame.mixer.Channel(6).set_volume(.15)

                        if CUARTA_FB == True:
                            if RELOJ.rect.x == 1210:
                                ver_bola_fuego4 = True
                            if ver_bola_fuego4 == True:
                                if MUSICA_FB_4 == True:
                                    pygame.mixer.Channel(7).play(pygame.mixer.Sound("MUSICA/FIREBALL.wav"))
                                    pygame.mixer.Channel(7).set_volume(.15)
                                screen.blit(bola_fuego4.image, bola_fuego4.rect)
                                mover_bola_fuego4 = True
                                QUINTA_FB = True
                                if mover_bola_fuego4 == True:
                                    MUSICA_FB_4 = False
                                    bola_fuego4.rect.x -= 15
                                    if bola_fuego4.rect.colliderect(Flappy.rect):
                                        VIDAS -= 1
                                        ver_bola_fuego4 = False
                                        screen.blit(BUM4.image, Flappy.rect)
                                        pygame.mixer.Channel(8).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                                        pygame.mixer.Channel(8).set_volume(.15)

                        if QUINTA_FB == True:
                            if RELOJ.rect.x == 1170:
                                ver_bola_fuego5 = True
                            if ver_bola_fuego5 == True:
                                if MUSICA_FB_5 == True:
                                    pygame.mixer.Channel(9).play(pygame.mixer.Sound("MUSICA/FIREBALL.wav"))
                                    pygame.mixer.Channel(9).set_volume(.15)
                                screen.blit(bola_fuego5.image, bola_fuego5.rect)
                                mover_bola_fuego5 = True
                                SEXTA_FB = True
                                if mover_bola_fuego5 == True:
                                    MUSICA_FB_5 = False
                                    bola_fuego5.rect.x -= 15
                                    if bola_fuego5.rect.colliderect(Flappy.rect):
                                        VIDAS -= 1
                                        ver_bola_fuego5 = False
                                        screen.blit(BUM5.image, Flappy.rect)
                                        pygame.mixer.Channel(10).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                                        pygame.mixer.Channel(10).set_volume(.15)

                        if SEXTA_FB == True:
                            if RELOJ.rect.x == 1150:
                                ver_bola_fuego6 = True
                            if ver_bola_fuego6 == True:
                                if MUSICA_FB_6 == True:
                                    pygame.mixer.Channel(11).play(pygame.mixer.Sound("MUSICA/FIREBALL.wav"))
                                    pygame.mixer.Channel(11).set_volume(.15)
                                screen.blit(bola_fuego6.image, bola_fuego6.rect)
                                mover_bola_fuego6 = True
                                SEPTIMA_FB = True
                                if mover_bola_fuego6 == True:
                                    MUSICA_FB_6 = False
                                    bola_fuego6.rect.x -= 15
                                    if bola_fuego6.rect.colliderect(Flappy.rect):
                                        VIDAS -= 1
                                        ver_bola_fuego6 = False
                                        screen.blit(BUM6.image, Flappy.rect)
                                        pygame.mixer.Channel(12).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                                        pygame.mixer.Channel(12).set_volume(.15)

                        if SEPTIMA_FB == True:
                            if RELOJ.rect.x == 1130:
                                ver_bola_fuego7 = True
                            if ver_bola_fuego7 == True:
                                if MUSICA_FB_7 == True:
                                    pygame.mixer.Channel(13).play(pygame.mixer.Sound("MUSICA/FIREBALL.wav"))
                                    pygame.mixer.Channel(13).set_volume(.15)
                                screen.blit(bola_fuego7.image, bola_fuego7.rect)
                                mover_bola_fuego7 = True
                                OCTAVA_FB = True
                                if mover_bola_fuego7 == True:
                                    MUSICA_FB_7 = False
                                    bola_fuego7.rect.x -= 15
                                    if bola_fuego7.rect.colliderect(Flappy.rect):
                                        VIDAS -= 1
                                        ver_bola_fuego7 = False
                                        screen.blit(BUM7.image, Flappy.rect)
                                        pygame.mixer.Channel(14).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                                        pygame.mixer.Channel(14).set_volume(.15)

                        if OCTAVA_FB == True:
                            if RELOJ.rect.x == 1100:
                                ver_bola_fuego8 = True
                            if ver_bola_fuego8 == True:
                                if MUSICA_FB_8 == True:
                                    pygame.mixer.Channel(15).play(pygame.mixer.Sound("MUSICA/FIREBALL.wav"))
                                    pygame.mixer.Channel(15).set_volume(.15)
                                screen.blit(bola_fuego8.image, bola_fuego8.rect)
                                mover_bola_fuego8 = True
                                NOVENA_FB = True
                                if mover_bola_fuego8 == True:
                                    MUSICA_FB_8 = False
                                    bola_fuego8.rect.x -= 15
                                    if bola_fuego8.rect.colliderect(Flappy.rect):
                                        VIDAS -= 1
                                        ver_bola_fuego8 = False
                                        screen.blit(BUM8.image, Flappy.rect)
                                        pygame.mixer.Channel(16).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                                        pygame.mixer.Channel(16).set_volume(.15)

                        if NOVENA_FB == True:
                            if RELOJ.rect.x == 1080:
                                ver_bola_fuego9 = True
                            if ver_bola_fuego9 == True:
                                if MUSICA_FB_9 == True:
                                    pygame.mixer.Channel(17).play(pygame.mixer.Sound("MUSICA/FIREBALL.wav"))
                                    pygame.mixer.Channel(17).set_volume(.15)
                                screen.blit(bola_fuego9.image, bola_fuego9.rect)
                                mover_bola_fuego9 = True
                                DECIMA_FB = True
                                if mover_bola_fuego9 == True:
                                    MUSICA_FB_9 = False
                                    bola_fuego9.rect.x -= 15
                                    if bola_fuego9.rect.colliderect(Flappy.rect):
                                        VIDAS -= 1
                                        ver_bola_fuego9 = False
                                        screen.blit(BUM9.image, Flappy.rect)
                                        pygame.mixer.Channel(18).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                                        pygame.mixer.Channel(18).set_volume(.15)

                        if DECIMA_FB == True:
                            if RELOJ.rect.x == 1060:
                                ver_bola_fuego10 = True
                            if ver_bola_fuego10 == True:
                                if MUSICA_FB_10 == True:
                                    pygame.mixer.Channel(19).play(pygame.mixer.Sound("MUSICA/FIREBALL.wav"))
                                    pygame.mixer.Channel(19).set_volume(.15)
                                screen.blit(bola_fuego10.image, bola_fuego10.rect)
                                mover_bola_fuego10 = True
                                ONCEAVA_FB = True
                                if mover_bola_fuego10 == True:
                                    MUSICA_FB_10 = False
                                    bola_fuego10.rect.x -= 15
                                    if bola_fuego10.rect.colliderect(Flappy.rect):
                                        VIDAS -= 1
                                        ver_bola_fuego10 = False
                                        screen.blit(BUM10.image, Flappy.rect)
                                        pygame.mixer.Channel(20).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                                        pygame.mixer.Channel(20).set_volume(.15)

                        if ONCEAVA_FB == True:
                            if RELOJ.rect.x == 1010:
                                ver_bola_fuego11 = True
                            if ver_bola_fuego11 == True:
                                if MUSICA_FB_11 == True:
                                    pygame.mixer.Channel(21).play(pygame.mixer.Sound("MUSICA/FIREBALL.wav"))
                                    pygame.mixer.Channel(21).set_volume(.15)
                                screen.blit(bola_fuego11.image, bola_fuego11.rect)
                                mover_bola_fuego11 = True
                                DOCEAVA_FB = True
                                if mover_bola_fuego11 == True:
                                    MUSICA_FB_11 = False
                                    bola_fuego11.rect.x -= 15
                                    if bola_fuego11.rect.colliderect(Flappy.rect):
                                        VIDAS -= 1
                                        ver_bola_fuego11 = False
                                        screen.blit(BUM11.image, Flappy.rect)
                                        pygame.mixer.Channel(22).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                                        pygame.mixer.Channel(22).set_volume(.15)

                        if DOCEAVA_FB == True:
                            if RELOJ.rect.x == 990:
                                ver_bola_fuego12 = True
                            if ver_bola_fuego12 == True:
                                if MUSICA_FB_12 == True:
                                    pygame.mixer.Channel(23).play(pygame.mixer.Sound("MUSICA/FIREBALL.wav"))
                                    pygame.mixer.Channel(23).set_volume(.15)
                                screen.blit(bola_fuego12.image, bola_fuego12.rect)
                                mover_bola_fuego12 = True
                                TRECEAVA_FB = True
                                if mover_bola_fuego12 == True:
                                    MUSICA_FB_12 = False
                                    bola_fuego12.rect.x -= 15
                                    if bola_fuego12.rect.colliderect(Flappy.rect):
                                        VIDAS -= 1
                                        ver_bola_fuego12 = False
                                        screen.blit(BUM12.image, Flappy.rect)
                                        pygame.mixer.Channel(24).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                                        pygame.mixer.Channel(24).set_volume(.15)

                        if TRECEAVA_FB == True:
                            if RELOJ.rect.x == 970:
                                ver_bola_fuego13 = True
                            if ver_bola_fuego13 == True:
                                if MUSICA_FB_13 == True:
                                    pygame.mixer.Channel(25).play(pygame.mixer.Sound("MUSICA/FIREBALL.wav"))
                                    pygame.mixer.Channel(25).set_volume(.15)
                                screen.blit(bola_fuego13.image, bola_fuego13.rect)
                                mover_bola_fuego13 = True
                                STOP_BOSS1 = True
                                if mover_bola_fuego13 == True:
                                    MUSICA_FB_13 = False
                                    bola_fuego13.rect.x -= 15
                                    if bola_fuego13.rect.colliderect(Flappy.rect):
                                        VIDAS -= 1
                                        ver_bola_fuego13 = False
                                        screen.blit(BUM13.image, Flappy.rect)
                                        pygame.mixer.Channel(26).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                                        pygame.mixer.Channel(26).set_volume(.15)

                        if STOP_BOSS1 == True:

                            if FB_GRANDE1 == True:

                                if ACT_MOV_BOSS == True:
                                    if BOSS1.rect.y >= 235:
                                        BOSS1.rect.y = 235
                                        RELOJ.rect.y += 1
                                if RELOJ.rect.y == 240:
                                    ver_bola_fuego14 = True
                                if ver_bola_fuego14 == True:
                                    if MUSICA_FB_14 == True:
                                        pygame.mixer.Channel(27).play(pygame.mixer.Sound("MUSICA/FIREBALL.wav"))
                                        pygame.mixer.Channel(27).set_volume(.15)
                                    screen.blit(bola_fuego14.image, bola_fuego14.rect)
                                    mover_bola_fuego14 = True
                                    FB_GRANDE2 = True
                                    if mover_bola_fuego14 == True:
                                        MUSICA_FB_14 = False
                                        bola_fuego14.rect.x -= 15
                                        act_oscilar_boss = False
                                        if ACT_MOV_FB == True:
                                            BOSS1.rect.y -= 12
                                        if bola_fuego14.rect.colliderect(Flappy.rect):
                                            VIDAS -= 1
                                            ver_bola_fuego14 = False
                                            screen.blit(BUM14.image, Flappy.rect)
                                            pygame.mixer.Channel(28).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                                            pygame.mixer.Channel(28).set_volume(.15)

                            if FB_GRANDE2 == True:
                                RELOJ.rect.y += 1
                                if RELOJ.rect.y == 260:
                                    ver_bola_fuego15 = True
                                if ver_bola_fuego15 == True:
                                    if MUSICA_FB_15 == True:
                                        pygame.mixer.Channel(29).play(pygame.mixer.Sound("MUSICA/FIREBALL.wav"))
                                        pygame.mixer.Channel(29).set_volume(.15)
                                    screen.blit(bola_fuego15.image, bola_fuego15.rect)
                                    mover_bola_fuego15 = True
                                    if BOSS1.rect.y <= 0:
                                        BOSS1.rect.y = 0
                                    FB_GRANDE3 = True
                                    if mover_bola_fuego15 == True:
                                        MUSICA_FB_15 = False
                                        bola_fuego15.rect.x -= 15
                                        if bola_fuego15.rect.colliderect(Flappy.rect):
                                            VIDAS -= 1
                                            ver_bola_fuego15 = False
                                            screen.blit(BUM15.image, Flappy.rect)
                                            pygame.mixer.Channel(30).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                                            pygame.mixer.Channel(30).set_volume(.15)

                            if FB_GRANDE3 == True:
                                ACT_MOV_FB = False
                                ACT_MOV_BOSS = False
                                if MOV_BOSS == True:
                                    BOSS1.rect.y += 20
                                if RELOJ.rect.y == 280:
                                    ver_bola_fuego16 = True
                                if ver_bola_fuego16 == True:
                                    if MUSICA_FB_16 == True:
                                        pygame.mixer.Channel(31).play(pygame.mixer.Sound("MUSICA/FIREBALL.wav"))
                                        pygame.mixer.Channel(31).set_volume(.15)
                                    screen.blit(bola_fuego16.image, bola_fuego16.rect)
                                    mover_bola_fuego16 = True
                                    if mover_bola_fuego16 == True:
                                        MUSICA_FB_16 = False
                                        bola_fuego16.rect.x -= 15
                                        if bola_fuego16.rect.colliderect(Flappy.rect):
                                            VIDAS -= 1
                                            ver_bola_fuego16 = False
                                            screen.blit(BUM16.image, Flappy.rect)
                                            pygame.mixer.Channel(32).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                                            pygame.mixer.Channel(32).set_volume(.15)


                            if BOSS1.rect.y >= 470:
                                BOSS1.rect.y = 470
                                FB_GRANDE4 = True

                            if FB_GRANDE4 == True:

                                MOV_BOSS = False
                                if DESACTIVAR == True:
                                    BOSS1.rect.y -= 10
                                RELOJ2.rect.x += 1

                                if RELOJ2.rect.x == 28:
                                    ver_bola_fuego17 = True
                                if ver_bola_fuego17 == True:
                                    if MUSICA_FB_17 == True:
                                        pygame.mixer.Channel(33).play(pygame.mixer.Sound("MUSICA/FIREBALL.wav"))
                                        pygame.mixer.Channel(33).set_volume(.15)
                                    screen.blit(bola_fuego17.image, bola_fuego17.rect)
                                    mover_bola_fuego17 = True
                                    FB_GRANDE5 = True
                                    if mover_bola_fuego17 == True:
                                        MUSICA_FB_17 = False
                                        bola_fuego17.rect.x -= 15
                                        act_oscilar_boss = False
                                        if bola_fuego17.rect.colliderect(Flappy.rect):
                                            VIDAS -= 1
                                            ver_bola_fuego17 = False
                                            screen.blit(BUM17.image, Flappy.rect)
                                            pygame.mixer.Channel(34).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                                            pygame.mixer.Channel(34).set_volume(.15)

                            if FB_GRANDE5 == True:
                                if BOSS1.rect.y <= 10:
                                    DESACTIVAR = False
                                    BOSS1.rect.y = 10
                                    if DESACTIVAR2 == True:
                                        BOSS1.rect.y -= 5
                                    if RELOJ2.rect.x == 50:
                                        ver_bola_fuego18 = True
                                if ver_bola_fuego18 == True:
                                    if MUSICA_FB_18 == True:
                                        pygame.mixer.Channel(35).play(pygame.mixer.Sound("MUSICA/FIREBALL.wav"))
                                        pygame.mixer.Channel(35).set_volume(.15)
                                    screen.blit(bola_fuego18.image, bola_fuego18.rect)
                                    mover_bola_fuego18 = True
                                    FB_GRANDE6 = True
                                    if mover_bola_fuego18 == True:
                                        MUSICA_FB_18 = False
                                        bola_fuego18.rect.x -= 15
                                        act_oscilar_boss = False
                                        if bola_fuego18.rect.colliderect(Flappy.rect):
                                            VIDAS -= 1
                                            ver_bola_fuego18 = False
                                            screen.blit(BUM18.image, Flappy.rect)
                                            pygame.mixer.Channel(36).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                                            pygame.mixer.Channel(36).set_volume(.15)

                            if FB_GRANDE6 == True:
                                if DESACTIVAR3 == True:
                                    BOSS1.rect.y += 15
                                if BOSS1.rect.y >= 470:
                                    BOSS1.rect.y = 470
                                    DESACTIVAR3 = False
                                if RELOJ2.rect.x == 73:
                                    ver_bola_fuego19 = True
                                if ver_bola_fuego19 == True:
                                    if MUSICA_FB_19 == True:
                                        pygame.mixer.Channel(37).play(pygame.mixer.Sound("MUSICA/FIREBALL.wav"))
                                        pygame.mixer.Channel(37).set_volume(.15)
                                    screen.blit(bola_fuego19.image, bola_fuego19.rect)
                                    mover_bola_fuego19 = True
                                    if mover_bola_fuego19 == True:
                                        MUSICA_FB_19 = False
                                        bola_fuego19.rect.x -= 15
                                        BOSS1.rect.x += 2
                                        if bola_fuego19.rect.colliderect(Flappy.rect):
                                            VIDAS -= 1
                                            ver_bola_fuego19 = False
                                            screen.blit(BUM19.image, Flappy.rect)
                                            pygame.mixer.Channel(38).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                                            pygame.mixer.Channel(38).set_volume(.15)


                                    if BOSS1.rect.y <= 235:
                                        BOSS1.rect.y = 235
                                        if BOSS1.rect.y == 235:
                                            BOSS1.rect.x += 5
                                        RELOJ2.rect.x += 1
                                        if RELOJ2.rect.x == 250:
                                            FBS = False



            if NIVEL == 2:
                screen.blit(bg_2,[0,0])
                if mov_flap_izq == True:
                    Flappy.rect.x  = 140
                screen.blit(Flappy2.image, Flappy2.rect)
                Flappy2.Movimiento_Pajaro(event)

                if activar_tubos2 == True:

                    mov_flap_izq = False

                    screen.blit(tubo_abajo11.image, tubo_abajo11.rect)
                    tubo_abajo11.update(event)
                    tubo_abajo11.rect.x -= 15
                    screen.blit(tubo_abajo12.image, tubo_abajo12.rect)
                    tubo_abajo12.update(event)
                    tubo_abajo12.rect.x -= 15
                    screen.blit(tubo_abajo13.image, tubo_abajo13.rect)
                    tubo_abajo13.update(event)
                    tubo_abajo13.rect.x -= 15
                    screen.blit(tubo_abajo14.image, tubo_abajo14.rect)
                    tubo_abajo14.update(event)
                    tubo_abajo14.rect.x -= 15
                    screen.blit(tubo_abajo15.image, tubo_abajo15.rect)
                    tubo_abajo15.update(event)
                    tubo_abajo15.rect.x -= 15
                    screen.blit(tubo_abajo16.image, tubo_abajo16.rect)
                    tubo_abajo16.update(event)
                    tubo_abajo16.rect.x -= 15
                    screen.blit(tubo_abajo17.image, tubo_abajo17.rect)
                    tubo_abajo17.update(event)
                    tubo_abajo17.rect.x -= 15
                    screen.blit(tubo_abajo18.image, tubo_abajo18.rect)
                    tubo_abajo18.update(event)
                    tubo_abajo18.rect.x -= 15
                    screen.blit(tubo_abajo19.image, tubo_abajo19.rect)
                    tubo_abajo19.update(event)
                    tubo_abajo19.rect.x -= 15
                    screen.blit(tubo_abajo20.image, tubo_abajo20.rect)
                    tubo_abajo20.update(event)
                    tubo_abajo20.rect.x -= 15
                    screen.blit(tubo_arriba11.image, tubo_arriba11.rect)
                    tubo_arriba11.update(event)
                    tubo_arriba11.rect.x -= 15
                    screen.blit(tubo_arriba12.image, tubo_arriba12.rect)
                    tubo_arriba12.update(event)
                    tubo_arriba12.rect.x -= 15
                    screen.blit(tubo_arriba13.image, tubo_arriba13.rect)
                    tubo_arriba13.update(event)
                    tubo_arriba13.rect.x -= 15
                    screen.blit(tubo_arriba14.image, tubo_arriba14.rect)
                    tubo_arriba14.update(event)
                    tubo_arriba14.rect.x -= 15
                    screen.blit(tubo_arriba15.image, tubo_arriba15.rect)
                    tubo_arriba15.update(event)
                    tubo_arriba15.rect.x -= 15
                    screen.blit(tubo_arriba16.image, tubo_arriba16.rect)
                    tubo_arriba16.update(event)
                    tubo_arriba16.rect.x -= 15
                    screen.blit(tubo_arriba17.image, tubo_arriba17.rect)
                    tubo_arriba17.update(event)
                    tubo_arriba17.rect.x -= 15
                    screen.blit(tubo_arriba18.image, tubo_arriba18.rect)
                    tubo_arriba18.update(event)
                    tubo_arriba18.rect.x -= 15
                    screen.blit(tubo_arriba19.image, tubo_arriba19.rect)
                    tubo_arriba19.update(event)
                    tubo_arriba19.rect.x -= 15
                    screen.blit(tubo_arriba20.image, tubo_arriba20.rect)
                    tubo_arriba20.update(event)
                    tubo_arriba20.rect.x -= 15


                    if tubo_abajo11.rect.colliderect(Flappy2.rect):
                        VIDAS -= 1
                        screen.blit(BUM.image, Flappy2.rect)
                        Flappy2.rect.y = 250
                        Flappy2.rect.x = 300
                        pygame.mixer.Channel(2).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                        pygame.mixer.Channel(2).set_volume(.15)
                    if tubo_arriba11.rect.colliderect(Flappy2.rect):
                        VIDAS -= 1
                        screen.blit(BUM.image, Flappy2.rect)
                        Flappy2.rect.y = 250
                        Flappy2.rect.x = 300
                        pygame.mixer.Channel(2).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                        pygame.mixer.Channel(2).set_volume(.15)
                    if tubo_abajo12.rect.colliderect(Flappy2.rect):
                        VIDAS -= 1
                        screen.blit(BUM.image, Flappy2.rect)
                        Flappy2.rect.y = 300
                        Flappy2.rect.x = 300
                        pygame.mixer.Channel(2).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                        pygame.mixer.Channel(2).set_volume(.15)
                    if tubo_arriba12.rect.colliderect(Flappy2.rect):
                        VIDAS -= 1
                        screen.blit(BUM.image, Flappy2.rect)
                        Flappy2.rect.y = 300
                        Flappy2.rect.x = 300
                        pygame.mixer.Channel(2).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                        pygame.mixer.Channel(2).set_volume(.15)
                    if tubo_abajo13.rect.colliderect(Flappy2.rect):
                        VIDAS -= 1
                        screen.blit(BUM.image, Flappy2.rect)
                        Flappy2.rect.y = 200
                        Flappy2.rect.x = 300
                        pygame.mixer.Channel(2).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                        pygame.mixer.Channel(2).set_volume(.15)
                    if tubo_arriba13.rect.colliderect(Flappy2.rect):
                        VIDAS -= 1
                        screen.blit(BUM.image, Flappy2.rect)
                        Flappy2.rect.y = 200
                        Flappy2.rect.x = 300
                        pygame.mixer.Channel(2).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                        pygame.mixer.Channel(2).set_volume(.15)
                    if tubo_abajo14.rect.colliderect(Flappy2.rect):
                        VIDAS -= 1
                        screen.blit(BUM.image, Flappy2.rect)
                        Flappy2.rect.y = 300
                        Flappy2.rect.x = 300
                        pygame.mixer.Channel(2).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                        pygame.mixer.Channel(2).set_volume(.15)
                    if tubo_arriba14.rect.colliderect(Flappy2.rect):
                        VIDAS -= 1
                        screen.blit(BUM.image, Flappy2.rect)
                        Flappy2.rect.y = 300
                        Flappy2.rect.x = 300
                        pygame.mixer.Channel(2).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                        pygame.mixer.Channel(2).set_volume(.15)
                    if tubo_abajo15.rect.colliderect(Flappy2.rect):
                        VIDAS -= 1
                        screen.blit(BUM.image, Flappy2.rect)
                        Flappy2.rect.y = 250
                        Flappy2.rect.x = 300
                        pygame.mixer.Channel(2).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                        pygame.mixer.Channel(2).set_volume(.15)
                    if tubo_arriba15.rect.colliderect(Flappy2.rect):
                        VIDAS -= 1
                        screen.blit(BUM.image, Flappy2.rect)
                        Flappy2.rect.y = 250
                        Flappy2.rect.x = 300
                        pygame.mixer.Channel(2).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                        pygame.mixer.Channel(2).set_volume(.15)
                    if tubo_abajo16.rect.colliderect(Flappy2.rect):
                        VIDAS -= 1
                        screen.blit(BUM.image, Flappy2.rect)
                        Flappy2.rect.y = 300
                        Flappy2.rect.x = 300
                        pygame.mixer.Channel(2).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                        pygame.mixer.Channel(2).set_volume(.15)
                    if tubo_arriba16.rect.colliderect(Flappy2.rect):
                        VIDAS -= 1
                        screen.blit(BUM.image, Flappy2.rect)
                        Flappy2.rect.y = 300
                        Flappy2.rect.x = 300
                        pygame.mixer.Channel(2).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                        pygame.mixer.Channel(2).set_volume(.15)
                    if tubo_abajo17.rect.colliderect(Flappy2.rect):
                        VIDAS -= 1
                        screen.blit(BUM.image, Flappy2.rect)
                        Flappy2.rect.y = 200
                        Flappy2.rect.x = 300
                        pygame.mixer.Channel(2).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                        pygame.mixer.Channel(2).set_volume(.15)
                    if tubo_arriba17.rect.colliderect(Flappy2.rect):
                        VIDAS -= 1
                        screen.blit(BUM.image, Flappy2.rect)
                        Flappy2.rect.y = 200
                        Flappy2.rect.x = 300
                        pygame.mixer.Channel(2).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                        pygame.mixer.Channel(2).set_volume(.15)
                    if tubo_abajo18.rect.colliderect(Flappy2.rect):
                        VIDAS -= 1
                        screen.blit(BUM.image, Flappy2.rect)
                        Flappy2.rect.y = 300
                        Flappy2.rect.x = 300
                        pygame.mixer.Channel(2).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                        pygame.mixer.Channel(2).set_volume(.15)
                    if tubo_arriba18.rect.colliderect(Flappy2.rect):
                        VIDAS -= 1
                        screen.blit(BUM.image, Flappy2.rect)
                        Flappy2.rect.y = 300
                        Flappy2.rect.x = 300
                        pygame.mixer.Channel(2).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                        pygame.mixer.Channel(2).set_volume(.15)
                    if tubo_abajo19.rect.colliderect(Flappy2.rect):
                        VIDAS -= 1
                        screen.blit(BUM.image, Flappy2.rect)
                        Flappy2.rect.y = 200
                        Flappy2.rect.x = 300
                        pygame.mixer.Channel(2).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                        pygame.mixer.Channel(2).set_volume(.15)
                    if tubo_arriba19.rect.colliderect(Flappy2.rect):
                        VIDAS -= 1
                        screen.blit(BUM.image, Flappy2.rect)
                        Flappy2.rect.y = 200
                        Flappy2.rect.x = 300
                        pygame.mixer.Channel(2).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                        pygame.mixer.Channel(2).set_volume(.15)
                    if tubo_abajo20.rect.colliderect(Flappy2.rect):
                        VIDAS -= 1
                        screen.blit(BUM.image, Flappy2.rect)
                        Flappy2.rect.y = 250
                        Flappy2.rect.x = 300
                        pygame.mixer.Channel(2).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                        pygame.mixer.Channel(2).set_volume(.15)
                    if tubo_arriba20.rect.colliderect(Flappy2.rect):
                        VIDAS -= 1
                        screen.blit(BUM.image, Flappy2.rect)
                        Flappy2.rect.y = 250
                        Flappy2.rect.x = 300
                        pygame.mixer.Channel(2).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                        pygame.mixer.Channel(2).set_volume(.15)



                    Flappy2.rect.x -= 5
                    if Flappy2.rect.x <= 140:
                        Flappy2.rect.x = 140

                if transicionador_tubos_boss_2 == True:
                    RELOJ_TRAN_TUBOS_BOSS_NVL2.rect.x += 1
                    if RELOJ_TRAN_TUBOS_BOSS_NVL2.rect.x == 465:
                        activar_tubos2 = False
                    if RELOJ_TRAN_TUBOS_BOSS_NVL2.rect.x == 400:
                        JEFE2_TOTAL = True

                RELOJ4.rect.x += 1
                if RELOJ4.rect.x >= 515:
                    x_relativa3 = x3 % bg_espacial2.get_rect().width
                    screen.blit(bg_espacial2,[x_relativa3 - bg_espacial2.get_rect().width ,0])
                    if x_relativa3 < pantalla_x:
                        screen.blit(bg_espacial2,(x_relativa3,0))
                    x3 -= 30
                    screen.blit(Flappy2.image, Flappy2.rect)
                    screen.blit(BOSS1.image, BOSS1.rect)
                    if RELOJ4.rect.x >= 1065:
                        x3 -= 10
                        mov_flap_der = True
                        if mov_flap_der == True:
                            Flappy2.rect.x += 12
                    if RELOJ4.rect.x >= 1075:
                        x3 -= 10
                    if RELOJ4.rect.x >= 1085:
                        x3 -= 10
                    if RELOJ4.rect.x >= 1095:
                        x3 -= 10
                    if RELOJ4.rect.x >= 1105:
                        x3 -= 10
                    if RELOJ4.rect.x >= 1115:
                        x3 -= 10
                    if RELOJ4.rect.x >= 1165:
                        NIVEL = 3
                        mov_flap_der = False
                        pygame.mixer.Channel(39).play(pygame.mixer.Sound("MUSICA/LIVE_UP2.wav"))
                        pygame.mixer.Channel(39).set_volume(.02)

                if JEFE2_TOTAL == True:

                    screen.blit(BOSS2.image, BOSS2.rect)
                    FBS2 = True

                    if act_mover_izq2 == True:

                        if BOSS2.rect.y == 234:
                            mover_izq2 = True
                            if mover_izq2 == True:
                                BOSS2.rect.x -= 1
                        if BOSS2.rect.x <= 1200:
                            mover_izq2 = False
                            BOSS2.rect.x = 1200
                            act_oscilar_boss2 = True


                    if act_oscilar_boss2 == True:

                        PRIMERA_FB2 = True

                        if BOSS2.rect.x == 1200:

                            act_mover_izq2 = False
                            if BOSS2.rect.y <= 0:
                                BOSS2.rect.y = 0
                                oscilar_boss2 = False
                            if BOSS2.rect.y >= 470:
                                BOSS2.rect.y = 470
                                oscilar_boss2 = True
                            if oscilar_boss2 == False:
                                BOSS2.rect.y += 6
                            elif oscilar_boss2 == True:
                                BOSS2.rect.y -= 6

                    if FBS2 == True:

                        if PRIMERA_FB2 == True:
                            if BOSS2.rect.y == 0:
                                ver_bola_fuego1_2 = True
                            if ver_bola_fuego1_2 == True:
                                if BOSS2.rect.y == 0 and BOSS2.rect.x == 1200:
                                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("MUSICA/SONIDO_ROCA.wav"))
                                    pygame.mixer.Channel(1).set_volume(.25)
                                screen.blit(bola_fuego1_2.image, bola_fuego1_2.rect)
                                mover_bola_fuego1_2 = True
                                SEGUNDA_FB2 = True
                                if mover_bola_fuego1_2 == True:
                                    bola_fuego1_2.rect.x -= 25
                                    if bola_fuego1_2.rect.colliderect(Flappy2.rect):
                                        VIDAS -= 1
                                        ver_bola_fuego1_2 = False
                                        screen.blit(BUM1_2.image, Flappy2.rect)
                                        pygame.mixer.Channel(2).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                                        pygame.mixer.Channel(2).set_volume(.15)

                        if SEGUNDA_FB2 == True:
                            RELOJ_2.rect.x -= 1
                            if RELOJ_2.rect.x == 1255:
                                ver_bola_fuego2_2 = True
                            if ver_bola_fuego2_2 == True:
                                if MUSICA_FB_2_2 == True:
                                    pygame.mixer.Channel(3).play(pygame.mixer.Sound("MUSICA/SONIDO_ROCA.wav"))
                                    pygame.mixer.Channel(3).set_volume(.25)
                                screen.blit(bola_fuego2_2.image, bola_fuego2_2.rect)
                                mover_bola_fuego2_2 = True
                                TERCERA_FB2 = True
                                if mover_bola_fuego2_2 == True:
                                    MUSICA_FB_2_2 = False
                                    bola_fuego2_2.rect.x -= 25
                                    if bola_fuego2_2.rect.colliderect(Flappy2.rect):
                                        VIDAS -= 1
                                        ver_bola_fuego2_2 = False
                                        screen.blit(BUM2_2.image, Flappy2.rect)
                                        pygame.mixer.Channel(4).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                                        pygame.mixer.Channel(4).set_volume(.15)


                        if TERCERA_FB2 == True:
                            if RELOJ_2.rect.x == 1230:
                                ver_bola_fuego3_2 = True
                            if ver_bola_fuego3_2 == True:
                                if MUSICA_FB_3_2 == True:
                                    pygame.mixer.Channel(5).play(pygame.mixer.Sound("MUSICA/SONIDO_ROCA.wav"))
                                    pygame.mixer.Channel(5).set_volume(.25)
                                screen.blit(bola_fuego3_2.image, bola_fuego3_2.rect)
                                mover_bola_fuego3_2 = True
                                CUARTA_FB2 = True
                                if mover_bola_fuego3_2 == True:
                                    MUSICA_FB_3_2 = False
                                    bola_fuego3_2.rect.x -= 25
                                    if bola_fuego3_2.rect.colliderect(Flappy2.rect):
                                        VIDAS -= 1
                                        ver_bola_fuego3_2 = False
                                        screen.blit(BUM3_2.image, Flappy2.rect)
                                        pygame.mixer.Channel(6).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                                        pygame.mixer.Channel(6).set_volume(.15)

                        if CUARTA_FB2 == True:
                            if RELOJ_2.rect.x == 1210:
                                ver_bola_fuego4_2 = True
                            if ver_bola_fuego4_2 == True:
                                if MUSICA_FB_4_2 == True:
                                    pygame.mixer.Channel(7).play(pygame.mixer.Sound("MUSICA/SONIDO_ROCA.wav"))
                                    pygame.mixer.Channel(7).set_volume(.25)
                                screen.blit(bola_fuego4_2.image, bola_fuego4_2.rect)
                                mover_bola_fuego4_2 = True
                                QUINTA_FB2 = True
                                if mover_bola_fuego4_2 == True:
                                    MUSICA_FB_4_2 = False
                                    bola_fuego4_2.rect.x -= 25
                                    if bola_fuego4_2.rect.colliderect(Flappy2.rect):
                                        VIDAS -= 1
                                        ver_bola_fuego4_2 = False
                                        screen.blit(BUM4_2.image, Flappy2.rect)
                                        pygame.mixer.Channel(8).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                                        pygame.mixer.Channel(8).set_volume(.15)

                        if QUINTA_FB2 == True:
                            if RELOJ_2.rect.x == 1170:
                                ver_bola_fuego5_2 = True
                            if ver_bola_fuego5_2 == True:
                                if MUSICA_FB_5_2 == True:
                                    pygame.mixer.Channel(9).play(pygame.mixer.Sound("MUSICA/SONIDO_ROCA.wav"))
                                    pygame.mixer.Channel(9).set_volume(.25)
                                screen.blit(bola_fuego5_2.image, bola_fuego5_2.rect)
                                mover_bola_fuego5_2 = True
                                SEXTA_FB2 = True
                                if mover_bola_fuego5_2 == True:
                                    MUSICA_FB_5_2 = False
                                    bola_fuego5_2.rect.x -= 25
                                    if bola_fuego5_2.rect.colliderect(Flappy2.rect):
                                        VIDAS -= 1
                                        ver_bola_fuego5_2 = False
                                        screen.blit(BUM5_2.image, Flappy2.rect)
                                        pygame.mixer.Channel(10).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                                        pygame.mixer.Channel(10).set_volume(.15)

                        if SEXTA_FB2 == True:
                            if RELOJ_2.rect.x == 1150:
                                ver_bola_fuego6_2 = True
                            if ver_bola_fuego6_2 == True:
                                if MUSICA_FB_6_2 == True:
                                    pygame.mixer.Channel(11).play(pygame.mixer.Sound("MUSICA/SONIDO_ROCA.wav"))
                                    pygame.mixer.Channel(11).set_volume(.25)
                                screen.blit(bola_fuego6_2.image, bola_fuego6_2.rect)
                                mover_bola_fuego6_2 = True
                                SEPTIMA_FB2 = True
                                if mover_bola_fuego6_2 == True:
                                    MUSICA_FB_6_2 = False
                                    bola_fuego6_2.rect.x -= 25
                                    if bola_fuego6_2.rect.colliderect(Flappy2.rect):
                                        VIDAS -= 1
                                        ver_bola_fuego6_2 = False
                                        screen.blit(BUM6_2.image, Flappy2.rect)
                                        pygame.mixer.Channel(12).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                                        pygame.mixer.Channel(12).set_volume(.15)

                        if SEPTIMA_FB2 == True:
                            if RELOJ_2.rect.x == 1130:
                                ver_bola_fuego7_2 = True
                            if ver_bola_fuego7_2 == True:
                                if MUSICA_FB_7_2 == True:
                                    pygame.mixer.Channel(13).play(pygame.mixer.Sound("MUSICA/SONIDO_ROCA.wav"))
                                    pygame.mixer.Channel(13).set_volume(.25)
                                screen.blit(bola_fuego7_2.image, bola_fuego7_2.rect)
                                mover_bola_fuego7_2 = True
                                OCTAVA_FB2 = True
                                if mover_bola_fuego7_2 == True:
                                    MUSICA_FB_7_2 = False
                                    bola_fuego7_2.rect.x -= 25
                                    if bola_fuego7_2.rect.colliderect(Flappy2.rect):
                                        VIDAS -= 1
                                        ver_bola_fuego7_2 = False
                                        screen.blit(BUM7_2.image, Flappy2.rect)
                                        pygame.mixer.Channel(14).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                                        pygame.mixer.Channel(14).set_volume(.15)

                        if OCTAVA_FB2 == True:
                            if RELOJ_2.rect.x == 1100:
                                ver_bola_fuego8_2 = True
                            if ver_bola_fuego8_2 == True:
                                if MUSICA_FB_8_2 == True:
                                    pygame.mixer.Channel(15).play(pygame.mixer.Sound("MUSICA/SONIDO_ROCA.wav"))
                                    pygame.mixer.Channel(15).set_volume(.25)
                                screen.blit(bola_fuego8_2.image, bola_fuego8_2.rect)
                                mover_bola_fuego8_2 = True
                                NOVENA_FB2 = True
                                if mover_bola_fuego8_2 == True:
                                    MUSICA_FB_8_2 = False
                                    bola_fuego8_2.rect.x -= 25
                                    if bola_fuego8_2.rect.colliderect(Flappy2.rect):
                                        VIDAS -= 1
                                        ver_bola_fuego8_2 = False
                                        screen.blit(BUM8_2.image, Flappy2.rect)
                                        pygame.mixer.Channel(16).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                                        pygame.mixer.Channel(16).set_volume(.15)

                        if NOVENA_FB2 == True:
                            if RELOJ_2.rect.x == 1080:
                                ver_bola_fuego9_2 = True
                            if ver_bola_fuego9_2 == True:
                                if MUSICA_FB_9_2 == True:
                                    pygame.mixer.Channel(17).play(pygame.mixer.Sound("MUSICA/SONIDO_ROCA.wav"))
                                    pygame.mixer.Channel(17).set_volume(.25)
                                screen.blit(bola_fuego9_2.image, bola_fuego9_2.rect)
                                mover_bola_fuego9_2 = True
                                DECIMA_FB2 = True
                                if mover_bola_fuego9_2 == True:
                                    MUSICA_FB_9_2 = False
                                    bola_fuego9_2.rect.x -= 25
                                    if bola_fuego9_2.rect.colliderect(Flappy2.rect):
                                        VIDAS -= 1
                                        ver_bola_fuego9_2 = False
                                        screen.blit(BUM9_2.image, Flappy2.rect)
                                        pygame.mixer.Channel(18).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                                        pygame.mixer.Channel(18).set_volume(.15)

                        if DECIMA_FB2 == True:
                            if RELOJ_2.rect.x == 1060:
                                ver_bola_fuego10_2 = True
                            if ver_bola_fuego10_2 == True:
                                if MUSICA_FB_10_2 == True:
                                    pygame.mixer.Channel(19).play(pygame.mixer.Sound("MUSICA/SONIDO_ROCA.wav"))
                                    pygame.mixer.Channel(19).set_volume(.25)
                                screen.blit(bola_fuego10_2.image, bola_fuego10_2.rect)
                                mover_bola_fuego10_2 = True
                                ONCEAVA_FB2 = True
                                if mover_bola_fuego10_2 == True:
                                    MUSICA_FB_10_2 = False
                                    bola_fuego10_2.rect.x -= 25
                                    if bola_fuego10_2.rect.colliderect(Flappy2.rect):
                                        VIDAS -= 1
                                        ver_bola_fuego10_2 = False
                                        screen.blit(BUM10_2.image, Flappy2.rect)
                                        pygame.mixer.Channel(20).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                                        pygame.mixer.Channel(20).set_volume(.15)

                        if ONCEAVA_FB2 == True:
                            if RELOJ_2.rect.x == 1010:
                                ver_bola_fuego11_2 = True
                            if ver_bola_fuego11_2 == True:
                                if MUSICA_FB_11_2 == True:
                                    pygame.mixer.Channel(21).play(pygame.mixer.Sound("MUSICA/SONIDO_ROCA.wav"))
                                    pygame.mixer.Channel(21).set_volume(.25)
                                screen.blit(bola_fuego11_2.image, bola_fuego11_2.rect)
                                mover_bola_fuego11_2 = True
                                DOCEAVA_FB2 = True
                                if mover_bola_fuego11_2 == True:
                                    MUSICA_FB_11_2 = False
                                    bola_fuego11_2.rect.x -= 25
                                    if bola_fuego11_2.rect.colliderect(Flappy2.rect):
                                        VIDAS -= 1
                                        ver_bola_fuego11_2 = False
                                        screen.blit(BUM11_2.image, Flappy2.rect)
                                        pygame.mixer.Channel(22).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                                        pygame.mixer.Channel(22).set_volume(.15)

                        if DOCEAVA_FB2 == True:
                            if RELOJ_2.rect.x == 990:
                                ver_bola_fuego12_2 = True
                            if ver_bola_fuego12_2 == True:
                                if MUSICA_FB_12_2 == True:
                                    pygame.mixer.Channel(23).play(pygame.mixer.Sound("MUSICA/SONIDO_ROCA.wav"))
                                    pygame.mixer.Channel(23).set_volume(.25)
                                screen.blit(bola_fuego12_2.image, bola_fuego12_2.rect)
                                mover_bola_fuego12_2 = True
                                TRECEAVA_FB2 = True
                                if mover_bola_fuego12_2 == True:
                                    MUSICA_FB_12_2 = False
                                    bola_fuego12_2.rect.x -= 25
                                    if bola_fuego12_2.rect.colliderect(Flappy2.rect):
                                        VIDAS -= 1
                                        ver_bola_fuego12_2 = False
                                        screen.blit(BUM12_2.image, Flappy2.rect)
                                        pygame.mixer.Channel(24).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                                        pygame.mixer.Channel(24).set_volume(.15)

                        if TRECEAVA_FB2 == True:
                            if RELOJ_2.rect.x == 970:
                                ver_bola_fuego13_2 = True
                            if ver_bola_fuego13_2 == True:
                                if MUSICA_FB_13_2 == True:
                                    pygame.mixer.Channel(25).play(pygame.mixer.Sound("MUSICA/SONIDO_ROCA.wav"))
                                    pygame.mixer.Channel(25).set_volume(.25)
                                screen.blit(bola_fuego13_2.image, bola_fuego13_2.rect)
                                mover_bola_fuego13_2 = True
                                STOP_BOSS3 = True
                                if mover_bola_fuego13_2 == True:
                                    MUSICA_FB_13_2 = False
                                    bola_fuego13_2.rect.x -= 25
                                    if bola_fuego13_2.rect.colliderect(Flappy2.rect):
                                        VIDAS -= 1
                                        ver_bola_fuego13_2 = False
                                        screen.blit(BUM13_2.image, Flappy2.rect)
                                        pygame.mixer.Channel(26).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                                        pygame.mixer.Channel(26).set_volume(.15)

                        if STOP_BOSS3 == True:

                            if FB_GRANDE1_2 == True:

                                if ACT_MOV_BOSS_2 == True:
                                    if BOSS2.rect.y >= 235:
                                        BOSS2.rect.y = 235
                                        RELOJ_2.rect.y += 1
                                if RELOJ_2.rect.y == 240:
                                    ver_bola_fuego14_2 = True
                                if ver_bola_fuego14_2 == True:
                                    if MUSICA_FB_14_2 == True:
                                        pygame.mixer.Channel(27).play(pygame.mixer.Sound("MUSICA/SONIDO_ROCA.wav"))
                                        pygame.mixer.Channel(27).set_volume(.25)
                                    screen.blit(bola_fuego14_2.image, bola_fuego14_2.rect)
                                    mover_bola_fuego14_2 = True
                                    FB_GRANDE2_2 = True
                                    if mover_bola_fuego14_2 == True:
                                        MUSICA_FB_14_2 = False
                                        bola_fuego14_2.rect.x -= 25
                                        act_oscilar_boss2 = False
                                        if ACT_MOV_FB_2 == True:
                                            BOSS2.rect.y -= 12
                                        if bola_fuego14_2.rect.colliderect(Flappy2.rect):
                                            VIDAS -= 1
                                            ver_bola_fuego14_2 = False
                                            screen.blit(BUM14_2.image, Flappy2.rect)
                                            pygame.mixer.Channel(28).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                                            pygame.mixer.Channel(28).set_volume(.15)

                            if FB_GRANDE2_2 == True:
                                RELOJ_2.rect.y += 1
                                if RELOJ_2.rect.y == 260:
                                    ver_bola_fuego15_2 = True
                                if ver_bola_fuego15_2 == True:
                                    if MUSICA_FB_15_2 == True:
                                        pygame.mixer.Channel(29).play(pygame.mixer.Sound("MUSICA/SONIDO_ROCA.wav"))
                                        pygame.mixer.Channel(29).set_volume(.25)
                                    screen.blit(bola_fuego15_2.image, bola_fuego15_2.rect)
                                    mover_bola_fuego15_2 = True
                                    if BOSS2.rect.y <= 0:
                                        BOSS2.rect.y = 0
                                    FB_GRANDE3_2 = True
                                    if mover_bola_fuego15_2 == True:
                                        MUSICA_FB_15_2 = False
                                        bola_fuego15_2.rect.x -= 25
                                        if bola_fuego15_2.rect.colliderect(Flappy2.rect):
                                            VIDAS -= 1
                                            ver_bola_fuego15_2 = False
                                            screen.blit(BUM15_2.image, Flappy2.rect)
                                            pygame.mixer.Channel(30).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                                            pygame.mixer.Channel(30).set_volume(.15)

                            if FB_GRANDE3_2 == True:
                                ACT_MOV_FB_2 = False
                                ACT_MOV_BOSS_2 = False
                                if MOV_BOSS_2 == True:
                                    BOSS2.rect.y += 20
                                if RELOJ_2.rect.y == 280:
                                    ver_bola_fuego16_2 = True
                                if ver_bola_fuego16_2 == True:
                                    if MUSICA_FB_16_2 == True:
                                        pygame.mixer.Channel(31).play(pygame.mixer.Sound("MUSICA/SONIDO_ROCA.wav"))
                                        pygame.mixer.Channel(31).set_volume(.25)
                                    screen.blit(bola_fuego16_2.image, bola_fuego16_2.rect)
                                    mover_bola_fuego16_2 = True
                                    if mover_bola_fuego16_2 == True:
                                        MUSICA_FB_16_2 = False
                                        bola_fuego16_2.rect.x -= 25
                                        if bola_fuego16_2.rect.colliderect(Flappy2.rect):
                                            VIDAS -= 1
                                            ver_bola_fuego16_2 = False
                                            screen.blit(BUM16_2.image, Flappy2.rect)
                                            pygame.mixer.Channel(32).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                                            pygame.mixer.Channel(32).set_volume(.15)


                            if BOSS2.rect.y >= 470:
                                BOSS2.rect.y = 470
                                FB_GRANDE4_2 = True

                            if FB_GRANDE4_2 == True:

                                MOV_BOSS_2 = False
                                if DESACTIVAR_2 == True:
                                    BOSS2.rect.y -= 10
                                RELOJ2_2.rect.x += 1

                                if RELOJ2_2.rect.x == 28:
                                    ver_bola_fuego17_2 = True
                                if ver_bola_fuego17_2 == True:
                                    if MUSICA_FB_17_2 == True:
                                        pygame.mixer.Channel(33).play(pygame.mixer.Sound("MUSICA/SONIDO_ROCA.wav"))
                                        pygame.mixer.Channel(33).set_volume(.25)
                                    screen.blit(bola_fuego17_2.image, bola_fuego17_2.rect)
                                    mover_bola_fuego17_2 = True
                                    FB_GRANDE5_2 = True
                                    if mover_bola_fuego17_2 == True:
                                        MUSICA_FB_17_2 = False
                                        bola_fuego17_2.rect.x -= 25
                                        act_oscilar_boss2 = False
                                        if bola_fuego17_2.rect.colliderect(Flappy2.rect):
                                            VIDAS -= 1
                                            ver_bola_fuego17_2 = False
                                            screen.blit(BUM17_2.image, Flappy2.rect)
                                            pygame.mixer.Channel(34).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                                            pygame.mixer.Channel(34).set_volume(.15)

                            if FB_GRANDE5_2 == True:
                                if BOSS2.rect.y <= 10:
                                    DESACTIVAR_2 = False
                                    BOSS2.rect.y = 10
                                    if DESACTIVAR2_2 == True:
                                        BOSS2.rect.y -= 5
                                    if RELOJ2_2.rect.x == 50:
                                        ver_bola_fuego18_2 = True
                                if ver_bola_fuego18_2 == True:
                                    if MUSICA_FB_18_2 == True:
                                        pygame.mixer.Channel(35).play(pygame.mixer.Sound("MUSICA/SONIDO_ROCA.wav"))
                                        pygame.mixer.Channel(35).set_volume(.25)
                                    screen.blit(bola_fuego18_2.image, bola_fuego18_2.rect)
                                    mover_bola_fuego18_2 = True
                                    FB_GRANDE6_2 = True
                                    if mover_bola_fuego18_2 == True:
                                        MUSICA_FB_18_2 = False
                                        bola_fuego18_2.rect.x -= 25
                                        act_oscilar_boss2 = False
                                        if bola_fuego18_2.rect.colliderect(Flappy2.rect):
                                            VIDAS -= 1
                                            ver_bola_fuego18_2 = False
                                            screen.blit(BUM18_2.image, Flappy2.rect)
                                            pygame.mixer.Channel(36).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                                            pygame.mixer.Channel(36).set_volume(.15)

                            if FB_GRANDE6_2 == True:
                                if DESACTIVAR3_2 == True:
                                    BOSS2.rect.y += 15
                                if BOSS2.rect.y >= 470:
                                    BOSS2.rect.y = 470
                                    DESACTIVAR3_2 = False
                                if RELOJ2_2.rect.x == 73:
                                    ver_bola_fuego19_2 = True
                                if ver_bola_fuego19_2 == True:
                                    if MUSICA_FB_19_2 == True:
                                        pygame.mixer.Channel(37).play(pygame.mixer.Sound("MUSICA/SONIDO_ROCA.wav"))
                                        pygame.mixer.Channel(37).set_volume(.25)
                                    screen.blit(bola_fuego19_2.image, bola_fuego19_2.rect)
                                    mover_bola_fuego19_2 = True
                                    if mover_bola_fuego19_2 == True:
                                        MUSICA_FB_19_2 = False
                                        bola_fuego19_2.rect.x -= 25
                                        BOSS2.rect.x += 3
                                        if bola_fuego19_2.rect.colliderect(Flappy2.rect):
                                            VIDAS -= 1
                                            ver_bola_fuego19_2 = False
                                            screen.blit(BUM19_2.image, Flappy2.rect)
                                            pygame.mixer.Channel(38).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                                            pygame.mixer.Channel(38).set_volume(.15)


                                    if BOSS2.rect.y <= 235:
                                        BOSS2.rect.y = 235
                                        if BOSS2.rect.y == 235:
                                            BOSS2.rect.x += 5
                                        RELOJ2_2.rect.x += 1
                                        if RELOJ2_2.rect.x == 250:
                                            FBS2 = False





            if NIVEL == 3:
                screen.blit(bg_3,[0,0])
                if mov_flap_izq2 == True:
                    Flappy3.rect.x  = 140
                screen.blit(Flappy3.image, Flappy3.rect)
                Flappy3.Movimiento_Pajaro(event)

                if activar_tubos3 == True:

                    mov_flap_izq2 = False

                    screen.blit(tubo_abajo21.image, tubo_abajo21.rect)
                    tubo_abajo21.update(event)
                    tubo_abajo21.rect.x -= 20
                    screen.blit(tubo_abajo22.image, tubo_abajo22.rect)
                    tubo_abajo22.update(event)
                    tubo_abajo22.rect.x -= 20
                    screen.blit(tubo_abajo23.image, tubo_abajo23.rect)
                    tubo_abajo23.update(event)
                    tubo_abajo23.rect.x -= 20
                    screen.blit(tubo_abajo24.image, tubo_abajo24.rect)
                    tubo_abajo24.update(event)
                    tubo_abajo24.rect.x -= 20
                    screen.blit(tubo_abajo25.image, tubo_abajo25.rect)
                    tubo_abajo25.update(event)
                    tubo_abajo25.rect.x -= 20
                    screen.blit(tubo_abajo26.image, tubo_abajo26.rect)
                    tubo_abajo26.update(event)
                    tubo_abajo26.rect.x -= 20
                    screen.blit(tubo_abajo27.image, tubo_abajo27.rect)
                    tubo_abajo27.update(event)
                    tubo_abajo27.rect.x -= 20
                    screen.blit(tubo_abajo28.image, tubo_abajo28.rect)
                    tubo_abajo28.update(event)
                    tubo_abajo28.rect.x -= 20
                    screen.blit(tubo_abajo29.image, tubo_abajo29.rect)
                    tubo_abajo29.update(event)
                    tubo_abajo29.rect.x -= 20
                    screen.blit(tubo_abajo30.image, tubo_abajo30.rect)
                    tubo_abajo30.update(event)
                    tubo_abajo30.rect.x -= 20
                    screen.blit(tubo_arriba21.image, tubo_arriba21.rect)
                    tubo_arriba21.update(event)
                    tubo_arriba21.rect.x -= 20
                    screen.blit(tubo_arriba22.image, tubo_arriba22.rect)
                    tubo_arriba22.update(event)
                    tubo_arriba22.rect.x -= 20
                    screen.blit(tubo_arriba23.image, tubo_arriba23.rect)
                    tubo_arriba23.update(event)
                    tubo_arriba23.rect.x -= 20
                    screen.blit(tubo_arriba24.image, tubo_arriba24.rect)
                    tubo_arriba24.update(event)
                    tubo_arriba24.rect.x -= 20
                    screen.blit(tubo_arriba25.image, tubo_arriba25.rect)
                    tubo_arriba25.update(event)
                    tubo_arriba25.rect.x -= 20
                    screen.blit(tubo_arriba26.image, tubo_arriba26.rect)
                    tubo_arriba26.update(event)
                    tubo_arriba26.rect.x -= 20
                    screen.blit(tubo_arriba27.image, tubo_arriba27.rect)
                    tubo_arriba27.update(event)
                    tubo_arriba27.rect.x -= 20
                    screen.blit(tubo_arriba28.image, tubo_arriba28.rect)
                    tubo_arriba28.update(event)
                    tubo_arriba28.rect.x -= 20
                    screen.blit(tubo_arriba29.image, tubo_arriba29.rect)
                    tubo_arriba29.update(event)
                    tubo_arriba29.rect.x -= 20
                    screen.blit(tubo_arriba30.image, tubo_arriba30.rect)
                    tubo_arriba30.update(event)
                    tubo_arriba30.rect.x -= 20


                    if tubo_abajo21.rect.colliderect(Flappy3.rect):
                        VIDAS -= 1
                        screen.blit(BUM1_3.image,Flappy3.rect)
                        Flappy3.rect.y = 250
                        Flappy3.rect.x = 300
                        pygame.mixer.Channel(2).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                        pygame.mixer.Channel(2).set_volume(.15)
                    if tubo_arriba21.rect.colliderect(Flappy3.rect):
                        VIDAS -= 1
                        screen.blit(BUM1_3.image,Flappy3.rect)
                        Flappy3.rect.y = 250
                        Flappy3.rect.x = 300
                        pygame.mixer.Channel(2).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                        pygame.mixer.Channel(2).set_volume(.15)
                    if tubo_abajo22.rect.colliderect(Flappy3.rect):
                        VIDAS -= 1
                        screen.blit(BUM1_3.image,Flappy3.rect)
                        Flappy3.rect.y = 300
                        Flappy3.rect.x = 300
                        pygame.mixer.Channel(2).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                        pygame.mixer.Channel(2).set_volume(.15)
                    if tubo_arriba22.rect.colliderect(Flappy3.rect):
                        VIDAS -= 1
                        screen.blit(BUM1_3.image,Flappy3.rect)
                        Flappy3.rect.y = 300
                        Flappy3.rect.x = 300
                        pygame.mixer.Channel(2).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                        pygame.mixer.Channel(2).set_volume(.15)
                    if tubo_abajo23.rect.colliderect(Flappy3.rect):
                        VIDAS -= 1
                        screen.blit(BUM1_3.image,Flappy3.rect)
                        Flappy3.rect.y = 200
                        Flappy3.rect.x = 300
                        pygame.mixer.Channel(2).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                        pygame.mixer.Channel(2).set_volume(.15)
                    if tubo_arriba23.rect.colliderect(Flappy3.rect):
                        VIDAS -= 1
                        screen.blit(BUM1_3.image,Flappy3.rect)
                        Flappy3.rect.y = 200
                        Flappy3.rect.x = 300
                        pygame.mixer.Channel(2).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                        pygame.mixer.Channel(2).set_volume(.15)
                    if tubo_abajo24.rect.colliderect(Flappy3.rect):
                        VIDAS -= 1
                        screen.blit(BUM1_3.image,Flappy3.rect)
                        Flappy3.rect.y = 300
                        Flappy3.rect.x = 300
                        pygame.mixer.Channel(2).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                        pygame.mixer.Channel(2).set_volume(.15)
                    if tubo_arriba24.rect.colliderect(Flappy3.rect):
                        VIDAS -= 1
                        screen.blit(BUM1_3.image,Flappy3.rect)
                        Flappy3.rect.y = 300
                        Flappy3.rect.x = 300
                        pygame.mixer.Channel(2).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                        pygame.mixer.Channel(2).set_volume(.15)
                    if tubo_abajo25.rect.colliderect(Flappy3.rect):
                        VIDAS -= 1
                        screen.blit(BUM1_3.image,Flappy3.rect)
                        Flappy3.rect.y = 250
                        Flappy3.rect.x = 300
                        pygame.mixer.Channel(2).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                        pygame.mixer.Channel(2).set_volume(.15)
                    if tubo_arriba25.rect.colliderect(Flappy3.rect):
                        VIDAS -= 1
                        screen.blit(BUM1_3.image,Flappy3.rect)
                        Flappy3.rect.y = 250
                        Flappy3.rect.x = 300
                        pygame.mixer.Channel(2).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                        pygame.mixer.Channel(2).set_volume(.15)
                    if tubo_abajo26.rect.colliderect(Flappy3.rect):
                        VIDAS -= 1
                        screen.blit(BUM1_3.image,Flappy3.rect)
                        Flappy3.rect.y = 300
                        Flappy3.rect.x = 300
                        pygame.mixer.Channel(2).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                        pygame.mixer.Channel(2).set_volume(.15)
                    if tubo_arriba26.rect.colliderect(Flappy3.rect):
                        VIDAS -= 1
                        screen.blit(BUM1_3.image,Flappy3.rect)
                        Flappy3.rect.y = 300
                        Flappy3.rect.x = 300
                        pygame.mixer.Channel(2).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                        pygame.mixer.Channel(2).set_volume(.15)
                    if tubo_abajo27.rect.colliderect(Flappy3.rect):
                        VIDAS -= 1
                        screen.blit(BUM1_3.image,Flappy3.rect)
                        Flappy3.rect.y = 200
                        Flappy3.rect.x = 300
                        pygame.mixer.Channel(2).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                        pygame.mixer.Channel(2).set_volume(.15)
                    if tubo_arriba27.rect.colliderect(Flappy3.rect):
                        VIDAS -= 1
                        screen.blit(BUM1_3.image,Flappy3.rect)
                        Flappy3.rect.y = 200
                        Flappy3.rect.x = 300
                        pygame.mixer.Channel(2).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                        pygame.mixer.Channel(2).set_volume(.15)
                    if tubo_abajo28.rect.colliderect(Flappy3.rect):
                        VIDAS -= 1
                        screen.blit(BUM1_3.image,Flappy3.rect)
                        Flappy3.rect.y = 300
                        Flappy3.rect.x = 300
                        pygame.mixer.Channel(2).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                        pygame.mixer.Channel(2).set_volume(.15)
                    if tubo_arriba28.rect.colliderect(Flappy3.rect):
                        VIDAS -= 1
                        screen.blit(BUM1_3.image,Flappy3.rect)
                        Flappy3.rect.y = 300
                        Flappy3.rect.x = 300
                        pygame.mixer.Channel(2).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                        pygame.mixer.Channel(2).set_volume(.15)
                    if tubo_abajo29.rect.colliderect(Flappy3.rect):
                        VIDAS -= 1
                        screen.blit(BUM1_3.image,Flappy3.rect)
                        Flappy3.rect.y = 200
                        Flappy3.rect.x = 300
                        pygame.mixer.Channel(2).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                        pygame.mixer.Channel(2).set_volume(.15)
                    if tubo_arriba29.rect.colliderect(Flappy3.rect):
                        VIDAS -= 1
                        screen.blit(BUM1_3.image,Flappy3.rect)
                        Flappy3.rect.y = 200
                        Flappy3.rect.x = 300
                        pygame.mixer.Channel(2).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                        pygame.mixer.Channel(2).set_volume(.15)
                    if tubo_abajo30.rect.colliderect(Flappy3.rect):
                        VIDAS -= 1
                        screen.blit(BUM1_3.image,Flappy3.rect)
                        Flappy3.rect.y = 250
                        Flappy3.rect.x = 300
                        pygame.mixer.Channel(2).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                        pygame.mixer.Channel(2).set_volume(.15)
                    if tubo_arriba30.rect.colliderect(Flappy3.rect):
                        VIDAS -= 1
                        screen.blit(BUM1_3.image,Flappy3.rect)
                        Flappy3.rect.y = 250
                        Flappy3.rect.x = 300
                        pygame.mixer.Channel(2).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                        pygame.mixer.Channel(2).set_volume(.15)



                    Flappy3.rect.x -= 8
                    if Flappy3.rect.x <= 140:
                        Flappy3.rect.x = 140

                if transicionador_tubos_boss_3 == True:
                    RELOJ_TRAN_TUBOS_BOSS_NVL3.rect.x += 1
                    if RELOJ_TRAN_TUBOS_BOSS_NVL3.rect.x == 465:
                        activar_tubos3 = False
                    if RELOJ_TRAN_TUBOS_BOSS_NVL3.rect.x == 270:
                        JEFE3_TOTAL = True

                RELOJ5.rect.x += 1
                if RELOJ5.rect.x >= 372:
                    x_relativa4 = x4 % bg_espacial3.get_rect().width
                    screen.blit(bg_espacial3,[x_relativa4 - bg_espacial3.get_rect().width ,0])
                    if x_relativa4 < pantalla_x:
                        screen.blit(bg_espacial3,(x_relativa4,0))
                    x4 -= 30
                    screen.blit(Flappy3.image, Flappy3.rect)
                    screen.blit(BOSS3.image, BOSS3.rect)
                    if RELOJ5.rect.x >= 925:
                        mov_flap_der = True
                        if mov_flap_der == True:
                            Flappy3.rect.x += 14
                    if RELOJ5.rect.x >= 930:
                        x4 -= 10
                    if RELOJ5.rect.x >= 940:
                        x4 -= 10
                    if RELOJ5.rect.x >= 950:
                        x4 -= 10
                    if RELOJ5.rect.x >= 960:
                        x4 -= 10
                    if RELOJ5.rect.x >= 970:
                        x4 -= 10
                    if RELOJ5.rect.x >= 980:
                        x4 -= 10
                    if RELOJ5.rect.x >= 1010:
                        NIVEL = 4
                        mov_flap_der = False
                        pygame.mixer.Channel(39).play(pygame.mixer.Sound("MUSICA/LIVE_UP2.wav"))
                        pygame.mixer.Channel(39).set_volume(.02)

                if JEFE3_TOTAL == True:

                    screen.blit(BOSS3.image, BOSS3.rect)
                    FBS3 = True

                    if act_mover_izq3 == True:

                        if BOSS3.rect.y == 234:
                            mover_izq3 = True
                            if mover_izq3 == True:
                                BOSS3.rect.x -= 3
                        if BOSS3.rect.x <= 1110:
                            mover_izq3 = False
                            BOSS3.rect.x = 1110
                            act_oscilar_boss3 = True


                    if act_oscilar_boss3 == True:

                        PRIMERA_FB3 = True

                        if BOSS3.rect.x == 1110:

                            act_mover_izq3 = False
                            if BOSS3.rect.y <= 0:
                                BOSS3.rect.y = 0
                                oscilar_boss3 = False
                            if BOSS3.rect.y >= 422:
                                BOSS3.rect.y = 422
                                oscilar_boss3 = True
                            if oscilar_boss3 == False:
                                BOSS3.rect.y += 6
                            elif oscilar_boss3 == True:
                                BOSS3.rect.y -= 6

                    if FBS3 == True:

                        if PRIMERA_FB3 == True:
                            if BOSS3.rect.y == 0:
                                ver_bola_fuego1_3 = True
                            if ver_bola_fuego1_3 == True:
                                if BOSS3.rect.y == 0 and BOSS3.rect.x == 1110:
                                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("MUSICA/SONIDO_BOWSER.wav"))
                                    pygame.mixer.Channel(1).set_volume(.15)
                                screen.blit(bola_fuego1_3.image, bola_fuego1_3.rect)
                                mover_bola_fuego1_3 = True
                                SEGUNDA_FB3 = True
                                if mover_bola_fuego1_3 == True:
                                    bola_fuego1_3.rect.x -= 35
                                    if bola_fuego1_3.rect.colliderect(Flappy3.rect):
                                        VIDAS -= 1
                                        ver_bola_fuego1_3 = False
                                        screen.blit(BUM1_3.image, Flappy3.rect)
                                        pygame.mixer.Channel(2).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                                        pygame.mixer.Channel(2).set_volume(.15)

                        if SEGUNDA_FB3 == True:
                            RELOJ_3.rect.x -= 1
                            if RELOJ_3.rect.x == 1255:
                                ver_bola_fuego2_3 = True
                            if ver_bola_fuego2_3 == True:
                                if MUSICA_FB_2_3 == True:
                                    pygame.mixer.Channel(3).play(pygame.mixer.Sound("MUSICA/SONIDO_BOWSER.wav"))
                                    pygame.mixer.Channel(3).set_volume(.15)
                                screen.blit(bola_fuego2_3.image, bola_fuego2_3.rect)
                                mover_bola_fuego2_3 = True
                                TERCERA_FB3 = True
                                if mover_bola_fuego2_3 == True:
                                    MUSICA_FB_2_3 = False
                                    bola_fuego2_3.rect.x -= 35
                                    if bola_fuego2_3.rect.colliderect(Flappy3.rect):
                                        VIDAS -= 1
                                        ver_bola_fuego2_3 = False
                                        screen.blit(BUM2_3.image, Flappy3.rect)
                                        pygame.mixer.Channel(4).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                                        pygame.mixer.Channel(4).set_volume(.15)


                        if TERCERA_FB3 == True:
                            if RELOJ_3.rect.x == 1230:
                                ver_bola_fuego3_3 = True
                            if ver_bola_fuego3_3 == True:
                                if MUSICA_FB_3_3 == True:
                                    pygame.mixer.Channel(5).play(pygame.mixer.Sound("MUSICA/SONIDO_BOWSER.wav"))
                                    pygame.mixer.Channel(5).set_volume(.15)
                                screen.blit(bola_fuego3_3.image, bola_fuego3_3.rect)
                                mover_bola_fuego3_3 = True
                                CUARTA_FB3 = True
                                if mover_bola_fuego3_3 == True:
                                    MUSICA_FB_3_3 = False
                                    bola_fuego3_3.rect.x -= 35
                                    if bola_fuego3_3.rect.colliderect(Flappy3.rect):
                                        VIDAS -= 1
                                        ver_bola_fuego3_3 = False
                                        screen.blit(BUM3_3.image, Flappy3.rect)
                                        pygame.mixer.Channel(6).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                                        pygame.mixer.Channel(6).set_volume(.15)

                        if CUARTA_FB3 == True:
                            if RELOJ_3.rect.x == 1210:
                                ver_bola_fuego4_3 = True
                            if ver_bola_fuego4_3 == True:
                                if MUSICA_FB_4_3 == True:
                                    pygame.mixer.Channel(7).play(pygame.mixer.Sound("MUSICA/SONIDO_BOWSER.wav"))
                                    pygame.mixer.Channel(7).set_volume(.15)
                                screen.blit(bola_fuego4_3.image, bola_fuego4_3.rect)
                                mover_bola_fuego4_3 = True
                                QUINTA_FB3 = True
                                if mover_bola_fuego4_3 == True:
                                    MUSICA_FB_4_3 = False
                                    bola_fuego4_3.rect.x -= 35
                                    if bola_fuego4_3.rect.colliderect(Flappy3.rect):
                                        VIDAS -= 1
                                        ver_bola_fuego4_3 = False
                                        screen.blit(BUM4_3.image, Flappy3.rect)
                                        pygame.mixer.Channel(8).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                                        pygame.mixer.Channel(8).set_volume(.15)

                        if QUINTA_FB3 == True:
                            if RELOJ_3.rect.x == 1170:
                                ver_bola_fuego5_3 = True
                            if ver_bola_fuego5_3 == True:
                                if MUSICA_FB_5_3 == True:
                                    pygame.mixer.Channel(9).play(pygame.mixer.Sound("MUSICA/SONIDO_BOWSER.wav"))
                                    pygame.mixer.Channel(9).set_volume(.15)
                                screen.blit(bola_fuego5_3.image, bola_fuego5_3.rect)
                                mover_bola_fuego5_3 = True
                                SEXTA_FB3 = True
                                if mover_bola_fuego5_3 == True:
                                    MUSICA_FB_5_3 = False
                                    bola_fuego5_3.rect.x -= 35
                                    if bola_fuego5_3.rect.colliderect(Flappy3.rect):
                                        VIDAS -= 1
                                        ver_bola_fuego5_3 = False
                                        screen.blit(BUM5_3.image, Flappy3.rect)
                                        pygame.mixer.Channel(10).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                                        pygame.mixer.Channel(10).set_volume(.15)

                        if SEXTA_FB3 == True:
                            if RELOJ_3.rect.x == 1150:
                                ver_bola_fuego6_3 = True
                            if ver_bola_fuego6_3 == True:
                                if MUSICA_FB_6_3 == True:
                                    pygame.mixer.Channel(11).play(pygame.mixer.Sound("MUSICA/SONIDO_BOWSER.wav"))
                                    pygame.mixer.Channel(11).set_volume(.15)
                                screen.blit(bola_fuego6_3.image, bola_fuego6_3.rect)
                                mover_bola_fuego6_3 = True
                                SEPTIMA_FB3 = True
                                if mover_bola_fuego6_3 == True:
                                    MUSICA_FB_6_3 = False
                                    bola_fuego6_3.rect.x -= 35
                                    if bola_fuego6_3.rect.colliderect(Flappy3.rect):
                                        VIDAS -= 1
                                        ver_bola_fuego6_3 = False
                                        screen.blit(BUM6_3.image, Flappy3.rect)
                                        pygame.mixer.Channel(12).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                                        pygame.mixer.Channel(12).set_volume(.15)

                        if SEPTIMA_FB3 == True:
                            if RELOJ_3.rect.x == 1130:
                                ver_bola_fuego7_3 = True
                            if ver_bola_fuego7_3 == True:
                                if MUSICA_FB_7_3 == True:
                                    pygame.mixer.Channel(13).play(pygame.mixer.Sound("MUSICA/SONIDO_BOWSER.wav"))
                                    pygame.mixer.Channel(13).set_volume(.15)
                                screen.blit(bola_fuego7_3.image, bola_fuego7_3.rect)
                                mover_bola_fuego7_3 = True
                                OCTAVA_FB3 = True
                                if mover_bola_fuego7_3 == True:
                                    MUSICA_FB_7_3 = False
                                    bola_fuego7_3.rect.x -= 35
                                    if bola_fuego7_3.rect.colliderect(Flappy3.rect):
                                        VIDAS -= 1
                                        ver_bola_fuego7_3 = False
                                        screen.blit(BUM7_3.image, Flappy3.rect)
                                        pygame.mixer.Channel(14).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                                        pygame.mixer.Channel(14).set_volume(.15)

                        if OCTAVA_FB3 == True:
                            if RELOJ_3.rect.x == 1100:
                                ver_bola_fuego8_3 = True
                            if ver_bola_fuego8_3 == True:
                                if MUSICA_FB_8_3 == True:
                                    pygame.mixer.Channel(15).play(pygame.mixer.Sound("MUSICA/SONIDO_BOWSER.wav"))
                                    pygame.mixer.Channel(15).set_volume(.15)
                                screen.blit(bola_fuego8_3.image, bola_fuego8_3.rect)
                                mover_bola_fuego8_3 = True
                                NOVENA_FB3 = True
                                if mover_bola_fuego8_3 == True:
                                    MUSICA_FB_8_3 = False
                                    bola_fuego8_3.rect.x -= 35
                                    if bola_fuego8_3.rect.colliderect(Flappy3.rect):
                                        VIDAS -= 1
                                        ver_bola_fuego8_3 = False
                                        screen.blit(BUM8_3.image, Flappy3.rect)
                                        pygame.mixer.Channel(16).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                                        pygame.mixer.Channel(16).set_volume(.15)

                        if NOVENA_FB3 == True:
                            if RELOJ_3.rect.x == 1080:
                                ver_bola_fuego9_3 = True
                            if ver_bola_fuego9_3 == True:
                                if MUSICA_FB_9_3 == True:
                                    pygame.mixer.Channel(17).play(pygame.mixer.Sound("MUSICA/SONIDO_BOWSER.wav"))
                                    pygame.mixer.Channel(17).set_volume(.15)
                                screen.blit(bola_fuego9_3.image, bola_fuego9_3.rect)
                                mover_bola_fuego9_3 = True
                                DECIMA_FB3 = True
                                if mover_bola_fuego9_3 == True:
                                    MUSICA_FB_9_3 = False
                                    bola_fuego9_3.rect.x -= 35
                                    if bola_fuego9_3.rect.colliderect(Flappy3.rect):
                                        VIDAS -= 1
                                        ver_bola_fuego9_3 = False
                                        screen.blit(BUM9_3.image, Flappy3.rect)
                                        pygame.mixer.Channel(18).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                                        pygame.mixer.Channel(18).set_volume(.15)

                        if DECIMA_FB3 == True:
                            if RELOJ_3.rect.x == 1060:
                                ver_bola_fuego10_3 = True
                            if ver_bola_fuego10_3 == True:
                                if MUSICA_FB_10_3 == True:
                                    pygame.mixer.Channel(19).play(pygame.mixer.Sound("MUSICA/SONIDO_BOWSER.wav"))
                                    pygame.mixer.Channel(19).set_volume(.15)
                                screen.blit(bola_fuego10_3.image, bola_fuego10_3.rect)
                                mover_bola_fuego10_3 = True
                                ONCEAVA_FB3 = True
                                if mover_bola_fuego10_3 == True:
                                    MUSICA_FB_10_3 = False
                                    bola_fuego10_3.rect.x -= 35
                                    if bola_fuego10_3.rect.colliderect(Flappy3.rect):
                                        VIDAS -= 1
                                        ver_bola_fuego10_3 = False
                                        screen.blit(BUM10_3.image, Flappy3.rect)
                                        pygame.mixer.Channel(20).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                                        pygame.mixer.Channel(20).set_volume(.15)

                        if ONCEAVA_FB3 == True:
                            if RELOJ_3.rect.x == 1010:
                                ver_bola_fuego11_3 = True
                            if ver_bola_fuego11_3 == True:
                                if MUSICA_FB_11_3 == True:
                                    pygame.mixer.Channel(21).play(pygame.mixer.Sound("MUSICA/SONIDO_BOWSER.wav"))
                                    pygame.mixer.Channel(21).set_volume(.15)
                                screen.blit(bola_fuego11_3.image, bola_fuego11_3.rect)
                                mover_bola_fuego11_3 = True
                                DOCEAVA_FB3 = True
                                if mover_bola_fuego11_3 == True:
                                    MUSICA_FB_11_3 = False
                                    bola_fuego11_3.rect.x -= 35
                                    if bola_fuego11_3.rect.colliderect(Flappy3.rect):
                                        VIDAS -= 1
                                        ver_bola_fuego11_3 = False
                                        screen.blit(BUM11_3.image, Flappy3.rect)
                                        pygame.mixer.Channel(22).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                                        pygame.mixer.Channel(22).set_volume(.15)

                        if DOCEAVA_FB3 == True:
                            if RELOJ_3.rect.x == 990:
                                ver_bola_fuego12_3 = True
                            if ver_bola_fuego12_3 == True:
                                if MUSICA_FB_12_3 == True:
                                    pygame.mixer.Channel(23).play(pygame.mixer.Sound("MUSICA/SONIDO_BOWSER.wav"))
                                    pygame.mixer.Channel(23).set_volume(.15)
                                screen.blit(bola_fuego12_3.image, bola_fuego12_3.rect)
                                mover_bola_fuego12_3 = True
                                TRECEAVA_FB3 = True
                                if mover_bola_fuego12_3 == True:
                                    MUSICA_FB_12_3 = False
                                    bola_fuego12_3.rect.x -= 35
                                    if bola_fuego12_3.rect.colliderect(Flappy3.rect):
                                        VIDAS -= 1
                                        ver_bola_fuego12_3 = False
                                        screen.blit(BUM12_3.image, Flappy3.rect)
                                        pygame.mixer.Channel(24).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                                        pygame.mixer.Channel(24).set_volume(.15)

                        if TRECEAVA_FB3 == True:
                            if RELOJ_3.rect.x == 970:
                                ver_bola_fuego13_3 = True
                            if ver_bola_fuego13_3 == True:
                                if MUSICA_FB_13_3 == True:
                                    pygame.mixer.Channel(25).play(pygame.mixer.Sound("MUSICA/SONIDO_BOWSER.wav"))
                                    pygame.mixer.Channel(25).set_volume(.15)
                                screen.blit(bola_fuego13_3.image, bola_fuego13_3.rect)
                                mover_bola_fuego13_3 = True
                                STOP_BOSS4 = True
                                if mover_bola_fuego13_3 == True:
                                    MUSICA_FB_13_3 = False
                                    bola_fuego13_3.rect.x -= 35
                                    if bola_fuego13_3.rect.colliderect(Flappy3.rect):
                                        VIDAS -= 1
                                        ver_bola_fuego13_3 = False
                                        screen.blit(BUM13_3.image, Flappy3.rect)
                                        pygame.mixer.Channel(26).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                                        pygame.mixer.Channel(26).set_volume(.15)


                        if STOP_BOSS4 == True:

                            if FB_GRANDE1_3 == True:

                                if ACT_MOV_BOSS_3 == True:
                                    if BOSS3.rect.y >= 235:
                                        BOSS3.rect.y = 235
                                        RELOJ_3.rect.y += 1
                                if RELOJ_3.rect.y == 240:
                                    ver_bola_fuego14_3 = True
                                if ver_bola_fuego14_3 == True:
                                    if MUSICA_FB_14_3 == True:
                                        pygame.mixer.Channel(27).play(pygame.mixer.Sound("MUSICA/SONIDO_BOWSER.wav"))
                                        pygame.mixer.Channel(27).set_volume(.15)
                                    screen.blit(bola_fuego14_3.image, bola_fuego14_3.rect)
                                    mover_bola_fuego14_3 = True
                                    FB_GRANDE2_3 = True
                                    if mover_bola_fuego14_3 == True:
                                        MUSICA_FB_14_3 = False
                                        bola_fuego14_3.rect.x -= 35
                                        act_oscilar_boss3 = False
                                        if ACT_MOV_FB_3 == True:
                                            BOSS3.rect.y -= 12
                                        if bola_fuego14_3.rect.colliderect(Flappy3.rect):
                                            VIDAS -= 1
                                            ver_bola_fuego14_3 = False
                                            screen.blit(BUM14_3.image, Flappy3.rect)
                                            pygame.mixer.Channel(28).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                                            pygame.mixer.Channel(28).set_volume(.15)

                            if FB_GRANDE2_3 == True:
                                RELOJ_3.rect.y += 1
                                if RELOJ_3.rect.y == 260:
                                    ver_bola_fuego15_3 = True
                                if ver_bola_fuego15_3 == True:
                                    if MUSICA_FB_15_3 == True:
                                        pygame.mixer.Channel(29).play(pygame.mixer.Sound("MUSICA/SONIDO_BOWSER.wav"))
                                        pygame.mixer.Channel(29).set_volume(.15)
                                    screen.blit(bola_fuego15_3.image, bola_fuego15_3.rect)
                                    mover_bola_fuego15_3 = True
                                    if BOSS3.rect.y <= 0:
                                        BOSS3.rect.y = 0
                                    FB_GRANDE3_3 = True
                                    if mover_bola_fuego15_3 == True:
                                        MUSICA_FB_15_3 = False
                                        bola_fuego15_3.rect.x -= 35
                                        if bola_fuego15_3.rect.colliderect(Flappy3.rect):
                                            VIDAS -= 1
                                            ver_bola_fuego15_3 = False
                                            screen.blit(BUM15_3.image, Flappy3.rect)
                                            pygame.mixer.Channel(30).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                                            pygame.mixer.Channel(30).set_volume(.15)

                            if FB_GRANDE3_3 == True:
                                ACT_MOV_FB_3 = False
                                ACT_MOV_BOSS_3 = False
                                if MOV_BOSS_3 == True:
                                    BOSS3.rect.y += 20
                                if RELOJ_3.rect.y == 280:
                                    ver_bola_fuego16_3 = True
                                if ver_bola_fuego16_3 == True:
                                    if MUSICA_FB_16_3 == True:
                                        pygame.mixer.Channel(31).play(pygame.mixer.Sound("MUSICA/SONIDO_BOWSER.wav"))
                                        pygame.mixer.Channel(31).set_volume(.15)
                                    screen.blit(bola_fuego16_3.image, bola_fuego16_3.rect)
                                    mover_bola_fuego16_3 = True
                                    if mover_bola_fuego16_3 == True:
                                        MUSICA_FB_16_3 = False
                                        bola_fuego16_3.rect.x -= 35
                                        if bola_fuego16_3.rect.colliderect(Flappy3.rect):
                                            VIDAS -= 1
                                            ver_bola_fuego16_3 = False
                                            screen.blit(BUM16_3.image, Flappy3.rect)
                                            pygame.mixer.Channel(32).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                                            pygame.mixer.Channel(32).set_volume(.15)


                            if BOSS3.rect.y >= 422:
                                BOSS3.rect.y = 422
                                FB_GRANDE4_3 = True

                            if FB_GRANDE4_3 == True:

                                MOV_BOSS_3 = False
                                if DESACTIVAR_3 == True:
                                    BOSS3.rect.y -= 10
                                RELOJ2_3.rect.x += 1

                                if RELOJ2_3.rect.x == 28:
                                    ver_bola_fuego17_3 = True
                                if ver_bola_fuego17_3 == True:
                                    if MUSICA_FB_17_3 == True:
                                        pygame.mixer.Channel(33).play(pygame.mixer.Sound("MUSICA/SONIDO_BOWSER.wav"))
                                        pygame.mixer.Channel(33).set_volume(.15)
                                    screen.blit(bola_fuego17_3.image, bola_fuego17_3.rect)
                                    mover_bola_fuego17_3 = True
                                    FB_GRANDE5_3 = True
                                    if mover_bola_fuego17_3 == True:
                                        MUSICA_FB_17_3 = False
                                        bola_fuego17_3.rect.x -= 35
                                        act_oscilar_boss3 = False
                                        if bola_fuego17_3.rect.colliderect(Flappy3.rect):
                                            VIDAS -= 1
                                            ver_bola_fuego17_3 = False
                                            screen.blit(BUM17_3.image, Flappy3.rect)
                                            pygame.mixer.Channel(34).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                                            pygame.mixer.Channel(34).set_volume(.15)

                            if FB_GRANDE5_3 == True:
                                if BOSS3.rect.y <= 10:
                                    DESACTIVAR_3 = False
                                    BOSS3.rect.y = 10
                                    if DESACTIVAR2_3 == True:
                                        BOSS3.rect.y -= 5
                                    if RELOJ2_3.rect.x == 50:
                                        ver_bola_fuego18_3 = True
                                if ver_bola_fuego18_3 == True:
                                    if MUSICA_FB_18_3 == True:
                                        pygame.mixer.Channel(35).play(pygame.mixer.Sound("MUSICA/SONIDO_BOWSER.wav"))
                                        pygame.mixer.Channel(35).set_volume(.15)
                                    screen.blit(bola_fuego18_3.image, bola_fuego18_3.rect)
                                    mover_bola_fuego18_3 = True
                                    FB_GRANDE6_3 = True
                                    if mover_bola_fuego18_3 == True:
                                        MUSICA_FB_18_3 = False
                                        bola_fuego18_3.rect.x -= 35
                                        act_oscilar_boss3 = False
                                        if bola_fuego18_3.rect.colliderect(Flappy3.rect):
                                            VIDAS -= 1
                                            ver_bola_fuego18_3 = False
                                            screen.blit(BUM18_3.image, Flappy3.rect)
                                            pygame.mixer.Channel(36).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                                            pygame.mixer.Channel(36).set_volume(.15)

                            if FB_GRANDE6_3 == True:
                                if DESACTIVAR3_3 == True:
                                    BOSS3.rect.y += 15
                                if BOSS3.rect.y >= 422:
                                    BOSS3.rect.y = 422
                                    DESACTIVAR3_3 = False
                                if RELOJ2_3.rect.x == 73:
                                    ver_bola_fuego19_3 = True
                                if ver_bola_fuego19_3 == True:
                                    if MUSICA_FB_19_3 == True:
                                        pygame.mixer.Channel(37).play(pygame.mixer.Sound("MUSICA/SONIDO_BOWSER.wav"))
                                        pygame.mixer.Channel(37).set_volume(.15)
                                    screen.blit(bola_fuego19_3.image, bola_fuego19_3.rect)
                                    mover_bola_fuego19_3 = True
                                    if mover_bola_fuego19_3 == True:
                                        MUSICA_FB_19_3 = False
                                        bola_fuego19_3.rect.x -= 35
                                        BOSS3.rect.x += 7
                                        if bola_fuego19_3.rect.colliderect(Flappy3.rect):
                                            VIDAS -= 1
                                            ver_bola_fuego19_3 = False
                                            screen.blit(BUM19_3.image, Flappy3.rect)
                                            pygame.mixer.Channel(38).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                                            pygame.mixer.Channel(38).set_volume(.15)




            if NIVEL == 4:
                screen.blit(bg_4,[0,0])
                if mov_flap_izq3 == True:
                    Flappy4.rect.x  = 140
                screen.blit(Flappy4.image, Flappy4.rect)
                Flappy4.Movimiento_Pajaro(event)

                if BATALLAFINAL == True:

                    RELOJ_BATALLAFINAL.rect.x += 1

                    if RELOJ_BATALLAFINAL.rect.x >= 50:
                        if ver1 == True:
                            screen.blit(PROYECTIL3_1.image, PROYECTIL3_1.rect)
                            PROYECTIL3_1.rect.x -= 20
                            if PROYECTIL3_1.rect.colliderect(Flappy4.rect):
                                ver1 = False
                                VIDAS -= 1
                                screen.blit(BUM3.image, Flappy4.rect)
                                pygame.mixer.Channel(50).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                                pygame.mixer.Channel(50).set_volume(.15)

                    if RELOJ_BATALLAFINAL.rect.x >= 100:
                        if ver2 == True:
                            screen.blit(PROYECTIL2_1.image, PROYECTIL2_1.rect)
                            PROYECTIL2_1.rect.x -= 20
                            if PROYECTIL2_1.rect.colliderect(Flappy4.rect):
                                ver2 = False
                                VIDAS -= 1
                                screen.blit(BUM3.image, Flappy4.rect)
                                pygame.mixer.Channel(50).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                                pygame.mixer.Channel(50).set_volume(.15)

                    if RELOJ_BATALLAFINAL.rect.x >= 150:
                        if ver3 == True:
                            screen.blit(PROYECTIL1_1.image, PROYECTIL1_1.rect)
                            PROYECTIL1_1.rect.x -= 20
                            if PROYECTIL1_1.rect.colliderect(Flappy4.rect):
                                ver3 = False
                                VIDAS -= 1
                                screen.blit(BUM3.image, Flappy4.rect)
                                pygame.mixer.Channel(50).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                                pygame.mixer.Channel(50).set_volume(.15)

                    if RELOJ_BATALLAFINAL.rect.x >= 200:
                        if ver4 == True:
                            screen.blit(PROYECTIL3_2.image, PROYECTIL3_2.rect)
                            PROYECTIL3_2.rect.x -= 30
                            if PROYECTIL3_2.rect.colliderect(Flappy4.rect):
                                ver4 = False
                                VIDAS -= 1
                                screen.blit(BUM3.image, Flappy4.rect)
                                pygame.mixer.Channel(50).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                                pygame.mixer.Channel(50).set_volume(.15)

                    if RELOJ_BATALLAFINAL.rect.x >= 250:
                        if ver5 == True:
                            screen.blit(PROYECTIL1_2.image, PROYECTIL1_2.rect)
                            PROYECTIL1_2.rect.x -= 30
                            if PROYECTIL1_2.rect.colliderect(Flappy4.rect):
                                ver5 = False
                                VIDAS -= 1
                                screen.blit(BUM3.image, Flappy4.rect)
                                pygame.mixer.Channel(50).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                                pygame.mixer.Channel(50).set_volume(.15)

                    if RELOJ_BATALLAFINAL.rect.x >= 300:
                        if ver6 == True:
                            screen.blit(PROYECTIL2_2.image, PROYECTIL2_2.rect)
                            PROYECTIL2_2.rect.x -= 30
                            if PROYECTIL2_2.rect.colliderect(Flappy4.rect):
                                ver6 = False
                                VIDAS -= 1
                                screen.blit(BUM3.image, Flappy4.rect)
                                pygame.mixer.Channel(50).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                                pygame.mixer.Channel(50).set_volume(.15)

                    if RELOJ_BATALLAFINAL.rect.x >= 350:
                        if ver7 == True:
                            screen.blit(PROYECTIL3_3.image, PROYECTIL3_3.rect)
                            PROYECTIL3_3.rect.x -= 40
                            if PROYECTIL3_3.rect.colliderect(Flappy4.rect):
                                ver7 = False
                                VIDAS -= 1
                                screen.blit(BUM3.image, Flappy4.rect)
                                pygame.mixer.Channel(50).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                                pygame.mixer.Channel(50).set_volume(.15)

                    if RELOJ_BATALLAFINAL.rect.x >= 400:
                        if ver8 == True:
                            screen.blit(PROYECTIL2_3.image, PROYECTIL2_3.rect)
                            PROYECTIL2_3.rect.x -= 40
                            if PROYECTIL2_3.rect.colliderect(Flappy4.rect):
                                ver8 = False
                                VIDAS -= 1
                                screen.blit(BUM3.image, Flappy4.rect)
                                pygame.mixer.Channel(50).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                                pygame.mixer.Channel(50).set_volume(.15)

                    if RELOJ_BATALLAFINAL.rect.x >= 450:
                        if ver9 == True:
                            screen.blit(PROYECTIL1_3.image, PROYECTIL1_3.rect)
                            PROYECTIL1_3.rect.x -= 50
                            if PROYECTIL1_3.rect.colliderect(Flappy4.rect):
                                ver9 = False
                                VIDAS -= 1
                                screen.blit(BUM3.image, Flappy4.rect)
                                pygame.mixer.Channel(50).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                                pygame.mixer.Channel(50).set_volume(.15)

                    if RELOJ_BATALLAFINAL.rect.x >= 480:
                        screen.blit(bg_batallafinal,(0,0))
                        if ver_paj == True:
                            screen.blit(Flappy5.image, Flappy5.rect)
                            Flappy5.Movimiento_Pajaro(event)

                    if RELOJ_BATALLAFINAL.rect.x >= 650:
                        if ver_boss1 == True:
                            screen.blit(BOSS1_BF.image, BOSS1_BF.rect)
                        if ver_boss2 == True:
                            screen.blit(BOSS2_BF.image, BOSS2_BF.rect)
                        if ver_boss3 == True:
                            screen.blit(BOSS3_BF.image, BOSS3_BF.rect)
                        BOSS1_BF.rect.x -= 20
                        BOSS2_BF.rect.x -= 20
                        BOSS3_BF.rect.x -= 20
                        if BOSS1_BF.rect.x <= 1190:
                            BOSS1_BF.rect.x = 1190
                        if BOSS2_BF.rect.x <= 1180:
                            BOSS2_BF.rect.x = 1180
                        if BOSS3_BF.rect.x <= 1110:
                            BOSS3_BF.rect.x = 1110

                        if RELOJ_BATALLAFINAL.rect.x >= 675:
                            if ver10 == True:
                                screen.blit(PROYECTIL3_4.image, PROYECTIL3_4.rect)
                                PROYECTIL3_4.rect.x -= 25
                                if RELOJ_BATALLAFINAL.rect.x == 675:
                                    pygame.mixer.Channel(51).play(pygame.mixer.Sound("MUSICA/SONIDO_BOWSER.wav"))
                                    pygame.mixer.Channel(51).set_volume(.15)
                                if PROYECTIL3_4.rect.colliderect(Flappy5.rect):
                                    ver10 = False
                                    VIDAS -= 1
                                    screen.blit(BUM3.image, Flappy5.rect)
                                    pygame.mixer.Channel(50).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                                    pygame.mixer.Channel(50).set_volume(.15)

                        if RELOJ_BATALLAFINAL.rect.x >= 700:
                            if ver11 == True:
                                screen.blit(PROYECTIL2_4.image, PROYECTIL2_4.rect)
                                PROYECTIL2_4.rect.x -= 25
                                if RELOJ_BATALLAFINAL.rect.x == 700:
                                    pygame.mixer.Channel(52).play(pygame.mixer.Sound("MUSICA/SONIDO_ROCA.wav"))
                                    pygame.mixer.Channel(52).set_volume(.25)
                                if PROYECTIL2_4.rect.colliderect(Flappy5.rect):
                                    ver11 = False
                                    VIDAS -= 1
                                    screen.blit(BUM3.image, Flappy5.rect)
                                    pygame.mixer.Channel(50).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                                    pygame.mixer.Channel(50).set_volume(.15)

                        if RELOJ_BATALLAFINAL.rect.x >= 725:
                            if ver12 == True:
                                screen.blit(PROYECTIL1_4.image, PROYECTIL1_4.rect)
                                PROYECTIL1_4.rect.x -= 25
                                if RELOJ_BATALLAFINAL.rect.x == 725:
                                    pygame.mixer.Channel(53).play(pygame.mixer.Sound("MUSICA/FIREBALL.wav"))
                                    pygame.mixer.Channel(53).set_volume(.15)
                                if PROYECTIL1_4.rect.colliderect(Flappy5.rect):
                                    ver12 = False
                                    VIDAS -= 1
                                    screen.blit(BUM3.image, Flappy5.rect)
                                    pygame.mixer.Channel(50).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                                    pygame.mixer.Channel(50).set_volume(.15)

                        if RELOJ_BATALLAFINAL.rect.x >= 750:
                            if ver13 == True:
                                screen.blit(PROYECTIL3_5.image, PROYECTIL3_5.rect)
                                PROYECTIL3_5.rect.x -= 25
                                if RELOJ_BATALLAFINAL.rect.x == 750:
                                    pygame.mixer.Channel(51).play(pygame.mixer.Sound("MUSICA/SONIDO_BOWSER.wav"))
                                    pygame.mixer.Channel(51).set_volume(.15)
                                if PROYECTIL3_5.rect.colliderect(Flappy5.rect):
                                    ver13 = False
                                    VIDAS -= 1
                                    screen.blit(BUM3.image, Flappy5.rect)
                                    pygame.mixer.Channel(50).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                                    pygame.mixer.Channel(50).set_volume(.15)

                        if RELOJ_BATALLAFINAL.rect.x >= 775:
                            if ver14 == True:
                                screen.blit(PROYECTIL2_5.image, PROYECTIL2_5.rect)
                                PROYECTIL2_5.rect.x -= 25
                                if RELOJ_BATALLAFINAL.rect.x == 775:
                                    pygame.mixer.Channel(52).play(pygame.mixer.Sound("MUSICA/SONIDO_ROCA.wav"))
                                    pygame.mixer.Channel(52).set_volume(.25)
                                if PROYECTIL2_5.rect.colliderect(Flappy5.rect):
                                    ver14 = False
                                    VIDAS -= 1
                                    screen.blit(BUM3.image, Flappy5.rect)
                                    pygame.mixer.Channel(50).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                                    pygame.mixer.Channel(50).set_volume(.15)

                        if RELOJ_BATALLAFINAL.rect.x >= 800:
                            if ver15 == True:
                                screen.blit(PROYECTIL1_5.image, PROYECTIL1_5.rect)
                                PROYECTIL1_5.rect.x -= 25
                                if RELOJ_BATALLAFINAL.rect.x == 800:
                                    pygame.mixer.Channel(53).play(pygame.mixer.Sound("MUSICA/FIREBALL.wav"))
                                    pygame.mixer.Channel(53).set_volume(.15)
                                if PROYECTIL1_5.rect.colliderect(Flappy5.rect):
                                    ver15 = False
                                    VIDAS -= 1
                                    screen.blit(BUM3.image, Flappy5.rect)
                                    pygame.mixer.Channel(50).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                                    pygame.mixer.Channel(50).set_volume(.15)

                        if RELOJ_BATALLAFINAL.rect.x >= 825:
                            if ver16 == True:
                                screen.blit(PROYECTIL3_6.image, PROYECTIL3_6.rect)
                                PROYECTIL3_6.rect.x -= 25
                                if RELOJ_BATALLAFINAL.rect.x == 825:
                                    pygame.mixer.Channel(51).play(pygame.mixer.Sound("MUSICA/SONIDO_BOWSER.wav"))
                                    pygame.mixer.Channel(51).set_volume(.15)
                                if PROYECTIL3_6.rect.colliderect(Flappy5.rect):
                                    ver16 = False
                                    VIDAS -= 1
                                    screen.blit(BUM3.image, Flappy5.rect)
                                    pygame.mixer.Channel(50).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                                    pygame.mixer.Channel(50).set_volume(.15)

                        if RELOJ_BATALLAFINAL.rect.x >= 825:
                            if ver17 == True:
                                screen.blit(PROYECTIL2_6.image, PROYECTIL2_6.rect)
                                PROYECTIL2_6.rect.x -= 25
                                if RELOJ_BATALLAFINAL.rect.x == 825:
                                    pygame.mixer.Channel(52).play(pygame.mixer.Sound("MUSICA/SONIDO_ROCA.wav"))
                                    pygame.mixer.Channel(52).set_volume(.25)
                                if PROYECTIL2_6.rect.colliderect(Flappy5.rect):
                                    ver17 = False
                                    VIDAS -= 1
                                    screen.blit(BUM3.image, Flappy5.rect)
                                    pygame.mixer.Channel(50).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                                    pygame.mixer.Channel(50).set_volume(.15)

                        if RELOJ_BATALLAFINAL.rect.x >= 860:
                            if ver18 == True:
                                screen.blit(PROYECTIL1_6.image, PROYECTIL1_6.rect)
                                PROYECTIL1_6.rect.x -= 25
                                if RELOJ_BATALLAFINAL.rect.x == 860:
                                    pygame.mixer.Channel(53).play(pygame.mixer.Sound("MUSICA/FIREBALL.wav"))
                                    pygame.mixer.Channel(53).set_volume(.15)
                                if PROYECTIL1_6.rect.colliderect(Flappy5.rect):
                                    ver18 = False
                                    VIDAS -= 1
                                    screen.blit(BUM3.image, Flappy5.rect)
                                    pygame.mixer.Channel(50).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                                    pygame.mixer.Channel(50).set_volume(.15)

                        if RELOJ_BATALLAFINAL.rect.x >= 860:
                            if ver19 == True:
                                screen.blit(PROYECTIL3_7.image, PROYECTIL3_7.rect)
                                PROYECTIL3_7.rect.x -= 25
                                if RELOJ_BATALLAFINAL.rect.x == 860:
                                    pygame.mixer.Channel(51).play(pygame.mixer.Sound("MUSICA/SONIDO_BOWSER.wav"))
                                    pygame.mixer.Channel(51).set_volume(.15)
                                if PROYECTIL3_7.rect.colliderect(Flappy5.rect):
                                    ver19 = False
                                    VIDAS -= 1
                                    screen.blit(BUM3.image, Flappy5.rect)
                                    pygame.mixer.Channel(50).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                                    pygame.mixer.Channel(50).set_volume(.15)

                        if RELOJ_BATALLAFINAL.rect.x >= 895:
                            if ver20 == True:
                                screen.blit(PROYECTIL2_7.image, PROYECTIL2_7.rect)
                                PROYECTIL2_7.rect.x -= 25
                                if RELOJ_BATALLAFINAL.rect.x == 895:
                                    pygame.mixer.Channel(52).play(pygame.mixer.Sound("MUSICA/SONIDO_ROCA.wav"))
                                    pygame.mixer.Channel(52).set_volume(.25)
                                if PROYECTIL2_7.rect.colliderect(Flappy5.rect):
                                    ver20 = False
                                    VIDAS -= 1
                                    screen.blit(BUM3.image, Flappy5.rect)
                                    pygame.mixer.Channel(50).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                                    pygame.mixer.Channel(50).set_volume(.15)

                        if RELOJ_BATALLAFINAL.rect.x >= 895:
                            if ver21 == True:
                                screen.blit(PROYECTIL1_7.image, PROYECTIL1_7.rect)
                                PROYECTIL1_7.rect.x -= 25
                                if RELOJ_BATALLAFINAL.rect.x == 895:
                                    pygame.mixer.Channel(53).play(pygame.mixer.Sound("MUSICA/FIREBALL.wav"))
                                    pygame.mixer.Channel(53).set_volume(.15)
                                if PROYECTIL1_7.rect.colliderect(Flappy5.rect):
                                    ver21 = False
                                    VIDAS -= 1
                                    screen.blit(BUM3.image, Flappy5.rect)
                                    pygame.mixer.Channel(50).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                                    pygame.mixer.Channel(50).set_volume(.15)

                        if RELOJ_BATALLAFINAL.rect.x >= 930:
                            if ver22 == True:
                                screen.blit(PROYECTIL3_8.image, PROYECTIL3_8.rect)
                                PROYECTIL3_8.rect.x -= 25
                                if RELOJ_BATALLAFINAL.rect.x == 930:
                                    pygame.mixer.Channel(51).play(pygame.mixer.Sound("MUSICA/SONIDO_BOWSER.wav"))
                                    pygame.mixer.Channel(51).set_volume(.15)
                                if PROYECTIL3_8.rect.colliderect(Flappy5.rect):
                                    ver22 = False
                                    VIDAS -= 1
                                    screen.blit(BUM3.image, Flappy5.rect)
                                    pygame.mixer.Channel(50).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                                    pygame.mixer.Channel(50).set_volume(.15)

                        if RELOJ_BATALLAFINAL.rect.x >= 970:
                            if ver23 == True:
                                screen.blit(ASTEROIDE.image, ASTEROIDE.rect)
                                ASTEROIDE.rect.x += 29
                                ASTEROIDE.rect.y -= 20
                                if ASTEROIDE.rect.colliderect(BOSS1_BF.rect):
                                    ver23 = False
                                    screen.blit(BUM3.image, BOSS1_BF.rect)
                                    pygame.mixer.Channel(50).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                                    pygame.mixer.Channel(50).set_volume(.15)
                                    pygame.mixer.Channel(54).play(pygame.mixer.Sound("MUSICA/MARIO.wav"))
                                    pygame.mixer.Channel(54).set_volume(.15)

                        if RELOJ_BATALLAFINAL.rect.x >= 980:
                            if ver_paj2 == True:
                                screen.blit(Flappy6.image,Flappy5.rect)
                                Flappy6.Movimiento_Pajaro(event)
                            ver_paj = False

                            if Flappy5.rect.y < 233:
                                Flappy5.rect.y += 20
                            if Flappy5.rect.y > 280:
                                Flappy5.rect.y -= 20
                            if Flappy5.rect.y == 279:
                                Flappy5.rect.y = 279


                        if RELOJ_BATALLAFINAL.rect.x >= 1000:
                            if ver24 == True:
                                screen.blit(HONGO.image, HONGO.rect)
                                HONGO.rect.y += 6
                                HONGO.rect.x -= 30
                                if HONGO.rect.colliderect(Flappy5.rect):
                                    ver24 = False
                                    screen.blit(BUM3.image, Flappy5.rect)
                                    pygame.mixer.Channel(55).play(pygame.mixer.Sound("MUSICA/SONIDO_HONGO.wav"))
                                    pygame.mixer.Channel(55).set_volume(.15)


                        if RELOJ_BATALLAFINAL.rect.x >= 1033:
                            if ver_nubes == True:
                                screen.blit(NUBE, [80,210])
                                screen.blit(NUBE, [80,17])
                                screen.blit(NUBE, [80,387])
                                ver_paj2 = False


                        if RELOJ_BATALLAFINAL.rect.x >= 1043:
                            ver_nubes = False
                            screen.blit(Flappy7.image, Flappy7.rect)
                            Flappy7.Movimiento_Pajaro(event)

                            screen.blit(Flappy8.image, Flappy8.rect)
                            Flappy8.Movimiento_Pajaro(event)

                            screen.blit(Flappy9.image, Flappy9.rect)
                            Flappy9.Movimiento_Pajaro(event)


                        if RELOJ_BATALLAFINAL.rect.x >= 1055:

                            if ver25 == True:
                                if act_ir_izq1 == False:
                                    screen.blit(PROYECTIL1_8.image, PROYECTIL1_8.rect)
                                    PROYECTIL1_8.rect.x -= 25
                                if RELOJ_BATALLAFINAL.rect.x == 1055:
                                    pygame.mixer.Channel(53).play(pygame.mixer.Sound("MUSICA/FIREBALL.wav"))
                                    pygame.mixer.Channel(53).set_volume(.15)
                                if PROYECTIL1_8.rect.x <= 200:
                                    PROYECTIL1_8.rect.x = 200
                                    act_ir_izq1 = True
                                if act_ir_izq1 == True:
                                    screen.blit(PROYECTIL1_8_v.image, PROYECTIL1_8_v.rect)
                                    PROYECTIL1_8_v.rect.x += 25
                                    if PROYECTIL1_8_v.rect.colliderect(BOSS1_BF):
                                        screen.blit(BUM3.image, BOSS1_BF.rect)
                                        pygame.mixer.Channel(50).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                                        pygame.mixer.Channel(50).set_volume(.15)
                                        pygame.mixer.Channel(54).play(pygame.mixer.Sound("MUSICA/MARIO.wav"))
                                        pygame.mixer.Channel(54).set_volume(.15)
                                        ver25 = False

                            if ver26 == True:
                                screen.blit(PROYECTIL2_8.image, PROYECTIL2_8.rect)
                                if act_ir_izq2 == False:
                                    PROYECTIL2_8.rect.x -= 25
                                if RELOJ_BATALLAFINAL.rect.x == 1055:
                                    pygame.mixer.Channel(51).play(pygame.mixer.Sound("MUSICA/SONIDO_BOWSER.wav"))
                                    pygame.mixer.Channel(51).set_volume(.15)
                                if PROYECTIL2_8.rect.x <= 220:
                                    PROYECTIL2_8.rect.x = 220
                                    act_ir_izq2 = True
                                if act_ir_izq2 == True:
                                    PROYECTIL2_8.rect.x += 25
                                    if PROYECTIL2_8.rect.colliderect(BOSS2_BF):
                                        screen.blit(BUM3.image, BOSS2_BF.rect)
                                        pygame.mixer.Channel(50).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                                        pygame.mixer.Channel(50).set_volume(.15)
                                        ver26 = False

                            if ver27 == True:
                                screen.blit(PROYECTIL3_9.image, PROYECTIL3_9.rect)
                                if act_ir_izq3 == False:
                                    PROYECTIL3_9.rect.x -= 25
                                if RELOJ_BATALLAFINAL.rect.x == 1055:
                                    pygame.mixer.Channel(51).play(pygame.mixer.Sound("MUSICA/SONIDO_BOWSER.wav"))
                                    pygame.mixer.Channel(51).set_volume(.15)
                                if PROYECTIL3_9.rect.x <= 200:
                                    PROYECTIL3_9.rect.x = 200
                                    act_ir_izq3 = True
                                    pygame.mixer.Channel(50).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                                    pygame.mixer.Channel(50).set_volume(.15)
                                if act_ir_izq3 == True:
                                    PROYECTIL3_9.rect.x += 25
                                    if PROYECTIL3_9.rect.colliderect(BOSS3_BF):
                                        screen.blit(BUM3.image, BOSS3_BF.rect)
                                        pygame.mixer.Channel(50).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                                        pygame.mixer.Channel(50).set_volume(.15)
                                        pygame.mixer.Channel(56).play(pygame.mixer.Sound("MUSICA/BOWSER_D.wav"))
                                        pygame.mixer.Channel(56).set_volume(.15)
                                        ver27 = False


                        if RELOJ_BATALLAFINAL.rect.x >= 1130:

                            if ver28 == True:
                                if act_ir_izq4 == False:
                                    screen.blit(PROYECTIL1_9.image, PROYECTIL1_9.rect)
                                    PROYECTIL1_9.rect.x -= 25
                                if RELOJ_BATALLAFINAL.rect.x == 1150:
                                    pygame.mixer.Channel(53).play(pygame.mixer.Sound("MUSICA/FIREBALL.wav"))
                                    pygame.mixer.Channel(53).set_volume(.15)
                                if PROYECTIL1_9.rect.x <= 200:
                                    PROYECTIL1_9.rect.x = 200
                                    act_ir_izq4 = True
                                if act_ir_izq4 == True:
                                    screen.blit(PROYECTIL1_9_v.image, PROYECTIL1_9_v.rect)
                                    PROYECTIL1_9_v.rect.x += 25
                                    if PROYECTIL1_9_v.rect.colliderect(BOSS1_BF):
                                        screen.blit(BUM3.image, BOSS1_BF.rect)
                                        pygame.mixer.Channel(50).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                                        pygame.mixer.Channel(50).set_volume(.15)
                                        pygame.mixer.Channel(54).play(pygame.mixer.Sound("MUSICA/MARIO.wav"))
                                        pygame.mixer.Channel(54).set_volume(.15)
                                        ver28 = False
                                        ver_boss1 = False
                                        ver_boss1_muerto = True

                            if ver_boss1_muerto == True:
                                screen.blit(BOSS1_MUERTO.image, BOSS1_MUERTO.rect)
                                BOSS1_MUERTO.rect.x += 5

                            if ver29 == True:
                                screen.blit(PROYECTIL2_9.image, PROYECTIL2_9.rect)
                                if act_ir_izq5 == False:
                                    PROYECTIL2_9.rect.x -= 25
                                if RELOJ_BATALLAFINAL.rect.x == 1150:
                                    pygame.mixer.Channel(51).play(pygame.mixer.Sound("MUSICA/SONIDO_ROCA.wav"))
                                    pygame.mixer.Channel(51).set_volume(.25)
                                if PROYECTIL2_9.rect.x <= 220:
                                    PROYECTIL2_9.rect.x = 220
                                    act_ir_izq5 = True
                                    pygame.mixer.Channel(50).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                                    pygame.mixer.Channel(50).set_volume(.15)
                                if act_ir_izq5 == True:
                                    PROYECTIL2_9.rect.x += 25
                                    if PROYECTIL2_9.rect.colliderect(BOSS2_BF):
                                        screen.blit(BUM3.image, BOSS2_BF.rect)
                                        pygame.mixer.Channel(50).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                                        pygame.mixer.Channel(50).set_volume(.15)
                                        ver29 = False
                                        ver_boss2 = False
                                        ver_boss2_muerto = True

                            if ver_boss2_muerto == True:
                                screen.blit(BOSS2_MUERTO.image, BOSS2_MUERTO.rect)
                                BOSS2_MUERTO.rect.x += 5

                        if RELOJ_BATALLAFINAL.rect.x >= 1220:
                            ver_boss3 = False
                            screen.blit(BOSS3_VOLTEADO.image, BOSS3_VOLTEADO.rect)
                            BOSS3_VOLTEADO.rect.x += 10

                        if RELOJ_BATALLAFINAL.rect.x >= 1230:
                            Flappy7.rect.x += 35
                            Flappy8.rect.x += 35
                            Flappy9.rect.x += 35


                        if RELOJ_BATALLAFINAL.rect.x >= 1260:
                            x_relativa5 = x5 % bg_espacial6.get_rect().width
                            screen.blit(bg_espacial6,[x_relativa5 - bg_espacial6.get_rect().width ,0])
                            if x_relativa5 < pantalla_x:
                                screen.blit(bg_espacial6,(x_relativa5,0))
                            x5 -= 30
                            if RELOJ_BATALLAFINAL.rect.x >= 1400:
                                x5 -= 10
                            if RELOJ_BATALLAFINAL.rect.x >= 1410:
                                x5 -= 10
                            if RELOJ_BATALLAFINAL.rect.x >= 1420:
                                x5 -= 10
                            if RELOJ_BATALLAFINAL.rect.x >= 1430:
                                x5 -= 10
                            if RELOJ_BATALLAFINAL.rect.x >= 1440:
                                x5 -= 10
                            if RELOJ_BATALLAFINAL.rect.x >= 1450:
                                x5 -= 10
                            if RELOJ_BATALLAFINAL.rect.x >= 1460:
                                x5 -= 10
                            if RELOJ_BATALLAFINAL.rect.x >= 1470:
                                pass

                        if RELOJ_BATALLAFINAL.rect.x >= 1260:
                            if ver_flappys_gigantes == True:
                                screen.blit(Flappy10.image,Flappy10.rect)
                                Flappy10.Movimiento_Pajaro(event)
                                screen.blit(Flappy11.image,Flappy11.rect)
                                Flappy11.Movimiento_Pajaro(event)
                                screen.blit(Flappy12.image,Flappy12.rect)
                                Flappy12.Movimiento_Pajaro(event)
                            if ver_boss3_vivo == True:
                                screen.blit(BOSS3_FINAL.image,BOSS3_FINAL.rect)

                        if RELOJ_BATALLAFINAL.rect.x >= 1300:
                            if ver30 == True:
                                screen.blit(PROYECTIL3_10.image, PROYECTIL3_10.rect)
                                screen.blit(PROYECTIL3_11.image, PROYECTIL3_11.rect)
                                screen.blit(PROYECTIL3_12.image, PROYECTIL3_12.rect)
                                if mov_projects == True:
                                    PROYECTIL3_10.rect.x -= 30
                                    PROYECTIL3_11.rect.x -= 30
                                    PROYECTIL3_11.rect.y += 6
                                    PROYECTIL3_12.rect.x -= 30
                                    PROYECTIL3_12.rect.y -= 6
                                if RELOJ_BATALLAFINAL.rect.x == 1300:
                                    pygame.mixer.Channel(51).play(pygame.mixer.Sound("MUSICA/SONIDO_BOWSER.wav"))
                                    pygame.mixer.Channel(51).set_volume(.15)

                                if PROYECTIL3_10.rect.x <= 130:
                                    PROYECTIL3_10.rect.x = 130
                                    mov_projects = False
                                    mov_der_bow_fb1 = True

                                if PROYECTIL3_10.rect.x == 130:
                                    pygame.mixer.Channel(57).play(pygame.mixer.Sound("MUSICA/REBOTE.wav"))
                                    pygame.mixer.Channel(57).set_volume(.15)

                                if PROYECTIL3_11.rect.x <= 130:
                                    PROYECTIL3_11.rect.x = 130
                                    mov_projects = False
                                    mov_der_bow_fb2 = True

                                if PROYECTIL3_12.rect.x <= 130:
                                    PROYECTIL3_12.rect.x = 130
                                    mov_projects = False
                                    mov_der_bow_fb3 = True

                                if mov_der_bow_fb1 == True:
                                    PROYECTIL3_10.rect.x += 30

                                if mov_der_bow_fb2 == True:
                                    PROYECTIL3_11.rect.x += 30
                                    PROYECTIL3_11.rect.y -= 6

                                if mov_der_bow_fb3 == True:
                                    PROYECTIL3_12.rect.x += 30
                                    PROYECTIL3_12.rect.y += 6

                        if RELOJ_BATALLAFINAL.rect.x >= 1350:
                            if ver31 == True:
                                if PROYECTIL3_10.rect.colliderect(BOSS3_FINAL.rect):
                                    ver30 = False
                                    ver_boss3_vivo = False
                                    screen.blit(BUM3.image, BOSS3_FINAL.rect)
                                    pygame.mixer.Channel(50).play(pygame.mixer.Sound("MUSICA/POW.wav"))
                                    pygame.mixer.Channel(50).set_volume(.15)
                                    pygame.mixer.Channel(58).play(pygame.mixer.Sound("MUSICA/BOWSER_MURIENDO.wav"))
                                    pygame.mixer.Channel(58).set_volume(.15)
                                    ver31 = False

                        if RELOJ_BATALLAFINAL.rect.x >= 1360:
                            screen.blit(BOSS3_MUERTO.image, BOSS3_MUERTO.rect)
                            BOSS3_MUERTO.rect.x += 3

                        if RELOJ_BATALLAFINAL.rect.x >= 1430:
                            if ver_nubes2 == True:
                                screen.blit(NUBE, [80,210])
                                screen.blit(NUBE, [80,17])
                                screen.blit(NUBE, [80,387])

                        if RELOJ_BATALLAFINAL.rect.x >= 1435:
                            ver_nubes2 = False
                            ver_flappys_gigantes = False
                            screen.blit(Flappy13.image, Flappy13.rect)
                            Flappy13.Movimiento_Pajaro(event)

                        if RELOJ_BATALLAFINAL.rect.x >= 1445:
                            Flappy13.rect.x += 10
                            if Flappy13.rect.x >= 640:
                                Flappy13.rect.x = 640

                        if RELOJ_BATALLAFINAL.rect.x == 1450:
                            mixer.music.load("MUSICA/END.wav")
                            mixer.music.set_volume(.03)
                            mixer.music.play(-1)

                        if RELOJ_BATALLAFINAL.rect.x >= 1620:
                            if ver_victoria == True:
                                screen.blit(corneta_izq,[100,0])
                                screen.blit(corneta_izq,[100,300])
                                screen.blit(corneta_der,[950,0])
                                screen.blit(corneta_der,[950,300])
                                victory = pygame.transform.smoothscale(victory,[586,204])
                                screen.blit(victory, [355, 100])
                                royale = pygame.transform.smoothscale(royale,[586,204])
                                screen.blit(royale, [370, 275])

                        if RELOJ_BATALLAFINAL.rect.x >= 1820:
                            screen.blit(bg_5,[0,0])
                            screen.blit(Flappy1_fin.image, Flappy1_fin.rect)
                            Flappy1_fin.Movimiento_Pajaro(event)
                            screen.blit(Flappy2_fin.image, Flappy2_fin.rect)
                            Flappy2_fin.Movimiento_Pajaro(event)
                            screen.blit(Flappy3_fin.image, Flappy3_fin.rect)
                            Flappy3_fin.Movimiento_Pajaro(event)
                            Flappy1_fin.rect.x += 10
                            Flappy2_fin.rect.x += 10
                            Flappy3_fin.rect.x += 10
                            if RELOJ_BATALLAFINAL.rect.x == 1820:
                                mixer.music.load("MUSICA/CAMPANERAS.wav")
                                mixer.music.set_volume(.06)
                                mixer.music.play(-1)

                        if RELOJ_BATALLAFINAL.rect.x == 1955:
                            mixer.music.load("MUSICA/FINITO.wav")
                            mixer.music.set_volume(.10)
                            mixer.music.play(-1)
                        if RELOJ_BATALLAFINAL.rect.x >= 1955:
                            screen.blit(theend,[350,100])
                        if RELOJ_BATALLAFINAL.rect.x == 2043:
                            pygame.quit()
                            sys.exit()



            if VIDAS == 0:
                screen.blit(game_over,[0,0])
                mixer.music.load("MUSICA/MUSICA_GAME_OVER.wav")
                mixer.music.set_volume(.03)
                mixer.music.play(-1)


        if NIVEL == 1:
            texto_marcador = FONT.render("Vidas:"+str(VIDAS), True, color_negro)
            texto_marcador_rect = texto_marcador.get_rect()
            texto_marcador_rect.center = screen_rect.center
            text_x = texto_marcador_rect[0]
            if VIDAS < 10:
                screen.blit(FONDO_VIDAS1p,[-38,-10])
                screen.blit(texto_marcador, [5, 0, 176, 21])
            if VIDAS >= 10:
                screen.blit(FONDO_VIDAS1g,[-38,-10])
                screen.blit(texto_marcador, [5, 0, 176, 21])
        if NIVEL == 2:
            texto_marcador = FONT.render("Vidas:"+str(VIDAS), True, color_negro)
            texto_marcador_rect = texto_marcador.get_rect()
            texto_marcador_rect.center = screen_rect.center
            text_x = texto_marcador_rect[0]
            if VIDAS < 10:
                screen.blit(FONDO_VIDAS2p,[-38,-10])
                screen.blit(texto_marcador, [5, 0, 176, 21])
            if VIDAS >= 10:
                screen.blit(FONDO_VIDAS2g,[-38,-10])
                screen.blit(texto_marcador, [5, 0, 176, 21])
        if NIVEL == 3:
            texto_marcador = FONT.render("Vidas:"+str(VIDAS), True, color_negro)
            texto_marcador_rect = texto_marcador.get_rect()
            texto_marcador_rect.center = screen_rect.center
            text_x = texto_marcador_rect[0]
            if VIDAS < 10:
                screen.blit(FONDO_VIDAS3p,[-38,-10])
                screen.blit(texto_marcador, [5, 0, 176, 21])
            if VIDAS >= 10:
                screen.blit(FONDO_VIDAS3g,[-38,-10])
                screen.blit(texto_marcador, [5, 0, 176, 21])

        if NIVEL == 4:
            texto_marcador = FONT.render("Vidas:"+str(VIDAS), True, color_negro)
            texto_marcador_rect = texto_marcador.get_rect()
            texto_marcador_rect.center = screen_rect.center
            text_x = texto_marcador_rect[0]
            if VIDAS < 10:
                screen.blit(FONDO_VIDAS4p,[-38,-10])
                screen.blit(texto_marcador, [5, 0, 176, 21])
            if VIDAS >= 10:
                screen.blit(FONDO_VIDAS4g,[-38,-10])
                screen.blit(texto_marcador, [5, 0, 176, 21])




        pygame.display.flip()
        clock.tick(FPS30)
