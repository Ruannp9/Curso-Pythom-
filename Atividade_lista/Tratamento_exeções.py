resultado = 10/0
print(resultado)

#Exemplos comuns de exceçôes
# ZeroDivisionError: ocorre quando se tenta dividir um número por zero.
#TyperError: ocorre quando uma operação é aplicada a um objeto de tipo inadequado.
#ValueError: Ocorre quando uma função recebe um argumento com o tipo certo, mas valor inapropriado.
#FileNotFoundError:Ocorre quando se tenta abrir um arquivo que não existe.

#Exemplo

# try:
#     resultado = 10/0

# except ZeroDivisionError:
#     print("Erro: Divisão por zero não é permitida.")
    
#Exemplo 1:

# try:
#     #Código que pode causar um exceção

# except TipoDaExceção:
#     #Código que sera executado se ocorrer a exceção
    
# else:
    #Código que sera executado se nenhuam exceção ocorrer
    
#Exemplo 2:

try:
    resultado = 10 / 2
    
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitada.")
else:
    print(f"O resultado é {resultado}")
    
#Exemplo 3:

# try:
#     #Codigo que pode causar um exceção
# except TipoDaExceção:
#     #Codigo que sera executado se ocorrer a exceçãp
    
# finally:
#     #Codigo que será sempre executado

#Exemplo 4:

try:
    arquivo = open('dados.txt', 'r') #Ele printa os dados que tão escrito na pasta que está com a extensão 'dados.txt'
    conteudo = arquivo.read()
    print(conteudo)
    
except FileNotFoundError:
    print("Erro: Arquivo não encontrado.")
    
finally:
    print("Operação finalizada.")
    
#Exemplo 5:

try:
    num = int(input("Digite um número: "))
    resultado = 100 / num
except ValueError:
    print("Erro: Voçê deve digitar um número inteiro.")
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitada.")
else:
    print(f"O resultado é {resultado}")
finally:
    print("Obrigado por usar o programa. ")
    
#Raise: permite que você force uma exceção ao error

#Exemplo 6:

# def verifica_idade(idade):
#     if idade < 18:
#         raise ValueError("Idade deve ser maior ou igual a 18.")
#     else:
#         print("Entrada permitida.")
        
# try:
#     verifica_idade(18)
# except ValueError as e:
#     print(e)
    
#Exemplo 7: criar uma exceção personalizada que herda o 'Exception' ou de uma de suas subclass

# class SaldoinsuficienteError(Exception):
#     """Exceção levantada quando o saldo é insuficiente para realizar uma transação"""
#     pass

# def sacar(valor,saldo):
#     if valor > saldo:
#         raise SaldoinsuficienteError("Saldo insuficiente para sacar o valor solicitado.")
#     saldo -= valor
#     return saldo

# try:
#     saldo_atual = sacar(1500, 1000)
# except SaldoinsuficienteError as e:
#     print(e)
    
#Desafio do professor: Criar outra exceção

# class DepositoInvalidoError(Exception):
#     """Exceção levantada quando o deposito passa do permetido."""
#     pass 

#     def __init__(self, valor, limite):    
#         super().__init__(f"Depósito inválido: R${valor:.2f}. O valor máximo permitido é R${limite:.2f}.")
        
#     limite = 500
#     valor_deposito = float(input("Valor a ser depositado: "))
# try:
#     if valor_deposito > limite:
#         raise DepositoInvalidoError(valor_deposito, limite)
#     print(f"Depósito de R${valor_deposito:.2f} realizado com sucesso.")
# except DepositoInvalidoError as e:
#     print(e)

class DepositoInvalidoError(Exception):
    """Exceção levantada quando o depósito ultrapassa o permitido."""
    def __init__(self, valor, limite):
        super().__init__(f"Depósito inválido: R${valor:.2f}. O valor máximo permitido é R${limite:.2f}.")

# Limite máximo para depósitos
limite = 1000.0

# Bloco try-except para verificar o depósito
try:
    valor_deposito = float(input("Digite o valor a ser depositado: "))  # Coleta o valor do depósito
    if valor_deposito > limite:  # Verifica se o valor ultrapassa o limite
        raise DepositoInvalidoError(valor_deposito, limite)  # Levanta a exceção personalizada
    print(f"Depósito de R${valor_deposito:.2f} realizado com sucesso.")
except DepositoInvalidoError as e:
    print(e)  # Exibe a mensagem de erro da exceção
except ValueError:
    print("Por favor, insira um valor numérico válido.")  # Tratamento para entradas não numéricas


#Atividade final do dia

def obter_elemento_da_lista():
    try:
        # Solicitar ao usuário uma lista de números
        entrada = input("Digite uma lista de números separados por espaço: ")
        lista_numeros = [float(num) for num in entrada.split()]  # Converter a entrada em uma lista de floats

        # Solicitar um índice
        indice = int(input("Digite um índice para obter o elemento correspondente: "))

        # Retornar o elemento no índice especificado
        elemento = lista_numeros[indice]
        return elemento

    except IndexError:
        return "Erro: Índice fora do intervalo da lista."
    except ValueError:
        return "Erro: Certifique-se de inserir apenas números válidos."
    except Exception as e:
        return f"Erro inesperado: {e}"

resultado = obter_elemento_da_lista()
print(resultado)

class SenhaFracaError(Exception):
    """Exceção levantada quando a senha não atende aos critérios de força."""
    def __init__(self, mensagem):
        super().__init__(mensagem)

def verificar_senha(senha):
    if len(senha) < 8:
        raise SenhaFracaError("A senha deve ter pelo menos 8 caracteres.")
    if not any(c.isupper() for c in senha):
        raise SenhaFracaError("A senha deve conter pelo menos uma letra maiúscula.")
    if not any(c.islower() for c in senha):
        raise SenhaFracaError("A senha deve conter pelo menos uma letra minúscula.")
    if not any(c.isdigit() for c in senha):
        raise SenhaFracaError("A senha deve conter pelo menos um número.")

    return "Senha forte!"


try:
    senha_usuario = input("Digite sua senha: ")
    resultado = verificar_senha(senha_usuario)
    print(resultado)
except SenhaFracaError as e:
    print(e)

def calculadora():
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        operacao = input("Digite a operação (+, -, *, /): ")

        if operacao == "+":
            resultado = num1 + num2
        elif operacao == "-":
            resultado = num1 - num2
        elif operacao == "*":
            resultado = num1 * num2
        elif operacao == "/":
            if num2 == 0:
                raise ZeroDivisionError("Erro: Divisão por zero não é permitida.")
            resultado = num1 / num2
        else:
            raise ValueError("Operação inválida. Por favor, escolha entre +, -, * ou /.")

        print(f"Resultado: {resultado}")

    except ValueError as e:
        print(e)
    except ZeroDivisionError as e:
        print(e)
    except Exception as e:
        print(f"Erro inesperado: {e}")

calculadora()



            
    
    
        
        
        
        
        

        

    
