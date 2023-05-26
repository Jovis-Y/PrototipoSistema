import re

def validar_cpf(cpf):
    if len(cpf) != 11:
        return False
    
    if cpf == cpf[0] * 11:
        return False
    
    # Calcula o primeiro dígito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    resto = (soma * 10) % 11
    if resto == 10 or resto == int(cpf[9]):
        pass
    else:
        return False
    
    # Calcula o segundo dígito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    resto = (soma * 10) % 11
    if resto == 10 or resto == int(cpf[10]):
        return True
    else:
        return False


def validar_nome(nome):
    nome = nome.strip()
    
    if re.match(r'^[a-zA-ZÀ-ÿ\s]+$', nome):
        return True
    else:
        return False

def validar_formato_data(data):
    if re.match(r'^\d{2}/\d{2}/\d{4}$', data):
        return True
    else:
        return False
    
def validar_data(data):
    if validar_formato_data(data):
        try:
          dia, mes, ano = [int(n) for n in data.split("/")]
        except TypeError:
          return False
        if not 1910 <= ano <= 2005:
            return False
        elif mes in (1,3,5,7,8,10,12) and 1<= dia <= 31:
            return True
        elif mes in (4,6,9,11) and 1<= dia <= 30:
            return True
        elif mes == 2:
            if isBissexto(ano) and 1 <= dia <= 29:
                return True
            elif (not isBissexto(ano)) and 1 <= dia <= 28:
                return True
            else:
                return False
        else:
            return False
    else:
       return False

def isBissexto(ano):
    if ano % 4 == 0:
      if ano % 100 == 0:
        if ano % 400:
          msg = True
        else:
            msg = False
      else:
        msg = True
    else:
      msg = False