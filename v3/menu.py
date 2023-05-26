options = {
         "1":      "Cadastrar cliente",
         "2":      "Cadastrar conta",
         "3":      "Depositar",
         "4":      "Sacar",
         "5":      "Mostrar extrato",
         "0":      "Sair"
}

colors = {
    "info":     "35m",      
    "error":    "31m",      
    "ok":       "32m",      
    "menu2c":  "\033[46m",  
    "menu1c":  "\033[44m",  
    "close":  "\033[0m"     
}

def printMenu(options:dict=options):
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
    line += " "*(50-len("Banco do Pará")-9) + "v3 "
    line += cc
    print(line)
    line = cs + " "+ "Operações"
    line += " "*(50-len("Operações")-6)
    line += cc
    print (line)
    for key in options:
        print (criarLinha(key, c1, 50 , options[key]))
