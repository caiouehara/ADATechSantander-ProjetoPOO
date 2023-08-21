from modulos.Medicamentos import Medicamentos

#Classe especializada de medicamentos de fitoterápicas
class MedicamentosFitoterápicos(Medicamentos):
    def __init__(self,nome,principal_composto,laboratorio,descricao):
        super().__init__(nome,principal_composto,laboratorio,descricao)