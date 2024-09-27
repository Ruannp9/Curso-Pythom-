#Atenção: Usem o print para retornar o valor das variáveis !!
#Declarando uma sting:

mensagem = "heloo, world!"

# Concatenando string: ( concatenando significa juntar)

primeiro_nome = "João"
sobrenome = "Silva"
nome_completo = primeiro_nome + " " + sobrenome
print(nome_completo)

#acessando caracteres individuais em uma string

mensagem = "Hello, world!"
primeiro_caractere = mensagem[0] #acessando a primeira letra da string utilizando o index 0
ultimo_caractere = mensagem[-1] #acessando a ultima letra da string utilizando o -1 que mostra o ultimo indice   
print(mensagem)

#Encontrando o comprimento de uma string:

mensagem = "Hello, world!"
comprimento = len(mensagem) # O len conta quantos elementos tem em uma string
print(comprimento) #output 13

#Convertendo uma string para letras maiúsculas ou minúscula
mensagem = "hello, world!"
maiuscula = mensagem.upper()
minuscula = mensagem.lower()
primeira_linha = mensagem [2:]
H = mensagem [0]
E = mensagem [1]
maiusculo = E.upper()
minusculo = H.lower()

juncao = minusculo + maiusculo + primeira_linha

print(juncao)

#dividindo uma string em substring com base em um delimita
mensagem = "Hello, world!"
palavras = mensagem.split(",")

#verificando se uma subtring está presente em uma string:

mensagem = "Hello, world!"
if "world" in mensagem:
    print("A substring 'world' esta presente na mensagem.")
    
    #Removando espaços em branco de uma string:
    
frase = "  Hello, world!  "
sem_espacos = frase.strip() # Retorna "Hello, world!"
print (sem_espacos)
