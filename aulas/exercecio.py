minhaLista= [ 76,92.3,"oi", True, 3, 76]

minhaLista.append ("pera")
minhaLista.append("76")
print ("adicionando pera e 75 no final da lista", minhaLista)

minhaLista.insert(3, "gato")
print( "adicionando gato no index 3", minhaLista)

minhaLista.insert(0, 99)
print("adicionando 99 no inicio da lista", minhaLista)


indice = minhaLista.index("oi")
print(indice)

minhaLista.remove (True)
print(minhaLista)