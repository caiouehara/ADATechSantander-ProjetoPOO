class Fração:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador
    
    def __add__(FracaoA, FracaoB):
        return ((FracaoA.numerador * FracaoB.denominador) + (FracaoA.denominador * FracaoB.numerador))/ (FracaoA.denominador * FracaoB.denominador)

