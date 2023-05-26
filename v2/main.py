from terminalFuncs import *
from validators import validar_cpf, validar_data, validar_nome

LIMITE_SAQUE = 500
SAQUE = 1
DEPOSITO = 0
AGENGIA = "0001"
toString = ["DEPÓSITO", "SAQUE"]

colors = {
  "info":     "35m",      #Orange for info messages
  "error":    "31m",      #Red for error messages
  "ok":       "32m",      #Green for success messages
  "menu2c":  "\033[46m",  #Light blue menu
  "menu1c":  "\033[44m",  #Blue menu
  "close":  "\033[0m"     #Color coding close
  }
cc = "\033[0m"
ct = "\033[101m"
cs = "\033[41m"
c1 = colors["menu1c"]
c2 = colors["menu2c"]

def printMenu():
    options = {
         "1":      "Cadastrar cliente",
         "2":      "Cadastrar conta",
         "3":      "Depositar",
         "4":      "Sacar",
         "5":      "Mostrar extrato",
         "0":      "Sair"
        }
    colors = {
    "info":     "35m",      #Orange for info messages
    "error":    "31m",      #Red for error messages
    "ok":       "32m",      #Green for success messages
    "menu2c":  "\033[46m",  #Light blue menu
    "menu1c":  "\033[44m",  #Blue menu
    "close":  "\033[0m"     #Color coding close
    }
    cc = "\033[0m"
    ct = "\033[101m"
    cs = "\033[41m"
    c1 = colors["menu1c"]
    c2 = colors["menu2c"]

    def criarLinha(letter, color, length, text):
        menu = color+" ["+letter+"] "+text
        line = " "*(length-len(menu))
        return  menu+line+cc
    line = ct + " "+"Banco do Pará"
    line += " "*(50-len("Banco do Pará")-9) + "v2 "
    line += cc
    print(line)
    line = cs + " "+ "Operações"
    line += " "*(50-len("Operações")-6)
    line += cc
    print (line)
    for key in options:
        print (criarLinha(key, c1, 50 , options[key]))

# nome, data de nascimento, CPF e endereço 
clientes = {}

# contas[IDconta] = {"saldo":0, "CPF":CPF}
contas = {}
         
# modelo -> {conta:{[(valor, operacao)]}
operacoes = {}

def get_valor(prompt):
    def is_float(string):
        try:
            float(string)
            return True
        except ValueError:
            return False
    
    n = "a"
    while not is_float(n):
        n = input(prompt)
        if is_float(n):
            if 0.01 > float(n):
                n = "a"
                continue
    
    return(float(n))

def get_contaIdByUser(prompt):
    def is_int(string):
        try:
            int(string)
            return True
        except ValueError:
            return False
    
    n = "a"
    while not is_int(n):
        n = input(prompt)
        if is_int(n):
            if int(n) < 1:
                n = "a"
                continue
    
    return(int(n))

def depositar(valor, conta):
    if contaExiste(conta):
        contas[conta]["saldo"] += valor
        operacoes[conta].append((valor, DEPOSITO))
        log("verde", f"DEPÓSITO REALIZADO COM SUCESSO: saldo -> {contas[conta]['saldo']}\n")
    else:
        log("amarelo", "Conta inexistente")

def sacar(valor, conta):
    numSaques = 0
    
    if not contaExiste(conta):
        log('amarelo',"Conta inexistente")
        return None

    for i in range(len(operacoes[conta])):
        numSaques += operacoes[conta][i][1]
    
    if numSaques > 2:
        log("amarelo", "já foram realizados 3 saques")
        return None
    
    if valor > 500:
        log("amarelo", "O valor máximo para saque é 500 reais")

    elif valor > contas[conta]["saldo"]:
        log("amarelo", "Saldo insuficiente")

    else:
        if contaExiste(conta):
            contas[conta]["saldo"] -= valor
            operacoes[conta].append((valor, SAQUE))
            log("verde", f"SAQUE REALIZADO COM SUCESSO: saldo -> {contas[conta]['saldo']}\n")
        else:
            log("amarelo", "conta inexistente")

def extrato(conta):
    if len(operacoes[conta]) == 0:
        log("amarelo", "nenhuma operação feita")
        return None
    saques = 0
    depositos = 0
    for operacao in operacoes[conta]:
        espaco = operacao[1] * "   "
        valor = operacao[0]
        cor = "vermelho" if operacao[1] == 1 else "verde"
        
        saques += operacao[0] if operacao[1] == 1 else 0
        depositos += operacao[0] if operacao[1] == 0 else 0

        log(cor, f"{toString[operacao[1]]}{espaco}   {valor}")
    print("=" * 14 )
    print(f"SALDO      {depositos - saques}")


def estaCadastrado(CPF):
    for key in clientes.keys():
        if key == CPF:
            return True
    return False

def cadastrarUser(CPF, nome, dataNas, endereco):
    if estaCadastrado(CPF):
        log("amarelo", "não foi possível cadastrar: CPF já existente")
        return None
    
    clientes[CPF] = {"nome":nome,
                     "data nascimento": dataNas,
                     "endereço":endereco
                     }
    log("verde", "CADASTRO REALIZADO COM SUCESSO\n")
    

def cadastrarConta(CPF):
    id = len(contas) + 1
    contas[id] = {"saldo":0, 
                  "CPF":CPF
                 }
    operacoes[id] = []
    log("verde", f"CONTA CADASTRADA COM SUCESSO: ID ->{id}\n")

def contaExiste(contaId):
    for key in contas.keys():
        if key == contaId:
            return True
    return False

def executarOp(op):
    pause = True
    prompt = "Tecle enter para continuar"
    
    if op == '1':
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
        
        cadastrarUser(CPF, nome, dataNas, endereco)
    
    elif op == '2':
        CPF = input("Insira o CPF: ")
        if estaCadastrado(CPF):
            cadastrarConta(CPF)
        else:
            log("amarelo", "Nenhum cadastro vinculado a esse CPF")

    elif op == '3':
        conta = get_contaIdByUser("Insira sua conta: ")
        valor = get_valor("Insira um valor real para depósito: ")
        depositar(valor, conta)
    
    elif op == '4':
        conta = get_contaIdByUser("Insira sua conta: ")
        valor = get_valor("Insira um valor real para saque: ")
        sacar(valor, conta)
    
    elif op == '5':
        conta = get_contaIdByUser("Insira sua conta: ")
        
        if contaExiste(conta):
            extrato(conta)
        else:
            log("amarelo", "conta inexistente")

    elif op == '0':
        exit(0)
    
    else:
        pause = False

    limpar_terminal(pause, prompt)
        

while True:
    printMenu()
    op = input(">> ")
    executarOp(op)