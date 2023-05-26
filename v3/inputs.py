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