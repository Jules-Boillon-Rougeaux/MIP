import pygame
from random import randint
root = "Car dodge tomatoes/images/"
class bonhomme:

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.sens = 0 # 0 haut 1 bas 2 gauche 3 droite


    def déplacement(self,direction):
        if direction == "droite":
            self.x += 20
            self.sens = 3

        elif direction == "gauche":
            self.x -= 20
            self.sens = 2

        elif direction == "haut":
            self.y -= 50
            self.sens = 0

        elif direction == "bas":
            self.y += 50
            self.sens = 1


pygame.init()
windows = pygame.display.set_mode((800,450))
windows.fill((227,222,165))
# Importation des images
tomate = pygame.transform.scale(pygame.image.load(root+"tomate.png") ,(13*4,12*4))
route = pygame.image.load(root+"route.png")

voiture1 = pygame.transform.scale(pygame.image.load(root+"voiture1.png") ,(22*3,41*3))
voiture2 = pygame.transform.scale(pygame.image.load(root+"voiture2.png") ,(22*3,41*3))
voiture3 = pygame.transform.scale(pygame.image.load(root+"voiture3.png") ,(41*3,22*3))
voiture4 = pygame.image.load(root+"voiture4.png")

voiture = [voiture4,voiture4,voiture4,voiture4]
######
voit = bonhomme(0,16)
enJeu = True
i = 0
u = 0+16
######
windows.blit(voiture[voit.sens],(0,0))
pygame.display.update()
while enJeu:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            enJeu = False
        if event.type == pygame.KEYDOWN:
            """if event.key == pygame.K_LEFT:
                voit.déplacement("gauche") 
            if event.key == pygame.K_RIGHT:
                voit.déplacement("droite")"""
            if event.key == pygame.K_UP:
                voit.déplacement("haut") 
            if event.key == pygame.K_DOWN:
                voit.déplacement("bas") 
    if i%10 == 0:          
        windows.blit(route,(0,0))
        windows.blit(voiture[voit.sens],(voit.x,voit.y))
        windows.blit(tomate,(900-i*0.2,u))
        if i == 5000:
            i = 0
            u = randint(1,5)* 50 + 16
    i+= 1
    pygame.display.update()
#end
pygame.quit()