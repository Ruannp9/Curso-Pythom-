
import sqlite3

# Criar uma conexão com o banco de dados
conn = sqlite3.connect('mydtabase.db')

# Inserir a data que deseja alterar
inserir = input("Insira a nova data que deseja alterar (formato YYYY-MM-DD): ")

# Usar parâmetros para evitar SQL injection e formatar a consulta corretamente
conn.execute("UPDATE stocks SET date = ? WHERE symbol = ?", (inserir, 'IBM'))

# Commit das mudanças
conn.commit()

# Fechar a conexão
conn.close()