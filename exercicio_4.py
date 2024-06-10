# Exercício 4: Implemente um algoritmo usando uma função recursiva que possa
# demonstrar os resultados impressos com base em um número informado pelo usuário.

# Explicação: 
# se o número for par, divide por 2
# se o número for ímpar, multiplica por 3 + 1 

def collatz(n):
    print(n)
    if n == 1: # Verifica se n é igual a 1, se for, a função retorna
        return
    elif n % 2 == 0: # Verfifica se n é par
        collatz(n // 2) # Se sim, chama a função "collatz" e com n divido por 2. 
    else: 
        collatz(3 * n + 1) # Caso n seja ímpar, chama a função "collatz" com 3 * n + 1
     
try:
    num = int(input("Digite um número inteiro positivo: "))
    if num <= 0: # Se o número for menor que 0, gera um erro
        raise ValueError("Por favor, insira um número inteiro positivo.")
    collatz(num) # Chama a função Collatz com o número fornecido pelo usuário
except ValueError as e: # Captura as exceções de ValueError e imprime a mensagem de erro correspondente.
    print(e)