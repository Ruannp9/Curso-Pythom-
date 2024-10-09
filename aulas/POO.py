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

class escola:
    def __init__(self, ano, localizada):
        self.ano = ano
        self.localizada = localizada
        
    def apresentar (self):
        print(f"O Ginasio pernanbucano aurora Foi criada no ano {self.ano}.")
        print(f"Está localizada {self.localizada}")
        
escola1 = escola(1886, "na rua da aurora.")
print(escola1.ano) 
print(escola1.localizada)

escola1.apresentar()

#Exemplo

class Animal:
    def __init__(self, nome):
        self.nome = nome
        
    def emitir_som(self):
        print(f"{self.nome} diz: barulho!")
        
class Cachorro(Animal):
        pass
class Gato(Animal):
    pass

dog = Cachorro("Rex")
cat = Gato("Tom")

dog.emitir_som()
cat.emitir_som()

class professor_carlos:
    def __init__(self, aluno1, aluno2):
        self.aluno = aluno1
        self.Aluno = aluno2
        
    def estudar(self):
        print(f"{self.aluno} estuda tupla.")
        print(f"{self.Aluno} estuda def.")
        
class Aluno16(professor_carlos):
    pass
class Aluno17(professor_carlos):
    pass
    
aluno1 = Aluno16("Ruan", "Guilherme")
aluno2 = Aluno17("Marcelo", "Vitor")

aluno1.estudar()
aluno2.estudar()
    
    
#Polimorfismo é um conceito fundamental na programação orientada a objetos que permite que objetos de defirentes classes sejam tratados
#de forma unificada através de uma interface comun.

#Exemplo

class Animal:
    def fazer_som(self):
        pass #Método abstrato
    
class Cachorro(Animal):
    def fazer_som(self):
        print("Au Au!")
        
class Gato(Animal):
    def fazer_som(self):
        print("Miau!")
        
animais = [Cachorro(), Gato()]

for animal in animais:
    animal.fazer_som()

class Música:
    def estilo_musical(self):
        pass
    
class musica1(Música):
    def estilo_musical(self):
        print("quem le e frango")
        
class musica2(Música):
    def estilo_musical(self):
        print("Estilo musical de marcelo é trap.")
        
Estilo = [musica1(), musica2()]

for musica in Estilo:
    musica.estilo_musical()
    
#Exemplo

class Pessoa:
    def __init__(self, nome):
        self.__nome = nome
        
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome (self, novo_nome):
        if isinstance(novo_nome, str) and novo_nome.strip():
            self.__nome = novo_nome
        else:
            print("Nome inválido.")
            
#Uso da classe

pessoa = Pessoa("Alice")
pessoa.nome = "Bob"
print(pessoa.nome)
pessoa.nome = ""

#Decoreitory

#Exemplo

class Pessoa:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade
        
    def exibir_informacoes(self):
        print(f"Nome: {self.__nome}, idade: {self.__idade}")
        
    def get_nome(self):
        return self.__nome
    
    def get_idade(self):
        return self.__idade
        
pessoa = Pessoa("Alice", 30)

print(pessoa.get_nome(), pessoa.get_idade())
        
    

        
    