from requests import get, ConnectionError

def get_timestamp(onlyDate=False, onlyHours=False, formatInter=False):
    def formatarData(data):
        ano, mes, dia = data.split("-")
        return "/".join((dia, mes, ano))

    try:
        resposta = get("http://worldtimeapi.org/api/ip")
        infoRequisicao = resposta.json()
        tempo = infoRequisicao['datetime']

        date = tempo[:10] if formatInter else formatarData(tempo[:10])
        horario = tempo[11:19]

        if onlyDate and onlyHours:
            return date, horario
        elif onlyHours:
            return horario
        elif onlyDate:
            return date
        else:
            return f"{date} {horario}"
    
    except ConnectionError:
        print("ERRO DE CONEXÃO: não foi possível acessar worldtimeapi.org")
        exit(1)
        
def timeToNextDay():
    hora = 23
    min = 59
    seg = 60
    
    horarioAtual = get_timestamp(onlyHours=True)
    horaAtual, minAtual, segAtual = [int(n) for n in horarioAtual.split(":")]
    
    if segAtual == 0:
        seg = 0
        if minAtual == 0:
            hora = 24
    
    elif minAtual == 0:
        hora = 24
        min = 0
    
    return f"{hora - horaAtual}:{min - minAtual}:{seg - segAtual}"