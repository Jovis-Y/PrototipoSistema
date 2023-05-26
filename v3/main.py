from handlerOp import executeOp
from menu import printMenu
from terminalFuncs import limpar_terminal

while True:
    printMenu()
    op = input(">> ")
    
    if op not in executeOp.keys():
        limpar_terminal()
        continue
    
    executeOp[op]()
    limpar_terminal(pause=True, prompt="Tecle enter para continuar")
