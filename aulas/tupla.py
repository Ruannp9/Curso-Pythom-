#ativade tupla

lista = [ "maçã","banana","laranja"]

lista.append("uva")
print("adicionar uva a lista", lista)

lista.remove("banana")
print("remover banana da lista", lista)

acessar = lista.index("laranja")
print(lista)
print("o segundo elemento da lista é", lista[1])

lista.reverse()
print("lista invertida: ", lista)


#atividade tupla

tupla = ("vermelho","verde","azul")

print("vermelho")
print("azul")

# tupla[2] = "amarelo" #Inalteravel pois uma tupla é imutavel

tupla1 = ("amarelo", "roxo")

tupla3 = tupla + tupla1
print(tupla1)
print(tupla3)

vermelho, verde, azul, amarelo, roxo = tupla3

print(vermelho)
print(verde)
print(azul)
print(amarelo)
print(roxo)

