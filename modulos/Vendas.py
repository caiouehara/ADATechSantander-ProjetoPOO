
#Classe venda
class Vendas:
    __vendas = []

    def __init__(self, datastamp, cliente, produto_vendido, valor_total):
        self.datastamp = datastamp
        self.cliente = cliente
        self.produto_vendido = produto_vendido
        self.valor_total = valor_total

    #Função de manipulação da estrutura de dados
    @classmethod
    def realizarVenda(cls, datastamp, cliente, produto_vendido, valor_total):
        novaVenda = cls(datastamp, cliente, produto_vendido, valor_total)
        
        try: 
            if(produto_vendido.necessidade_receita):
                print(f'Atenção esse produto {produto_vendido.nome} precisa ser vendido com receita')
        except AttributeError:
            print()
        if(cliente.getAge() > 65):
            novaVenda = cls(datastamp, cliente, produto_vendido, valor_total * 0.80)
        if(valor_total > 150):
            novaVenda = cls(datastamp, cliente, produto_vendido, valor_total * 0.90)

        cls.__vendas.append(novaVenda)

    @classmethod
    def mostrarVendas(cls):
        for venda in cls.__vendas:
            print(vars(venda))

    #Getters
    @classmethod
    def getVendas(cls):
        return cls.__vendas   

    def getValor_Total(self):
        return self.valor_total 
    
    def getCliente(self):
        return self.cliente
