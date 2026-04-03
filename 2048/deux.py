from random import randint
from random import *

grille = [[0,2,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
shuffle(grille[0])
shuffle(grille)
print(grille)

def bouger(sens,grille):
    for _ in range(sens):
        c1,c2,c3,c4 = grille[0][0],grille[0][1],grille[0][2],grille[0][3]
        c5,c6,c7,c8 = grille[1][3],grille[2][3],grille[3][3],grille[3][2]
        c9,c10,c11,c12 = grille[3][1],grille[3][0],grille[2][0],grille[1][0]
        c13,c14,c15,c16 = grille[1][1],grille[1][2],grille[2][2],grille[2][1]

        grille[0][3],grille[1][3],grille[2][3],grille[3][3] = c1,c2,c3,c4
        grille[3][2],grille[3][1],grille[3][0],grille[2][0] = c5,c6,c7,c8
        grille[1][0],grille[0][0],grille[0][1],grille[0][2] = c9,c10,c11,c12
        grille[1][2],grille[2][2],grille[2][1],grille[1][1] = c13,c14,c15,c16

    for _ in range(4):
        for i2 in range(3):
            for i in range(4):
                if grille[i][i2+1] == grille[i][i2] and grille[i][i2] != 0 and grille[i][i2]%2 == 0:
                    grille[i][i2+1] = 2*grille[i][i2+1]+1
                    grille[i][i2] = 0
                elif grille[i][i2+1] == 0:
                    u = grille[i][i2]
                    grille[i][i2] = 0
                    grille[i][i2+1] = u


    for i2 in range(4):
        for i in range(4):
            if grille[i][i2]%2 == 1:
                grille[i][i2] = grille[i][i2]-1


                """
                00 01 02 03
                10 11 12 13
                20 21 22 23
                30 31 32 33
                """


    for _ in range(4-sens):

        c1,c2,c3,c4 = grille[0][0],grille[0][1],grille[0][2],grille[0][3]
        c5,c6,c7,c8 = grille[1][3],grille[2][3],grille[3][3],grille[3][2]
        c9,c10,c11,c12 = grille[3][1],grille[3][0],grille[2][0],grille[1][0]
        c13,c14,c15,c16 = grille[1][1],grille[1][2],grille[2][2],grille[2][1]


        grille[0][3],grille[1][3],grille[2][3],grille[3][3] = c1,c2,c3,c4
        grille[3][2],grille[3][1],grille[3][0],grille[2][0] = c5,c6,c7,c8
        grille[1][0],grille[0][0],grille[0][1],grille[0][2] = c9,c10,c11,c12
        grille[1][2],grille[2][2],grille[2][1],grille[1][1] = c13,c14,c15,c16
    return grille

def jouer():

    en_jeu = True
    while en_jeu:
        print("---------------------------------------------------")
        for i in range(4):
            print(grille[i][0],"   ",grille[i][1],"   ",grille[i][2],"   ",grille[i][3])
        print("---------------------------------------------------")

        r = input()
        if r == "*":
            en_jeu = False
        if r == "z":
            bouger(1)
        if r == "q":
            bouger(2)
        if r == "s":
            bouger(3)
        if r == "d":
            bouger(0)
        if r in ["z","q","s","d","start"]:
            k = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
            while len(k) > 1:
                o = randint(0,len(k))
                if grille[(o//4)-1][(o%4)-1] == 0 :
                    grille[(o//4)-1][(o%4)-1] = 2**randint(1,2)
                    k = [0]
                    print("2")
                else:
                    k.pop(o-1)
                    print("3",k)
            print(k)
            if k == [] or r == "start":
                print("FIN")
                en_jeu = False
