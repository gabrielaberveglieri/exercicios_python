# Exercício: Escreva um algoritmo que leia N números e armazene em um array.
# Depois, implemente uma função recursiva que encontre o maior número em um array.


def ler_numeros(n):   # Essa função lê "n" números e armazena em um array "numeros"
    numeros = []
    for _ in range(n): # Inicia um loop que repete "n" vezes. O _ é usado como variável do loop, indicando que não precisamos usar dentro do loop.
        numero = float(input("Digite um número:"))
        numeros.append(numero) # Adiciona o número lido na lista "numeros"
    return numeros # Retorna a lista com todos os números lidos.

def encontrar_maior_numero(array, n): # Função recursiva que recebe um array e o tamanho "n" de array
    if n == 1:  # Se o array tiver apenas um elemento, retorne-o
        return array[0]  # Retorna o único elemento
    
    maior_no_resto = encontrar_maior_numero(array, n-1)  # Chamada recursiva para encontrar o maior número no array

    if array[n-1] > maior_no_resto: # Compara o último elemento do array com o maior número encontrado no "maior_no_resto"
        return array[n-1] # Se o último elemento do array for maior que o maior número no subarray, retorna o último elemento
    else:
        return maior_no_resto # Caso contrário, retorna o maior número encontrado no subarray

N = int(input("Quantos números você quer inserir? ")) # Le o valor de N

numeros = ler_numeros(N) # Le os N números e armazena em um array

maior_numero = encontrar_maior_numero(numeros, N) # Encontra o maior número no array usando a função recursiva

print(f"O maior número no array é: {maior_numero}")