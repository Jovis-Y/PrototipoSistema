import pandas as pd
from tempo import get_timestamp, timeToNextDay
from datasetManipulation import persistir, somatorio
from terminalFuncs import printOperacao

VALOR_MAXIMO_SAQUE = 500
SAQUE = 1
DEPOSITO = 0


def saqueBlock():
    df = pd.read_csv("dados/operacoes.csv")
    df = df.loc[df["Operação"] == SAQUE]
    
    # verificando se os últimos 3 saques foram realizadas no mesmo dia
    if len(df) >= 3:
        # guardando as 3 datas de quando os 3 saques foram realizados
        tf = df.tail(3)["Data"].reset_index(drop=True) 
        
        if tf[0] == tf[1] == tf[2] == get_timestamp(onlyDate=True):
            print(f"3 saques já se realizaram hoje. Tente novamente em {timeToNextDay()}")
            return(True)
        

def saldoAtual():
    saques = somatorio(SAQUE)
    depositos = somatorio(DEPOSITO)

    return depositos - saques
saldo = saldoAtual()


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
        

def depositar(valor):
    persistir(DEPOSITO, valor)
    print("OPERAÇÃO REALIZADA COM SUCESSO")
    

def sacar(valor):
    # verificando saldo
    if valor > saldo:
        print("Saldo insuficiente")

    # verificando valor
    elif valor > VALOR_MAXIMO_SAQUE:
        print("O valor máximo para saque é 500 reais")
    
    else:
        persistir(SAQUE, valor)
        print("OPERAÇÃO REALIZADA COM SUCESSO")
        
    
def extrato():
    df = pd.read_csv("dados/operacoes.csv")
    for index, row in df.iterrows():
        operacao = 1 if row['Operação'] == 1 else 0
        printOperacao(operacao,f"{row['Data']}   {row['Horário']}   {'SAQUE   ' if row['Operação'] == 1 else 'DEPÓSITO'}    {row['Valor']}")

