import pandas as pd
from tempo import *

SAQUE = 1
DEPOSITO = 0

def persistir(operacao, valor):
    data = {
        "Data": [get_timestamp(onlyDate=True)],
        "Horário": [get_timestamp(onlyHours=True)],
        "Valor": [valor],
        "Operação": [operacao]
    }
    
    df = pd.DataFrame(data)
    df.to_csv('dados/operacoes.csv', mode='a', index=False, header=False)

def somatorio(operacao):
    df = pd.read_csv("dados/operacoes.csv")
    return df.loc[df["Operação"] == operacao]["Valor"].sum()
    
