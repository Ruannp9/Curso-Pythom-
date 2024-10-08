#Sintaxe básica
class NomeDaClasse:
    #Definição da classe
    pass
class Pessoa:
    pass
Pessoa1 = Pessoa()
Pessoa2 = Pessoa()

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
Pessoa1 = Pessoa("Maria", 30)
print(Pessoa1.nome) #Saída: Maria
print(Pessoa1.idade) #Saída: 30

Pessoa2 = Pessoa("Chico", 40)
print(Pessoa2.nome) #Saída: Chico
print(Pessoa2.idade) #Saída: 40


#Exemplo

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def apresentar(self):
        print(f"Ola, meu nome é {self.nome} e tenho {self.idade} anos.")
        
Pessoa1 = Pessoa("Maria", 30)
print(Pessoa1.nome) #Saída Maria
print(Pessoa1.idade) # Saída 30
Pessoa1.apresentar()

#Execercio:

class Data_nascimento:
    def __init__(self, Data):
        self.Data = Data
        
        
    def apresentar (self):
        print(f"Eu tenho {self.Data} anos.")
        print(f"Eu nasci no ano de {2024 - self.Data}.")
        
  
         
pessoa = Data_nascimento(31)

pessoa.apresentar()
    