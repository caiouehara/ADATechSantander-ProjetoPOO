#Injeção de dependências

class ContaCorrente:
    def __init__(self, saldo):
        self.saldo = saldo

class ContaBancária:
    def __init__(self, contaCorrente: type(ContaCorrente)) -> None:
        self.__contaCorrente = contaCorrente

