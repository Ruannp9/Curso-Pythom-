#Laços de reptições

# A sintaxe básica de um for em Python é

# for variavel in sequencia:
#     bloco de código executado
    
#     Exemplo
    
# frutas = ["maça", "banana", "laranja"]

# for fruta in frutas:  #Aqui, a variável fruta assume cade valor de lista frutas eo imprime
#     print(fruta)
    
# A função range() gera uma sequencia de números, que é frequentemente utilizada para laços for.:

# for i in range(50): #Gera uma sequência de 0 a 4
#     print(i)
    
#     o range (5) gera números de 0 a 4 (o ultimo número não é incluído).
    
    # Exemplo
    
    
soma = 0
    
for i in range(1, 11): #gera uma sequência de 1 a 10
        soma += i
        
        a = 0 
        b = 10
        print(a)
        print("A soma de 1 a 10 é:", soma) #Neste exemplo, o laço for usado para somar os números de 1 a 10
print(soma)
    
    
#     Exemplo
    
palavra = "Python"

for letra in palavra: #Neste caso, a variável letra assume cada caractere de string palavra
    print(letra)
palavra = "Python"
for letra in palavra:
    print(f"a letra {letra} tem indice {palavra.index(letra)}")
    
#     #Exemplo
    
# frase = input("Digite uma frase: ").lower()
# vogais = "aeiou"
# consoantes = "bcdfghjklmnpqrstvwxyz"
# contador = 0
# contador2 = 0 
 

# for letra in frase:
#     if letra in vogais:
#         contador += 1 
#     elif letra in consoantes:
#         contador2 += 1
# print(f"há {contador} vogais na frase.") # voçê pode usar um laço for para percorrer a frase e verificar se cada caractere é uma vogal..
# print(f"há {contador2} consoantes na frase.")

