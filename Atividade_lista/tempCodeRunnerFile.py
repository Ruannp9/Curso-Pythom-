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
