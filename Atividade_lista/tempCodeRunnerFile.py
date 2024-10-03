palavra = "Python"

for letra in palavra: #Neste caso, a variável letra assume cada caractere de string palavra
    print(letra)
palavra = "Python"
for letra in palavra:
    print(f"a letra {letra} tem indice {palavra.index(letra)}")
    