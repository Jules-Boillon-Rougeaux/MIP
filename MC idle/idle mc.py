import pygame


root = 'MC idle/ressource/'
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(root+"musique.mp3")

pygame.mixer.music.play(-1)         # Pour lancer la musique infiniment
#pygame.mixer.music.set_volume(0.5)  # Pour le volume, entre 0.0 et 1.0

########################### Début du programme
def lancement(scoreM = 5, grille = [0]*12):   # scoreM = nombre de fois qu'il faut appuyer 
    enJeu = True
    bouger = True
    score = 0 
    select,select2 = 13,13
    surface = pygame.display.set_mode((600,600)) #taille
    surface.fill((50,0,140))
    pygame.display.set_caption("Idle MC") #nom de la page
    # importation des images
    b0 = pygame.image.load(root+'bouton/b0.png')
    b1 = pygame.image.load(root+'bouton/b1.png')
    b2 = pygame.image.load(root+'bouton/b2.png')
    b3 = pygame.image.load(root+'bouton/b3.png')
    b4 = pygame.image.load(root+'bouton/b4.png')
    b5 = pygame.image.load(root+'bouton/b5.png')
    bouton = [b0,b1,b2,b3,b4,b5]
    
    c = pygame.image.load(root+'img/c.png')
    c0 = pygame.image.load(root+'img/c0.png')
    c1 = pygame.image.load(root+'img/c1.png')
    c2 = pygame.image.load(root+'img/c2.png')
    c3 = pygame.image.load(root+'img/c3.png')
    c4 = pygame.image.load(root+'img/c4.png')
    c5 = pygame.image.load(root+'img/c5.png')
    case = [c0,c1,c2,c3,c4,c5]
    # Coordonnée de chaque case
    coCase = [[55,80],[185,80],[315,80],[445,80],[55,210],[185,210],[315,210],[445,210],[55,340],[185,340],[315,340],[445,340]]
    
    # On met les cases noire et la rouge
    for i in range(12):
        surface.blit(c0,coCase[i])
    surface.blit(bouton[score],(225,480))
    if select != 13:
        surface.blit(c,coCase[select])
    pygame.display.update()
    
    while enJeu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                enJeu = False
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 :
                    x,y = pygame.mouse.get_pos()
                    #print (x, 'x', y, 'y')
                    if 225 <= x <= 375 and 480 <= y <= 580 and score < scoreM:
                        score += 1
                        print(score,"oki")
                        
                    surface.fill((50,0,140))
                    for i in range(4):
                        surface.blit(c0,(130*i+55,80))
                        surface.blit(c0,(130*i+55,210))
                        surface.blit(c0,(130*i+55,340))
                    surface.blit(bouton[score],(225,480))
                    
                    for i in range(4):
                        if (55+130*i) <= x <= (155+130*i) and 80 <= y <= 180 :
                            select = i
                            print("case ",select)
                            surface.blit(c,((55+130*i),80))
                        elif (55+130*i) <= x <= (155+130*i) and 210 <= y <= 310 :
                            select = i+4
                            print("case ",select)
                            surface.blit(c,((55+130*i),210))
                        elif (55+130*i) <= x <= (155+130*i) and 340 <= y <= 440 :
                            select = i+8
                            print("case ",select)
                            surface.blit(c,((55+130*i),340))
                    
                    if select2 == 13: # pas encore assigner
                        select2 = select
                    elif grille[select] == grille[select2] and select != select2 and grille[select] != 0:
                        if grille[select] != (len(case)-1):
                            grille[select] += 1
                            grille[select2] = 0
                            select2 = 13
                            for i in range(4):
                                surface.blit(c0,(130*i+55,80))
                                surface.blit(c0,(130*i+55,210))
                                surface.blit(c0,(130*i+55,340))
                            surface.blit(bouton[score],(225,480))
                        else:
                            print("Vous avez atteint la limite pour le moment")
                    else:
                        select2 = select
                    if score == scoreM: 
                        for i in range(12):
                            if grille[i] == 0 and score == scoreM:
                                grille[i] = 1
                                score = 0
                        if score == scoreM:
                            print("Il n'y a plus de place")
                        

                    for i in range(4):
                        if grille[0+i] != 0:
                            surface.blit(case[grille[0+i]],(130*i+55,80))
                        if grille[4+i] != 0:
                            surface.blit(case[grille[4+i]],(130*i+55,210))
                        if grille[8+i] != 0:
                            surface.blit(case[grille[8+i]],(130*i+55,340))
                    pygame.display.update()    
    
lancement()
pygame.quit()