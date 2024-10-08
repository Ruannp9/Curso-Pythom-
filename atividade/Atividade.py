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

# frase = "Python é divertido!"
# palavras = frase.split()
# juntas = ''.join(palavras)
# letras = 0

# for letra in juntas:
#     letras += 1 
# print(letras)

#exercio 6 

# lista = [1,2,3,4,5,6]

# for i in lista:
#     lista.reverse()
#     print(lista)

#Exercio 7



#Exercicio  8

# cont = 0 

# for i in range (1,101):
#     cont=+1
#     print(i*i) 
    
    # a estrutara basica de um laço while é
    
    # while condicao: 
    #     bloco de codigo a ser executado
    #     Enquanto a condição for true, o bloco de codigo sera repetidamente executado. Assim que a condicao for false, 
        
    
    
# contador = 1

# while contador <= 5: #Neste exemplo, a variável contador é incrementada a cada iteração
#     print(contador) # Quando o valor de contador é maior que 5
#     contador += 1 #a condição de while deixa de ser verdadeira, e o laço é encerrado
    
    #Exemplos:
    
# while True:
#     nome = input("Digite seu nome(ou 'sair' para parar):") # o programa continua pedidndo ao usuário para digitar seu nome ata que escreva "sair"

#     if nome == "sair":
#          break #o break é usado para sair do laço quando a condição desejada for atiginda
#     print(f"Olá, {nome}!") 
    
    #Exemplo
    
# numero_secreto = 7
# tentativa = None

# while tentativa != numero_secreto:
#     tentativa = int(input("Advinhe o número (entre 1 e 10):"))
    
# print("Parabéns! Voçê advunhou o número")

# #Exemplos:

# contagem = 10 

# while contagem > 0:
#     print(contagem)
#     contagem -= 1
    
# print("Feliz Ano Novo!") # aqui, o laço while é usado para realizar uma contagem regressiva até chegar a 0

# import random

# numero_secreto = random.randint (1, 20)
# tentativa = None

# while tentativa != numero_secreto:
#     tentativa = int(input("Adivinhe o número (entre 1 e 20):"))
    
#     if tentativa >= numero_secreto:
#         print(f"Digite um numero menor que {tentativa} ")
#     elif tentativa <= numero_secreto:
#         print(f"digite um numero maior que {tentativa} ")
        
# print("Parabens voçê advinhou o número")

# Crie um programa que continue pedindo para o usuário digitar
# dois números e a operação desejada (+,-,*,/)
# o laço deve parar quando o usuário digitar "sair".:

# while True:
#     num1 = float(input("Digite o primeiro número: "))
#     num2 = float(input("Digite o segundo número: ")) 
#     operacao = input("Digite a operação (+, -, *, /) ou 'sair' para parar: ")      
    
#     if operacao == "sair":
#         break
    
#     if operacao == "+":
#         print(f"Resultado: {num1 + num2}")
#     elif operacao == "-":
#         print(f"Resultado: {num1 - num2}")
#     elif operacao == "*":
#         print(f"Resultado: {num1 * num2}")
#     elif operacao == "/":
#         if num2 != 0:
#             print(f"Resultado: {num1 / num2}")
#         else:
#             print("Erro: Divisão por zero.")
            
#     else:
#         print("Operação inválida!")
        
# contador = 1

# while contador <= 10: #Neste exemplo, a variável contador é incrementada a cada iteração
#     print(contador) # Quando o valor de contador é maior que 5
#     contador += 1
    
    


# senha = 1234
# tentativa = None

# while tentativa != senha:
#         tentativa = int(input("Advinhe a senha (De 4 digitos):"))
    
# print("Parabéns! Voçê advinhou a senha")
    
    
nomes = []

while True:
    
    nome =input("Adicione nomesa lista( ou 'sair' para parar): ")
 
    if nome == "sair":
        break 
    else:
        nomes.append(nome)
print(nomes)    



    
    


    
    

    