class escola:
    def __init__(self, ano, localizada):
        self.ano = ano
        self.localizada = localizada
        
    def apresentar(self):
        print(f"O Ginasio pernanbucano aurora foi criado no ano de {self.ano}. ")
        print(f"E está localizada {self.localizada}. ")
        
escola1 = escola(1886,"Na rua da aurora em frente ao rio capibaribe.")
print(escola1.ano)
print(escola1.localizada)

escola1.apresentar()
 