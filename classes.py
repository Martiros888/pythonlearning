class Human():
    """
    my first class
    """ 
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def PrintName(self):
        print(self.name)

    def PrintAge(self):
        print(self.age)

class Man(Human):
    def __init__(self,name,age,maleOrFemale):
        self.maleOrFemale = maleOrFemale
    
    def PrintMale(self):
        print(self.maleOrFemale)
        


man = Man('Martiros',17,'txa')
man.PrintMale()