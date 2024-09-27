#criando um dicionario vazio
dicionario = {}

#criando algums dicionario com uns pare de chave-valor
dicionario = {"nome": "joão", "idade": 30, "cidade": "São Paulo"}



#declarando dicionários

dic = {} #criando um dicionario vazio

print(type(dic)) #verificando se a varial 'dic' é realmente um dicionario
dic_pernambuco = {"Sport": 41, "Santa Cruz": 29, "Nautico": 21} #criando um dicionario ja com a chave e valores
print(dic_pernambuco)

#adicionando um elemento no dicionário (chave: valor)
#onde a chave é 'Salgueiro' e o valor é 1
# note que a chave é passada dentro de colchetes, após o nome do dicionario.

dic_pernambuco["Salgueiro"] = 1
print(dic_pernambuco)

#Buscando valor com base na chave

qnt_titulos = dic_pernambuco.get("Sport") #acessando o valor com base na chave "Sport"
print(qnt_titulos)
print("O Sport tem", qnt_titulos, "titulos")

#remove um elemento com base na chave
del dic_pernambuco ["Salgueiro"]#utilizando o del remove eternamente a chave e o valor
print(dic_pernambuco)

#remove a chave e retorna seu valor
valor = dic_pernambuco.pop ("Nautico") #diferente do (del) o pop exclui e armazena o valor da chave
print("O valor retornado da chave é: ", valor)
print(dic_pernambuco)

#verificando se uma chave existe no dicionário
print("Santa Cruz" in dic_pernambuco)

#Pegar todas as chaves do dicionario
chaves = (dic_pernambuco.keys()) #retorna umna lista dentro de uma tupla
print(chaves)

#Pegar todos os valores do dicionario
teste = dic_pernambuco.values()
print(teste)

acessar = list(chaves) #transformando em uma lista
print(acessar[0]) #acessando um elemento especifico

#pegar todos os valor do dicionario
teste = dic_pernambuco.values()

dic_paulista = {"Corinthias": 29, "Santos": 22, "Palmeiras": 22}

#Removendo e Retornando último elemento
print(dic_paulista.popitem()) #ele apaga e retorna o ultimo elemento do dicionario
print(dic_paulista)

#Mesclar dois dicionários
dic_pernambuco.update(dic_paulista) #ele junta dois dicionario em um so (ele mescla com a variavel inserida a)
print(dic_pernambuco)

#Convertendo um dicionario em uma lista
print(list(dic_pernambuco))
print(list(dic_pernambuco.values()))




