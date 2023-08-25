import Banco.ContaCorrente as ContaCorrente

class ContaBancária:
    def __init__(self, contaCorrente: type(ContaCorrente)) -> None:
        self.__contaCorrente = contaCorrente
