from systemSimulator import *
from validators import validar_cpf, validar_nome, validar_data
from inputs import get_contaIdByUser, get_valor
from terminalFuncs import log


def option1():
    nome = input("Insira o nome: ")
    while not validar_nome(nome):
        nome = input("Insira um nome válido: ")
    
    CPF = input("Insira o CPF: ")
    while not validar_cpf(CPF):
        CPF = input("Insira um CPF válido: ")
    
    dataNas = input("Insira a data de nascimento: ")
    while not validar_data(dataNas):
        dataNas = input("Insira uma data de nascimento válida: ")
    
    endereco = input("Insira o endereço: ")

    if estaCadastrado(CPF): 
        log("amarelo", "cliente já cadastrado")
        return None
    
    cliente0 = PessoaFisica(nome, dataNas, CPF, endereco)
    ListaClientes.append(cliente0)
    log("verde", "CADASTRO REALIZADO COM SUCESSO")
        

def option2():
    CPF = input("Insira o CPF: ")
    while not validar_cpf(CPF):
        CPF = input("Insira um CPF válido: ")
    
    if estaCadastrado(CPF):
        global idTemp 
        idTemp += 1
        cliente0 = returnCliente(CPF)
        conta0 = ContaCorrente(idTemp, cliente0)
        cliente0.contas.append(conta0)
        log("verde", "CONTA CRIADA COM SUCESSO")

    else:
        log("amarelo", "Nenhum cadastro vinculado a esse CPF")

def option3():
    idConta = get_contaIdByUser("Insira sua conta: ")
    valor = get_valor("Insira um valor real para depósito: ")
    
    conta = getInstaceConta(idConta)

    if conta == None:
        log("amarelo", "Conta Inexistente")
        return None

    deposito = Deposito(valor)
    deposito.registrar(conta)
    

def option4():
    idConta = get_contaIdByUser("Insira sua conta: ")
    valor = get_valor("Insira um valor real para depósito: ")
    
    conta = getInstaceConta(idConta)

    if conta == None:
        log("amarelo", "Conta Inexistente")
        return None

    saque = saque(valor)
    saque.registrar(conta)

def option5():
    idConta = get_contaIdByUser("Insira sua conta: ")
    
    conta = getInstaceConta(idConta)

    if conta == None:
        log("amarelo", "Conta Inexistente")
        return None
    
    extrato(conta)

def option0():
    exit(0)

executeOp = {
         "1":      option1,
         "2":      option2,
         "3":      option3,
         "4":      option4,
         "5":      option5,
         "0":      option0
}