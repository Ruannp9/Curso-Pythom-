import sqlite3

# Criar uma conexão com o banco de dados
conn = sqlite3.connect('Escola.db')

def inserir():
    Dia_semana = input("Insira a data da semana: ")
    Professor_contratado = input("Insira o nome do professor contratado: ")
    Cadeiras_compradas = float(input("Insira a quantidade de cadeiras compradas: "))
    Cadeiras_valor = float(input("Insira o valor da cadeira que foi comprada: "))
    
    # Inserir os dados na tabela (certifique-se de que a tabela existe)
    conn.execute("INSERT INTO stocks (Dia_semana, Professor_contratado, Cadeiras_compradas, Cadeiras_valor) VALUES (?, ?, ?, ?)", 
                 (Dia_semana, Professor_contratado, Cadeiras_compradas, Cadeiras_valor))
    conn.commit()  # Chamar commit como uma função

# Chamar a função de inserir
inserir()   
conn.close()
