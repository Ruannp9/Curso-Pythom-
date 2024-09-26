tupla1= (1,2,3)
tupla2 =("quatro", "cinco")
tupla3 = tupla1 + tupla2
print(tupla3)

#desestruturação de tupla

tupla =(1,2,3)
a, b, c = tupla

print(a) #Output: 1
print(b) #Output: 2
print(c) #Output: 3


tupla =(1,2,3) 
print(2 in tupla) #Output: True
print(4 in tupla)  #Output: False

texto = "sera que vai funcionar?"
print(texto.split(" "))

tupla = (1,2,3,2,3,3)
print(tupla.count(2)) #Output: 2 
print(tupla.count(4)) #Output: 0