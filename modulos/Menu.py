#Bibliotecas importadas
import time
import sys
from datetime import datetime
from IPython.display import clear_output

#Módulos
from modulos.Laboratórios import Laboratórios
from modulos.Cliente import Cliente
from modulos.Vendas import Vendas
from modulos.Medicamentos import Medicamentos
from modulos.MedicamentosQuimioterápicos import MedicamentosQuimioterápicos
from modulos.MedicamentosFitoterápicos import MedicamentosFitoterápicos

class Menu:
    #constante do loop, para manter a atualização ou não
    __visualizacao = False
    apresentacao = f"---- Olá, bem-vindo ao Controle Farmaceutico ADA TECH ----"

    #Menu principal, onde contém os cadastro e acesso geral
    @classmethod
    def menu_principal(cls):
        print(f">> Escolha a operação desejada: ")
        print(f"""
                1. Cadastro de Cliente
                2. Cadastro de Medicamento
                3. Cadastro de Laboratório 
                4. Venda de Medicamento
                5. Emitir relatórios
                6. Sair
            """)
        time.sleep(1) #o delay ocorre para dar tempo de renderizar

        try:
            op = int(input(f"Qual opção você deseja?"))

            #Estrutura de opções do menu
            menu_opcoes = [cls.cadastrarCliente, cls.cadastrarMedicamento, cls.cadastrarLaboratório , cls.venderMedicamento, cls.menu_relatorios, cls.exit]
            menu_opcoes[op-1]() #-1 por conta do índice do array
            print("Realização feita com sucesso. Você deseja fazer outra operação?")
        except Exception as ex:
            cls.limparTela()
            print("Alguma coisa aconteceu de errado.... Tente novamente")
            print(f'ERROR: {ex}')
            print() 
            print("-----------------------------------------------------") 
        cls.menu_principal() 


    #Função cadastro laboratório
    @classmethod
    def cadastrarLaboratório(cls):    
        print("> Cadastro de Laboratório")

        nome =  input("Digite o nome do Laboratório: ")
        if(Laboratórios.buscarLaboratório(nome)):
            print("Laboratório já cadastrado")
            return
        else:
            novoLaboratório = (
                nome,
                input("Digite seu endereço: "),
                input("Digite seu telefone: "),
                input("Digite sua cidade: "),
                input("Digite seu estado: ")
            )
            nome, endereço, telefone, cidade, estado = novoLaboratório
            Laboratórios.cadastroLaboratório(nome, endereço, telefone, cidade, estado)

    @classmethod
    def exit(cls):
        print()
        print("-----> Programa encerrando....")
        sys.exit() 

    #Meu relatórios
    @classmethod
    def menu_relatorios(cls):
        print(f">> Área de Relatórios")
        print(f"""
                1. Medicamento mais vendido
                2. Quantidade de pessoas atendidas
                3. Número de remédios Quimioterápicos vendidos
                4. Número de remédio Fitoterápicos vendidos
              """)
        time.sleep(1)
        
        try:
            op = int(input(f"Qual opção você deseja?"))
            menu_opcoes = [cls.medicamentoMaisVendido, cls.quantidadePessoasAtendidas, cls.medicamentoQuimioterapicosVendidos, cls.medicamentoFitoterapicosVendidos]
            menu_opcoes[op-1]()
            print("Realização feita com sucesso. Você deseja fazer outra operação?")
        except Exception as ex:
            cls.limparTela()
            print("Alguma coisa aconteceu de errado.... Tente novamente")
            print(f'ERROR: {ex}')
            print() 
            print("-----------------------------------------------------") 
        cls.menu_principal() 

    @classmethod
    def quantidadePessoasAtendidas(cls):
        vendas = Vendas.getVendas()

        countList = []
        for venda in vendas:
            countList.append(venda.getCliente().getNome())

        result = dict(((i, countList.count(i)) for i in countList))

        print(f'O número de pessoas atendias foi {len(result)}')

    #Funções relatórios
    @classmethod
    def medicamentoMaisVendido(cls):
        vendas = Vendas.getVendas()
       
        countList = []
        for venda in vendas:
            countList.append(venda.produto_vendido.nome)

        result = dict(((i, countList.count(i)) for i in countList))
        max_value = max(result, key=result.get)

        sum = 0
        for venda in vendas:
            if(venda.produto_vendido.nome == max_value):
                sum += venda.valor_total 

        print(f'O medicamento mais vendido foi o {max_value} com {result[max_value]} unidades vendidas e valor total de {sum}')

    @classmethod
    def medicamentoQuimioterapicosVendidos(cls):
        vendas = Vendas.getVendas()
       
        countList = []
        sum = 0
        for venda in vendas:
            if(hasattr(venda.produto_vendido, 'necessidade_receita')):
                countList.append(venda.produto_vendido.nome)
                sum += venda.valor_total

        print(f'O número de medicamentos quimioterápicos vendidos foi {len(countList)} somando no total {sum}') 

    @classmethod
    def medicamentoFitoterapicosVendidos(cls):
        vendas = Vendas.getVendas()
       
        countList = []
        sum = 0
        for venda in vendas:
            if(not hasattr(venda.produto_vendido, 'necessidade_receita')):
                countList.append(venda.produto_vendido.nome)
                sum += venda.valor_total

        print(f'O número de medicamentos fitoterapicos vendidos foi {len(countList)} somando no total {sum}')   

    @classmethod
    def venderMedicamento(cls):
        print("> Venda de Medicamento")

        cpf = input("Digite seu CPF: ")
        cliente = Cliente.buscarCliente(cpf)
        if(not cliente):
            cls.cadastrarCliente()
        
        medicamento_nome = input("Digite o nome do Medicamento: ")
        medicamento = Medicamentos.buscarMedicamento(medicamento_nome)[0]
        if(not medicamento):
           cls.cadastrarMedicamento()

        valor_total = float(input("Digite o valor da venda: "))

        novaVenda = ( 
                datetime.today,
                cliente,
                medicamento,
                valor_total
        )

        datastamp, cliente, produto_vendido, valor_total = novaVenda
        Vendas.realizarVenda(datastamp, cliente, produto_vendido, valor_total)

    #Funções cadastro com visualização
    @classmethod
    def cadastrarMedicamento(cls):
        print("> Cadastro de Medicamento")

        medicamento_nome = input("Digite o nome do medicamento: ")
        laboratorio_nome = input("Digite o laborátorio: ")

        if(not Laboratórios.buscarLaboratório(laboratorio_nome)):
            cls.cadastrarLaboratório()
        laboratorio = Laboratórios.buscarLaboratório(laboratorio_nome)

        if(Medicamentos.buscarMedicamento(medicamento_nome)):
            print("Medicamento já cadastrado")
            return
        if(input("O medicamento precisa de receita (s/n)?") == "s"):
            novoMedicamento = (
                medicamento_nome,
                input("Qual é o principal composto? "),
                laboratorio,
                input("Descreva o medicamento: "), 
                True
            )
            nome, principal_composto, laboratorio, descricao, necessidade_receita = novoMedicamento
            MedicamentosQuimioterápicos.cadastrarMedicamento(nome, principal_composto, laboratorio, descricao, necessidade_receita)
        else:
            novoMedicamento = (
                medicamento_nome, 
                input("Qual é o principal composto? "),
                laboratorio,
                input("Descreva o medicamento: "), 
            )
            nome, principal_composto, laboratorio, descricao = novoMedicamento
            Medicamentos.cadastrarMedicamento(nome, principal_composto, laboratorio, descricao)

    @classmethod
    def cadastrarCliente(cls):
        print("> Cadastro de Cliente")

        cpf =  input("Digite seu CPF: ")
        if(Cliente.buscarCliente(cpf)):
            print("Usuário já cadastrado")
            return
        else:
            novoCliente = (
                cpf, 
                input("Digite seu nome: "), 
                input("Digite sua data de nascimento XX/XX/XXXX: ")
            )
            cpf, nome, data_nasc = novoCliente
            Cliente.cadastrarCliente(cpf, nome, data_nasc)

    #Funções auxiliares
    @classmethod
    def limparTela(cls):
        clear_output()

    @classmethod
    def __loop(cls):
        if(cls.__visualizacao):
            print(cls.apresentacao)
            cls.menu_principal()
            cls.__visualizacao = False

            cls.__loop()

    @classmethod       
    def create(cls):
        cls.__visualizacao = True
        cls.limparTela()
        cls.__loop()