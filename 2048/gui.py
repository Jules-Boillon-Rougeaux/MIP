import pygame
from random import randint
import deux as dqh
import copy


root = "2048/ressource/"
pygame.init()

def lancement():

    global surface
    global table
    global num
    global place
    global grille

    surface = pygame.display.set_mode((592+128+16,592))
    surface.fill((255,255,255))
    pygame.display.set_caption("2048")



    grille = pygame.image.load(root+'grille.png')
    n0 = pygame.image.load(root+'0.png')
    n2 = pygame.image.load(root+'2.png')
    n4 = pygame.image.load(root+'4.png')
    n8 = pygame.image.load(root+'8.png')
    n16 = pygame.image.load(root+'16.png')
    n32 = pygame.image.load(root+'32.png')
    n64 = pygame.image.load(root+'64.png')
    n128 = pygame.image.load(root+'128.png')
    n256 = pygame.image.load(root+'256.png')
    n512 = pygame.image.load(root+'512.png')
    n1024 = pygame.image.load(root+'1024.png')
    n2048 = pygame.image.load(root+'2048.png')
    num = [n0,n2,n4,n8,n16,n32,n64,n128,n256,n512,n1024,n2048]

    place = [[16,16],[16,160],[16,304],[16,448],[160,16],[160,160],[160,304],[160,448],[304,16],[304,160],[304,304],[304,448],[448,16],[448,160],[448,304],[448,448]]

############  PLACER  ############

    surface.blit(grille,(0,0))
    table = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

##################################

    pygame.display.update()
    principale(table)



def principale (table):
    loose = pygame.image.load(root+'loose.png')
    en_jeu = True
    e = 0
    touche = 1
    x,y = 0,0
    verif = 0
    pygame.display.update()
    while en_jeu:
        if touche == 1:
            for i in range(len(table)):
                if 0 in table[i]:
                    ok = 1
            if ok == 1 :
                while touche == 1:
                    t,p = randint(0,3),randint(0,3)
                    if table[t][p] == 0:
                        a = randint (1,10)
                        if a < 10 :
                            table[t][p] = 2**(1) # nombres de la case en plus
                        else :
                            table[t][p] = 2**(2)
                        touche = 0
                        ok = 0

            else :
                print("mvt impossible")

            for o in range(4):
                for i in range (4):
                    for u in range(len(num)):
                        if table[o][i] == 2**u:
                            surface.blit(num[u],(place[i+o*4][1],place[i+o*4][0]))
                        if table[o][i] == 0:
                            surface.blit(num[0],(place[i+o*4][1],place[i+o*4][0]))
            print(table,"table")
            touche = 0
            pygame.display.update()
        if verif == 1 :
            table3 = copy.deepcopy(table)
            v1 = dqh.bouger(1,table3)
            table3 = copy.deepcopy(table)
            v2 = dqh.bouger(2,table3)
            table3 = copy.deepcopy(table)
            v3 = dqh.bouger(3,table3)
            table3 = copy.deepcopy(table)
            v0 = dqh.bouger(0,table3)
            if v1 == v2 and v1 == v3 and v1 == v0 :
                print('perdu, pour reset, appuyez sur "r" ')
                verif = 2
                surface.blit(loose,(256-32-64,256-32))
                pygame.display.update()
            else :
                verif = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                en_jeu = False

            if event.type==pygame.MOUSEBUTTONUP:
                if event.button == 1 :
                    (x,y) = pygame.mouse.get_pos()
                    print (x, 'x', y, 'y')
                    if e == 1 :
                        if 16 <= x <= 166 and 150 <= y <= 316 :
                            print("click case 1")
                            case = 1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q or event.key == pygame.K_LEFT:
                    print("gauche")
                    table2 = copy.deepcopy(table)
                    table = dqh.bouger(2,table)
                    if table == table2:
                        pass
                    else :
                        touche = 1
                        verif = 1
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    print("droite")
                    table2 = copy.deepcopy(table)
                    table = dqh.bouger(0,table)
                    if table == table2:
                        pass
                    else :
                        touche = 1
                        verif = 1
                if event.key == pygame.K_z or event.key == pygame.K_UP:
                    print("haut")
                    table2 = copy.deepcopy(table)
                    table = dqh.bouger(1,table)
                    if table == table2:
                        pass
                    else :
                        touche = 1
                        verif = 1
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    print("bas")
                    table2 = copy.deepcopy(table)
                    table = dqh.bouger(3,table)
                    if table == table2:
                        pass
                    else :
                        touche = 1
                        verif = 1


                if event.key == pygame.K_r :
                    table = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
                    table = [[0,2,8,16],[32,64,128,256],[512,1024,2048,2],[4,8,16,32]]
                    surface.blit(grille,(0,0))
                    touche = 1



    pygame.quit()
lancement()