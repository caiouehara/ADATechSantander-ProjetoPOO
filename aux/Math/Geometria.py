class Retângulo:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b

class Círculo:
    def __init__(self, r):
        self.r = r
        self.pi = 3.14
    
    def area(self):
        return self.pi * r^2 

class Quadrado(Retângulo):
    def __init__(self, a):
        super.__init__(a, a)

class Triângulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
