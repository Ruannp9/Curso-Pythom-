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