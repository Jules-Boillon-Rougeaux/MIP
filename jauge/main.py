import pygame
from random import randint

root = 'marche/'
pygame.init()


def jauge(surface, x, contour = 5, eppaisseur = 10):
    pygame.draw.rect(surface, (0, 0, 0), (200, 300, x, contour*2+eppaisseur))
    pygame.draw.rect(surface, (255,255,255), (200+contour, 300+contour, x-2*contour, eppaisseur))
    r = randint(20,80)
    r2 = randint(10, x-r-contour)
    pygame.draw.rect(surface, (100,200,100), (200+contour+r2, 300+contour, r, eppaisseur))

def start():
    surface = pygame.display.set_mode((800,600))
    surface.fill((255,255,255))
    pygame.display.set_caption("Jauge simulator")
    
    enJeu = True
    x_bal = 400
    while enJeu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                enJeu = False
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 :
                    x_bal,y_bal = pygame.mouse.get_pos()
                    print (x_bal, 'x', y_bal, 'y')
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            if x_bal > 208:
                x_bal -= 0.2
                
        x_bal += 0.1
        surface.fill((255,255,255))
        jauge(surface, 200)

        pygame.display.update()
        
start()
pygame.quit()