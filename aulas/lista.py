lista1 = [] #uma lista vazia

lista = [1,"2", 3] #adicionando itens a uma lista
# print(type(lista)) #verificando o tipo da lista

#declaração explícita de lista
lista2 = list ((1,"2",3))
# print (lista2)

#Declarcão implicita
lista3 = ["C", 4.65, True, "True", "vamos aprender", ["outra", "lista", "interna"], lista2]
# print(lista3)

lista4 =["primeiro", "segundo", "terceiro"]
# print(lista4)

#acessando uum elemento da lista
print(lista3)
print(lista3[-1][2]) #acessando a lista dentro da lista


# **fatiando listas**

#nomeDalista[start:stop:step]

#execute um print por vez!! 

# print(lista3[2:4:4])
# print(lista[:3])
# print(lista[3:])
# print(len(lista3))
# print(len(lista3[5[2]]))

lista1.append("marcelo é legal")
lista1.append("ruan")
lista1.append("carro")
lista1.append("black")
lista1.append("caio")
lista1.append("as")


# lista1.insert(1, "Marcos")
# # print(lista1)
# lista1[3] = "ruan"
# print(lista1)

# lista1.sort()
# print("Lista Ordenada: ", lista1)

a = [6,45,89,76]
b = a[:]
b[0] = 5
print(a[2])