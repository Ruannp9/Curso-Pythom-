import openpyxl.workbook
import requests
import openpyxl

#URL da API

url = "https://jsonplaceholder.typicode.com/users"

#Fazendo a requisição GET para a API
response = requests.get(url)

if response.status_code == 200:
    users = response.json()
    
    #Criando um novo arquivo excel
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    
    #Adicionando os cabeçalhos
    sheet.append(["ID", "Nome", "Email", "Empresa"])
    
    #Adicionando dados da API ao Excel
    for user in users:
        sheet.append([user['id'], user['name'], user['email'], user['company']['name']])
        
    #Salvando o arquivo
    workbook.save("usuarios_api.xlsx")
    print("Dados salvos no arquivo 'usuarios_api.xlsx'.")
    
else:
    print(f"Falha ao obter dados. Status code: {response.status_code}")
    
    

