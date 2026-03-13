def estaOrdenado(lista):
    for x in range(len(lista)):
        if x != len(lista) - 1:
            if lista[x] > lista[x+1]:
                return False
    return True

a = [1, 5, 7, 9]
print(estaOrdenado(a))
