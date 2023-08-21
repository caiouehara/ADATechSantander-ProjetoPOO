from modulos.Medicamentos import Medicamentos

#Classe especializada de medicamentos de quimioterápicos
class MedicamentosQuimioterápicos(Medicamentos):
    def __init__(self,nome,principal_composto,laboratorio,descricao, necessidade_receita):
        super().__init__(nome,principal_composto,laboratorio,descricao)
        self.necessidade_receita = necessidade_receita

    @classmethod
    def cadastrarMedicamento(cls, nome,principal_composto,laboratorio,descricao, necessidade_receita):
        novoMedicamento = cls(nome,principal_composto,laboratorio, descricao,necessidade_receita)
        Medicamentos.adicionarMedicamentos(novoMedicamento)
        print(f'Medicamento {nome} cadastrado')
