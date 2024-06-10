# Exercício 2: Faça um algoritmo que leia uma frase. Depois implemente uma função recursiva que conte o número
# de vogais dentro desta frase. 


# Define a função e recebe dois parâmetros: frase(a string que vai contar as vogais)
# n(comprimento atual da frase a ser processada)
def contar_vogais(frase, n): 
    if n == 0:
        return 0
    
    if frase[n - 1].lower() in 'aeiouáàâãéêíóôõúü': # Verifica se o último caractere da frase é uma vogal, converte para minúsculo
        return 1 + contar_vogais(frase, n - 1) # Se o último caractere for uma vogal, adiciona 1 à contagem e faz uma chamada recursiva para `contar_vogais` com `n-1`
    else:
        return contar_vogais(frase, n - 1) # Se o último caractere não for uma vogal, faz uma chamada recursiva para "contar_vogais" com "n - 1", sem adicionar a contagem

# Solicita uma frase
frase = input("Digite uma frase: ")

# Calcula o número das vogais na frase 
numero_de_vogais = contar_vogais(frase, len(frase))  # Len é uma função que retorna o número de um objeto

# Exibe a frase
print (f"A frase digitada foi: '{frase}'")

# Exibe o número de vogais na frase
print(f"O número de vogais na frase é: {numero_de_vogais}")