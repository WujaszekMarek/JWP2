import math
class Vector3D:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"Vector3D({self.x}, {self.y}, {self.z})"

    def setValue(self):
        self.x=int(input("Podaj x:"))
        self.y = int(input("Podaj y:"))
        self.z = int(input("Podaj z:"))

    def showValue(self):
        print(f"Wartosci: [{self.x}, {self.y}, {self.z}]")

    def norm(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y,self.z+other.z)
    def __sub__(self, other):
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self):
        skalar=int(input("Podaj wartosc skalara:"))
        return Vector3D(self.x*skalar,self.y*skalar,self.z*skalar)
    def dot(self,other):
        return self.x*other.x+self.y*other.y+self.z*other.z

    def cross(self,other):
        return Vector3D(self.y*other.z-self.z*other.y,self.z*other.x-self.x*other.z,self.x*other.y-self.y*other.x)

    @staticmethod
    def are_orthogonal(vector1,vector2):
        wynik=vector1.x*vector2.x+vector1.y*vector2.y+vector1.z*vector2.z
        if(wynik==0):
            return True
        else:
            return False

vector = Vector3D(1,2,3)
vector1 = Vector3D(2,2,2)
vector.setValue()
vector.showValue()
print(f"Długość: {vector.norm()}")
print(f"Suma: {vector.__add__(vector1)}")
print(f"Różnica: {vector.__sub__(vector1)}")
print(f"Mnożenie przez skalar: {vector.__mul__()}")
print(f"Iloczyn skalarny: {vector.dot(vector1)}")
print(f"Iloczyn wektorowy: {vector.cross(vector1)}")
print(f"Czy wektory są ortogonalne: {Vector3D.are_orthogonal(vector,vector1)}")
