
class Animal():
    def __init__(self,id,name,age,tür):
        self.id = id
        self.name = name
        self.age = age
        self.tür = tür

    def bigi_goster(self):
        print("==================================HAYVANLAR SINIFI============================================")
        print("**ID : {}\n**Name : {}\n**Age : {}\n**Tür : {} \n ".format(self.id,self.name,self.age,self.tür))


class Köpekler(Animal):
    def __init__(self,id,name,age,tür,cins):
        super().__init__(id,name,age,tür)
        self.cins = cins

    def bigi_goster(self):
        print("==================================KÖPEKLER SINIFI============================================")
        print("**ID : {}\n**Name : {}\n**Age : {}\n**Tür : {}\nCins : {}\n  ".format(self.id,self.name,self.age,self.tür,self.cins))

class Atlar(Animal):
    def __init__(self,id,name,age,tür,cins):
        super().__init__(id,name,age,tür)
        self.cins = cins

    def bigi_goster(self):
        print("==================================ATLAR SINIFI============================================")
        print("**ID : {}\n**Name : {}\n**Age : {}\n**Tür : {}\nCins : {}\n  ".format(self.id,self.name,self.age,self.tür,self.cins))

animals=Animal("1234","ÇOMİ","2","Köpek")
kopek1=Köpekler("2525","Alex","3","Köpek","Golden")
at1=Atlar("36369","GÜLBATUR","4","AT","Arap Atı")

animals.bigi_goster()
kopek1.bigi_goster()
at1.bigi_goster()