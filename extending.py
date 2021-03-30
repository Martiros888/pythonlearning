class R():
    def __init__(self,r):
        self.r = r

class G():
    def __init__(self,g):
        self.g = g

class B():
    def __init__(self,b):
        self.b = b
        
class RGB(R,G,B):
    def __init__(self,r,g,b):
        self.r = r
        self.g = g
        self.b = b

    def Print(self):
        print(self.r,self.g,self.b)

a = RGB(10,10,10)

a.Print()
