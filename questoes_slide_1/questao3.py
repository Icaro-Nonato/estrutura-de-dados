
def calcula_salario(salario_hora, horas_normais, horas_extras):
    return salario_hora * horas_normais + horas_extras * salario_hora * 1.5

print(calcula_salario(float(input()), float(input()), float(input())))