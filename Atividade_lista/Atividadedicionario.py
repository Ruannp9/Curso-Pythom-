Aluno = { "Nome": "Ruan" , "idade": 16,  "nota": 10}

Aluno["curso"] =  "Ciência da Computação"
print(f"curso adicionando ao dicionario {Aluno}") 

Nome_aluno = Aluno.get("Nome")
print(Nome_aluno)

del Aluno[ "nota"]
print(Aluno)

print("idade" in Aluno)