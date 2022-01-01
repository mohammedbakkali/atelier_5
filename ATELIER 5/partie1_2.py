class Point:
    def __init__(self,x=0.0,y=0.0):
        self.x = x
        self.y = y

class Segment:
    orig=Point()
    extrem=Point()
    def __init__(self,x,y,z,t):
       self.orig.x=x
       self.orig.y=y
       self.extrem.z=z
       self.extrem.t=t
    def afficher(self):
        print("l'origine : (%f,%f) "%(self.orig.x,self.orig.y))
        print("l'extremite : (%f,%f)"%(self.extrem.z,self.extrem.t))

#auto test
a=Segment(1,2,3,4)
a.afficher()