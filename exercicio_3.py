# Exercício 3: Escreva uma função recursiva que calcule a potência de um número base elevado a um expoente. 

# base = 2 
# expoente = 3
# resultado = base ** expoente
# print(resultado)


def potencia (base, expoente):
    if expoente == 0: # qualquer número elevado a 0 é 1 
        return 1
    elif expoente == 1: # Caso expoente for 1,  dá ele mesmo
        return base
    else: 
        return base * potencia(base, expoente - 1) # Caso recursivo: base * (base elevado ao expoente - 1)

base = int(input("Digite um número para base: "))
print(base)
expoente = int(input("Digite um número para o expoente: "))
print(expoente)

calcular_potencia = potencia(base, expoente)
print(f"O resultado da potência é: {calcular_potencia}") 