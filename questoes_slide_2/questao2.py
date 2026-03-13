import os

dic = {}
programEnd = False

while not programEnd:
    decision = input("Selecione a opção que deseja:\n\n1-Adicionar/Modificar Elementos\n2-Remover Elementos\n3-Mostrar Lista\n0- Encerrar Programa\n")
    os.system("clear")
    
    if decision == "0":
        programEnd = True
    elif decision == "1":
        el = input("Coloque o nome do elemento que você deseja adicionar/modificar: ")
        os.system("clear")
        quant = int(input("Digite a quantidade de " + el + " que você quer adicionar: "))
        os.system("clear")
        dic[el] = quant
        print("Item adicionado com sucesso\n")
    elif decision == "2":
        done = False
        while not done:
            el = input("Qual elemento você quer remover?")
            os.system("clear")
            if el in list(dic.keys()):
                del dic[el]
                done = True
                print("Item excluído com sucesso\n")
            elif el == "-1":
                done = True
                print("Operação cancelada com suesso\n")
            else:
                print("Item não está na lista")
    elif decision == "3":
        print(dic)
    input("Pressione Enter para continuar ")
    os.system("clear")
            
        