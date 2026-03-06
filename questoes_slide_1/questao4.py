def min_max(l):
    menor = l[0]
    maior = l[0]
    for x in l:
        if x > maior:
            maior = x
        if x < menor:
            menor = x
    
    return (menor, maior)

print(min_max([53, 653,342, 123, 4245,56, 54, 747, 678,43]))
    
