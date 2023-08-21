#Classe Medicamentos
class Medicamentos:
    #Estrutura baseando em lista
    __medicamentos = []
    
    def __init__(self,nome,principal_composto,laboratorio,descricao):
        self.nome = nome
        self.principal_composto = principal_composto
        self.laboratorio = laboratorio
        self.descricao = descricao

    #Getters
    def getNome(self):
       return self.nome

    def getLaboratorio(self):
       return self.laboratorio

    def getDescricao(self):
       return self.descricao 

    #Funções estáticas de manipualação da estrutura de dados
    @classmethod
    def cadastrarMedicamento(cls,nome,principal_composto,laboratorio,descricao):
        novoMedicamento = cls(nome,principal_composto,laboratorio,descricao)
        cls.adicionarMedicamentos(novoMedicamento)
        print(f'Medicamento {nome} cadastrado')

    @classmethod
    def adicionarMedicamentos(cls, object):
        cls.__medicamentos.append(object)

    @classmethod
    def mostrarMedicamentos(cls):
        for medicamento in cls.__medicamentos:
            print(vars(medicamento))

   #Busca de medicamento baseado no nome ou laboratório do medicamento 
    @classmethod
    def buscarMedicamento(cls, key):
        result = []

        for medicamento in cls.__medicamentos:
            if(medicamento.getNome() == key or medicamento.getLaboratorio() == key):
                result.append(medicamento)
            if key in medicamento.getDescricao():
                result.append(medicamento)
        return result