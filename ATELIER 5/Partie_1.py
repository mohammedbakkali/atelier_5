class Vecteur2D :
    def __init__(self,x=0,y=0):
       self.x=x
       self.y=y
    def dispaly(self):
        print(self.x,self.y)
    def addition(self,p1,p2):
        self.x=p1.x+p2.x
        self.y=p1.y+p2.y
        return self 

class Rectongle:
    nom ="rectangle"
    def __init__(self,L=0,H=0):
        self.L=L
        self.H=H
    def surface(self,x,y):
        s=x*y
        return s     
    def afficher(self,s):
        print("la surface = ",s)

class carre(Rectongle):
    nom ="carre"
#calcule du surface 
R = Rectongle()
s = R.surface(4,5)
R.afficher(s)
#declaration d'instance de calss caree 
carre1=carre()
print(carre1.nom)
#declaration d'instance de calss Rectongle 
Rectongle1=Rectongle()
print(Rectongle1.nom)





