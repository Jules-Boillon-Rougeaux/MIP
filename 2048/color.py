import pygame

pygame.init()

def exa(nb):
    r = 0
    g = 210
    b = 0
    
    for i in range(nb%21):
        if g > 0:
            g -= 30
            b += 30
        elif b > 0:
            b -= 30
            r += 30
        else:
            r -= 30
            g += 30
    
    rgb = (r,g,b)
    print(rgb)
    return rgb


def principale ():
    surface = pygame.display.set_mode((592,592))
    surface.fill(exa(0))
    pygame.display.set_caption("2048")

    pygame.display.update()
    x,y = 0,0
    i = 0
    
    """
    font = font.SysFont(None, 24)
    img = font.render('hello', True, BLUE)
    screen.blit(img, (20, 20))"""
    
    
    
    
    en_jeu = True
    pygame.display.update()
    while en_jeu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                en_jeu = False
            if event.type==pygame.MOUSEBUTTONUP:
                if event.button == 1 :
                    (x,y) = pygame.mouse.get_pos(x,y)
                    print (x, 'x', y, 'y')
                    surface.fill(exa(i))
                    pygame.display.update()
                    i+= 1


    pygame.quit()
principale()