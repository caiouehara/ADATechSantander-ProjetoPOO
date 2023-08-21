#Classe laboratório
class Laboratórios:
    #Estrutura de dados laboratório
    __laboratórios = []

    def __init__(self,nome ,endereço ,telefone ,cidade ,estado):
        self.nome = nome
        self.endereço = endereço
        self.telefone = telefone
        self.cidade = cidade
        self.estado = estado

    #Funções de manipuação da estrutura de dados
    @classmethod
    def buscarLaboratório(cls, key):
        result = []

        for laboratório in cls.__laboratórios:
            if(laboratório.getNome() == key):
                result.append(laboratório)
        return result

    @classmethod
    def adicionarLaboratório(cls, object):
        cls.__laboratórios.append(object)

    @classmethod
    def cadastroLaboratório(cls, nome, endereço, telefone, cidade, estado):
        novoLaboratório = cls(nome, endereço, telefone, cidade, estado)
        cls.adicionarLaboratório(novoLaboratório)

    #Getters
    def getNome(self):
        return self.nome