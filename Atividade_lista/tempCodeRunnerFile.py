class Data_nascimento:
    def __init__(self, Data, ano):
        self.DataDeNascimento = Data
        self.Ano = ano
        
    def apresentar (self):
        print(f"Eu tenho {self.idade()} anos.")
        print(f"Eu nasci no ano de{self.Ano}.")
        
    def idade(self):
        ano_atual = 2024
        return ano_atual - self.Ano
        
pessoa = Data_nascimento(31, 2007)
print(pessoa.DataDeNascimento)
print(pessoa.Ano)
pessoa.apresentar
    