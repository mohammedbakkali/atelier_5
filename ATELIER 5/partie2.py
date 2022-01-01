class Etudiant:
    def __init__(self,nom,prenom,age,cne,moyenne):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.cne = cne
        self.moyenne = moyenne
list = []
list.append(Etudiant("Mohammed","bakkali",22,586547,18))
list.append(Etudiant("Ali","abdoni",23,545457,15))
list.append(Etudiant("Rim","lakkel",10,244415,17)) 

for obj in list:
    print(obj.nom,obj.prenom)
def tri_abulle(list):
    n=len(list)                    
    permutation=True
    while(permutation==True): 
        permutation=False     
        for i in range(0,n-1):
            if list[i].moyenne<list[i+1].moyenne:
                tmp=list[i]
                list[i]=list[i+1]
                list[i+1]=tmp
                permutation=True
    n=n-1 
tri_abulle(list)
for obj in list:
    print(obj.nom,obj.prenom,obj.age,obj.cne,obj.moyenne)    