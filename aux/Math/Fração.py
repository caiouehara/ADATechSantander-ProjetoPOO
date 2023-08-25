class Fração:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador
    
    def __add__(FracaoA, FracaoB):
        if(FracaoA.denominador * FracaoB.denominador == 0): return
        return ((FracaoA.numerador * FracaoB.denominador) + (FracaoA.denominador * FracaoB.numerador))/ (FracaoA.denominador * FracaoB.denominador)

    def __sub__(FracaoA, FracaoB):
        if(FracaoA.denominador * FracaoB.denominador == 0): return
        return ((FracaoA.numerador * FracaoB.denominador) - (FracaoA.denominador * FracaoB.numerador))/ (FracaoA.denominador * FracaoB.denominador)

    def __mul__(FracaoA, FracaoB):
        if(FracaoA.denominador * FracaoB.denominador == 0): return
        return (FracaoA.numerador * FracaoB.numerador) / (FracaoA.denominador * FracaoB.denominador)

    def __truediv__(FracaoA, FracaoB):
        if(FracaoA.denominador * FracaoB.denominador == 0): return
        return (FracaoA.numerador * FracaoB.denominador) / (FracaoA.denominador * FracaoB.numerador)