#aux
from aux.Fração import Fração

#Módulos
from modulos.Laboratórios import Laboratórios
from modulos.Cliente import Cliente
from modulos.Menu import Menu
from modulos.Vendas import Vendas
from modulos.Medicamentos import Medicamentos
from modulos.MedicamentosQuimioterápicos import MedicamentosQuimioterápicos
from modulos.MedicamentosFitoterápicos import MedicamentosFitoterápicos

#Testes para codificação do programa
"""
Cliente.cadastrarCliente('44631113132', 'Caio', '13/09/2002')
Cliente.buscarCliente('44631113132')

Laboratórios.cadastroLaboratório('lab1', 'Rua Luigi Rosiello', '119707952', 'São Paulo', 'SP')
Laboratórios.cadastroLaboratório('lab2', 'Rua Enersto', '1321333', 'São José dos Campos', 'SP')

MedicamentosFitoterápicos.cadastrarMedicamento('Fisioterapico', 'componente1', Laboratórios.buscarLaboratório('lab1')[0], 'para dor nas costas')
MedicamentosQuimioterápicos.cadastrarMedicamento('Quimioterapico', 'componente2', Laboratórios.buscarLaboratório('lab1')[0], 'para cancer', True)
MedicamentosQuimioterápicos.cadastrarMedicamento('Quimioterapico2', 'componente2', Laboratórios.buscarLaboratório('lab2')[0], 'para cancer', True)
MedicamentosQuimioterápicos.cadastrarMedicamento('Quimioterapico2', 'componente2', Laboratórios.buscarLaboratório('lab1'), 'para cancer', True)
#Medicamentos.mostrarMedicamentos()

busca = Medicamentos.buscarMedicamento('para')
for resultado in busca:
    print(vars(resultado))

Vendas.realizarVenda('11/11/2023', Cliente.buscarCliente('44631113132'), Medicamentos.buscarMedicamento('Fisioterapico')[0], 200)
Vendas.realizarVenda('11/11/2023', Cliente.buscarCliente('44631113132'), Medicamentos.buscarMedicamento('Fisioterapico')[0], 200)
Vendas.realizarVenda('11/11/2023', Cliente.buscarCliente('44631113132'), Medicamentos.buscarMedicamento('Quimioterapico')[0], 200)
Vendas.realizarVenda('11/11/2023', Cliente.buscarCliente('44631113132'), Medicamentos.buscarMedicamento('Quimioterapico')[0], 200)
Vendas.realizarVenda('11/11/2023', Cliente.buscarCliente('44631113132'), Medicamentos.buscarMedicamento('Quimioterapico')[0], 200)
Vendas.realizarVenda('11/11/2023', Cliente.buscarCliente('44631113132'), Medicamentos.buscarMedicamento('Quimioterapico')[0], 200)
Vendas.mostrarVendas()
"""

#Função inicial
#Menu.create()

A = Fração(1, 2)
B = Fração(1, 3)
print(A + B)
print(A - B)
print(A * B)
print(A / B)