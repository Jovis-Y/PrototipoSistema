from os import name, system

def limpar_terminal(pause=False, prompt=""):
    if pause:
        input(prompt)
    
    if name == 'nt':
        system('cls')
    else:
        system('clear')

def log(cor, prompt):
    cores = {
        'vermelho': '\033[91m',
        'verde': '\033[92m',
        'amarelo': '\033[93m',
        'azul': '\033[94m',
        'magenta': '\033[95m',
        'ciano': '\033[96m',
        'branco': '\033[97m'
    }
    resetar_cor = '\033[0m'

    if cor in cores:
        cor_selecionada = cores[cor]
        print(cor_selecionada + prompt + resetar_cor)
    else:
        print(prompt)