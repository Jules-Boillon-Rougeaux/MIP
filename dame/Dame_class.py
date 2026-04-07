class pions:
    
    def __init__(self,couleur,x,y):
        
        self.voisin1 = ""
        self.voisin2 = ""
        self.voisin3 = ""
        self.voisin4 = ""
        self.couleur = couleur
        self.posx = x
        self.posy = y
        self.dame = 0
        
    def bouger(self,mouv):
        if mouv == 1 and self.posx > 0 and self.posy > 0 :
            self.posx += -1
            self.posy += -1
        elif mouv == 2 and self.posx < 10 and self.posy > 0 :
            self.posx += 1
            self.posy += -1
        elif mouv == 3 and self.posx > 0 and self.posy < 10 :
            self.posx += -1
            self.posy += 1
        elif mouv == 4 and self.posx < 10 and self.posy < 10 :
            self.posx += 1
            self.posy += 1
 
    def voisin(self,co,pi):
        self.voisin1 = ""
        self.voisin2 = ""
        self.voisin3 = ""
        self.voisin4 = ""
        if self.posx > 0 and self.posy > 0 :
            self.voisin1 = "v"
            if [self.posx-1,self.posy-1] in co:
                self.voisin1 = ""
        if self.posx < 9 and self.posy > 0 :
            self.voisin2 = "v"
            if [self.posx+1,self.posy-1] in co:
                self.voisin2 = ""
        if self.posx > 0 and self.posy < 9 :
            self.voisin3 = "v"
            if [self.posx-1,self.posy+1] in co:
                self.voisin3 = ""
        if self.posx < 9 and self.posy < 9 :
            self.voisin4 = "v"
            if [self.posx+1,self.posy+1] in co:
                self.voisin4 = ""
