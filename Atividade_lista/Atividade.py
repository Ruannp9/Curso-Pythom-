#Exercio 1

# soma = 0
    
# for i in range(1, 11):

#     print(i)
    
# #Exercio 2
# for i in range(1, 50): 
#         soma += i
#         print("A soma de 1 a 50 é:", soma)         
# print(soma)

# #Exercio 3

# tabuada = int(input("insira o numero que deseja saber a tabuada: "))
# mult = 0
# for numero in range (1,11):
#     mult += 1
#     print( f"{tabuada}x {mult} = ", mult*tabuada)

#Exercio 4
# pares = 0

# for i in range(1, 21):
#     pares += 1
#     if pares % 2 == 0:
#         print(i)
        
#Exercio 5 

frase = "Python é divertido!"
palavras = frase.split()
juntas = ''.join(palavras)
letras = 0

for letra in juntas:
    letras += 1 
print(letras)

#exercio 6 

lista = [1,2,3,4,5,6]

for i in lista:
    lista.reverse()
    print(lista)

#Exercio 7



#Exercicio  8

cont = 0 

for i in range (1,101):
    cont=+1
    print(i*i) 