from os import name, system

def limpar_terminal(pause=False, prompt=""):
    if pause:
        input(prompt)
    
    if name == 'nt':
        system('cls')
    else:
        system('clear')

def printOperacao(operacao, texto):
    if operacao == 1:
        print("\033[91m" + texto + "\033[0m")
    else:
        print("\033[92m" + texto + "\033[0m")
