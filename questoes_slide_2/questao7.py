def divideNumeros(lista):
    dic = {'pares': [], 'impares': []}
    for x in lista:
        if x%2==0:
            dic['pares'].append(x)
        else:
            dic['impares'].append(x)
    return dic

print(divideNumeros([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))