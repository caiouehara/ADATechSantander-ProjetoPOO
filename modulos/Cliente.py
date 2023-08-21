#Bibliotecas importadas
from datetime import datetime
from IPython.display import clear_output
import time
import sys

#Classe cliente
class Cliente:
    #Estrutura de dados em base de lista
    __clientes = []
    
    def __init__(self, cpf,nome, data_nasc):
        self.__cpf = cpf
        self.__nome = nome
        self.__data_nasc = datetime.strptime(data_nasc, "%d/%m/%Y")

    #Getters
    def getCpf(self):
        return self.__cpf;

    def getData_Nasc(self):
        return self.__data_nasc;    

    def getAge(self):
        dateNow = datetime.today()
        age = (dateNow.year - self.__data_nasc.year)
        return age

    def getNome(self):
        return self.__nome 
    
    #Funções de manipulação da estrutuda de dados
    @classmethod
    def cadastrarCliente(cls, cpf, nome, data_nasc):
        novoCliente = Cliente(cpf, nome, data_nasc)
        cls.__clientes.append(novoCliente)
        
    @classmethod
    def mostrarClientes(cls):
        for cliente in cls.__clientes:
            print(vars(cliente))

    @classmethod
    def buscarCliente(cls, cpf):
        for cliente in cls.__clientes:
            #Busca pelo CPF
            if(cliente.getCpf() == cpf):
                return cliente
        # print(f'Cliente {cpf} NÃO encontrado')