# Sintaxe Básica
# def nome_da_funcao(parametros):
#     #bloco de código
#     return resultado


# Exemplo 

def saudacao():
    print("Olá, bem-vindo (a) à aula de funções em Python!")
    
#para "chamar" a função e executar seu código:

saudacao()

#Exemplo

def saudacao(nome): #'nome' é um parâmetro
    print(f"Olá, {nome}!")
    
saudacao("carlos") #carlos é um argumento
saudacao("Ruan")#colocar outro nome sem apagar o anterior (só reptir o cod.)
#saída: Olá, Carlos!

#Exemplo
def somar (a, b, c, d): #mais de um parâmetro
    return a + b - c * d
resultado = somar (10,20, 5, 2)
print(resultado) #saída: 30

# valores padrão para parâmetros:

def saudacao(nome="aluno"):
    print(f"Olá, {nome}!")
    
saudacao()
saudacao("carlos")
    
#Exemplo de múltiplos retornos:

def checar_numero(n):
    if n > 0:
        return "Positivo"
    elif n < 0:
        return "Negativo"
    else:
        return "Zero"
print(checar_numero(10))

global_var = 100

def exemplo_escopo():
    local_var = "Estou dentro da função"
    print(local_var)
    print(global_var)
    
exemplo_escopo()
# print(local_var)

#Argumentos Posicionais:
#Os argumentos são passados para a função na mesma ordem dos parâmetros.

def exibir_nome_idade(nome, idade):
    print(f"Nome: {nome}, idade: {idade}")
exibir_nome_idade("Carlos", 30)

exibir_nome_idade(idade=71,nome="Marcelo" )

#Argumentos Arbitrários (*args e ** kwargs):
# *args: Recebe multiplos argumentos como um tupla.

def somar_todos(*args):
    return sum(args)
print(somar_todos(1,2,3,4,5)) #Saída: 15

# **kargs: Recebe múltiplos argumentos nomeados como um dicionário
def exibir_detalhes(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")
        
exibir_detalhes(nome="Carlos", idade=30, cidade="São Paulo")