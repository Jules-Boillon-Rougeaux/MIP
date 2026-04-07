#################### Importation des paquets
import pygame
import Dame_class as D
#################### Initialiser pygame

pygame.init()
root = 'dame/ressource/'

########################### Début du programme
def lancement(taille):    
    enJeu = True
    selected = ""
    surface = pygame.display.set_mode((taille*12,taille*12)) # Taille
    surface.fill((160,100,20))
    pygame.display.set_caption("Dame") # Nom de la page
    # importation des images
    BG         = pygame.transform.scale( pygame.image.load(root + 'BG.png')         ,(taille*12,taille*12))
    noire      = pygame.transform.scale( pygame.image.load(root + 'noire.png')      ,(taille,taille))
    blanc      = pygame.transform.scale( pygame.image.load(root + 'blanc.png')      ,(taille,taille))
    Dnoire     = pygame.transform.scale( pygame.image.load(root + 'Dnoire.png')     ,(taille,taille))
    Dblanc     = pygame.transform.scale( pygame.image.load(root + 'Dblanc.png')     ,(taille,taille))
    case_noire = pygame.transform.scale( pygame.image.load(root + 'case_noire.png') ,(taille,taille))
    case_blanc = pygame.transform.scale( pygame.image.load(root + 'case_blanc.png') ,(taille,taille))
    select     = pygame.transform.scale( pygame.image.load(root + 'select.png')     ,(taille,taille))
    bouge      = pygame.transform.scale( pygame.image.load(root + 'bouge.png')      ,(taille,taille))
    bouge2     = pygame.transform.scale( pygame.image.load(root + 'bouge2.png')     ,(taille,taille))
############################ Place des pions
    pions = []
    coord = []
    for i in range(10):
        pions.append(D.pions("n",(i+1)%2,i))
        pions.append(D.pions("n",(i+1)%2+2,i))
        
    for i in range(10):
        pions.append(D.pions("b",(i+1)%2+6,i))
        pions.append(D.pions("b",(i+1)%2+8,i))
   
    for i in range(len(pions)):
        coord.append([pions[i].posx,pions[i].posy])
############################ Reste
    #surface.blit(BG,(0,0))
    
    pygame.display.update()
    while enJeu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                enJeu = False
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 :
                    x,y = pygame.mouse.get_pos()
                    if -1 < (x//taille-1) <10 and -1 < (y//taille-1) < 10:
                        x,y = x//taille-1, y//taille-1
                        print ("Case :",y,x,'LC')
                    
                    ##### Plateau
                    for i2 in range(10):
                        for i in range(5):
                            if (i2)%2 == 0:
                                surface.blit(case_blanc,(taille*2*i+taille,taille*(i2)+taille))
                                surface.blit(case_noire,(taille*2*i+taille+taille,taille*i2+taille))
                            else:
                                surface.blit(case_blanc,(taille*2*i+taille+taille,taille*i2+taille))
                                surface.blit(case_noire,(taille*2*i+taille,taille*(i2)+taille))
                    ##### Placer les pions
                    for p in pions:
                        if p.couleur == "n":
                            if p.dame == 0:
                                surface.blit(noire,(p.posy*taille+taille,p.posx*taille+taille))
                            else:
                                surface.blit(Dnoire,(p.posy*taille+taille,p.posx*taille+taille))

                        elif p.couleur == "b":
                            if p.dame == 0:
                                surface.blit(blanc,(p.posy*taille+taille,p.posx*taille+taille))
                            else:
                                surface.blit(Dblanc,(p.posy*taille+taille,p.posx*taille+taille))

                    ##### Select
                    if [y,x] in coord:
                        p = pions[coord.index([y,x])]
                        surface.blit(select,(taille*x+taille,taille*y+taille))
                        p.voisin(coord,pions)
                        if p.voisin1 == "v":
                            surface.blit(bouge,(taille*x,taille*y))
                        elif p.voisin1 == p.couleur:
                            surface.blit(bouge2,(taille*x,taille*y))
                        if p.voisin2 == "v":
                            surface.blit(bouge,(taille*x,taille*y+2*taille))
                        if p.voisin3 == "v":
                            surface.blit(bouge,(taille*x+2*taille,taille*y))
                        if p.voisin4 == "v":
                            surface.blit(bouge,(taille*x+2*taille,taille*y+2*taille))
                            
                        selected = p.couleur
                    
                    selected = ""
                    pygame.display.update()
##################################################"

lancement(64)
pygame.quit()
