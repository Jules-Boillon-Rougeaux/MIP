import pygame
from random import randint
from time import sleep

root = 'click/ressource/'


pygame.init()
def debut():
    global surface
    y,u = 0,0
    surface = pygame.display.set_mode((600,600)) #taille
    pygame.display.set_caption("Idle click") #nom de la page
    title = pygame.image.load(root + 'ti.png')
    for i in range(25):
        y += 5
        if i%2 == 0:
            u = i
        surface.fill((10*u+5,10*u+5,10*u+5))
        surface.blit(title,(150,5*i+y))
        pygame.display.update()
        sleep(0.08)
    pygame.display.update()
    sleep(2)
        
    
def lancement():

    global surface
    global c_taille
    global c
    global r
    global xi
    global yi
    global score
    global niveau
    global logo
    global un
    global jauge
    global sr
    global s
    global s0
    global s1
    global s2
    global s3
    global s4
    global s5
    global s6
    global s7
    global s8
    global s9
    

    surface.fill((255,255,255))

    
    c1 = pygame.image.load(root + 'click.png')
    c2 = pygame.image.load(root + 'click2.png')
    r = pygame.image.load(root + 'r.png')
    un = pygame.image.load(root + '1.png')
    logo = pygame.image.load(root + 'logo.png')
    jauge = pygame.image.load(root + 'jauge.png')
    
    sr1 = pygame.image.load(root + 'score/s1.png')
    sr2 = pygame.image.load(root + 'score/s2.png')
    s0 = pygame.image.load(root + 'score/0.png')
    s1 = pygame.image.load(root + 'score/1.png')
    s2 = pygame.image.load(root + 'score/2.png')
    s3 = pygame.image.load(root + 'score/3.png')
    s4 = pygame.image.load(root + 'score/4.png')
    s5 = pygame.image.load(root + 'score/5.png')
    s6 = pygame.image.load(root + 'score/6.png')
    s7 = pygame.image.load(root + 'score/7.png')
    s8 = pygame.image.load(root + 'score/8.png')
    s9 = pygame.image.load(root + 'score/9.png')

    s = [s0,s1,s2,s3,s4,s5,s6,s7,s8,s9]
    c = [c1,c2]
    sr = [sr1,sr2]
    surface.blit(logo,(100,15))
    surface.blit(jauge,(20,20))
    pygame.display.update()
    principale()

def principale ():
    niveau = 0
    x,y = 0,0
    score = 0
    fin_partie = False
    xi,yi = randint(85,500),randint(130,500)
    surface.blit(c[0],(xi,yi))
    surface.blit(s0,(496,50))
    surface.blit(s0,(530,50))
    pygame.display.update()
    while fin_partie == False :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin_partie = True
                
            if event.type==pygame.MOUSEBUTTONUP:
                if event.button == 1 :
                    x,y = pygame.mouse.get_pos()
                    #print (x, 'x', y, 'y')
                    if xi <= x <= (xi+80) and yi <= y <= (yi+80) :
                        score += 1
                        print(score)
                        surface.blit(r,(xi,yi))
                        xi,yi = randint(85,500),randint(130,500)
                        surface.blit(un,(24,19 + score*5))
                        surface.blit(c[niveau],(xi,yi))

                    print("ok")
                    if score != 24:
                        surface.blit(sr[niveau],(530,50))
                        surface.blit(sr[niveau],(496,50))
                        surface.blit(s[score//10],(496,50))
                        surface.blit(s[score%10],(530,50))
                    pygame.display.update()

                        
                        

    pygame.quit()
    
debut()
lancement()