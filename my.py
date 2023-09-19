import os
os.system("cls")
class comp:
    def __init__(self,nom,narx,xotira,vkard,zOt,zIt):
       self.nom=nom
       self.narx=narx
       self.xotira=xotira
       self.vkard=vkard
       self.zOt=zOt
       self.zIt=zIt
    def show(self):
        print(f"komuter nomi - {self.nom}")
        print(f"narxi - {self.narx}")
        print(f"xotirasi - {self.xotira}")
        print(f"video karta - {self.vkard}")
        print(f"zaryadga {self.zOt} vaqtda toladi")
        print(f"zaryadi {self.zIt} soatga yetadi")
n=str(input("nomi= "))
na=int(input("narxi = "))
x=int(input("xotira= "))
vk=int(input("video karta = "))
zOt=int(input("qancha vaqtda zaryadi 100 boladi = "))
zIt=int(input("100 fozi necha soatga yetadi = "))
os.system("cls")
komp=comp(n,na,x,vk,zOt,zIt)
komp.show()