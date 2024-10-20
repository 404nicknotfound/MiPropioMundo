import pygame
import sys

pygame.init()

#definir colores

BLACK     = (  0,  0,  0)
WHITE     = (255,255,255)
RED       = (255,  0,  0)
GREEN     = (  0,255,  0)
BLUE      = (  0,  0,255)
BlUE_SKYE = (173,216,255)

#se configura la pantalla del juego... por lo regular todo se pone en ingles
size = (800,600)

nombre= "Mi Primer Juego" 
screen=pygame.display.set_mode(size)#esta linea lo que hace es: si le da las dimensiones de la ventana, como se identifica, porque se llama set_ todo lo que inicie por set quiere decir que vamos a sobreescribir y data argumentos a algo, esos son metodos estandar.... 
pygame.display.set_caption(nombre)

jugando=True

while jugando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando=False

    #color fondo de pantalla
    screen.fill(BlUE_SKYE)
    ### ---- ZONA DE DIBUJO
    pygame.draw.line(screen, GREEN, [750,100], [800,50], 5)
    pygame.draw.polygon(screen, BLACK, [(250,200),(300,300),(250,300),(200,300)], 5)

    ### ---- ZONA DE DIBUJO

    #Actualizacion de pantalla
    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
