def escrever_data():
    checkBar = 0
    while checkBar != 2:
        data_nascimento = input("Coloque sua data de nascimento: ")
        checkBar = 0
        
        for x in data_nascimento:
            if (not x.isdigit()):
                if x == '/':
                    checkBar += 1
                else:
                    checkBar = 0
                    break
        if checkBar != 2:
            print("Data de nascimento inválida. Tente novamente!")
    return data_nascimento

def inverter_data():
    data = escrever_data()
    dia = ""
    mes = ""
    ano = ""
    bars = 0

    for x in data:
        if x == "/":
            bars += 1
            continue
        if bars == 0:
            dia += x
        elif bars == 1:
            mes += x
        elif bars == 2:
            ano += x
    
    return f"{mes}/{dia}/{ano}"

print(inverter_data())