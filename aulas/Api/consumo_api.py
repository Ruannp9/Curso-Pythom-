#Metodos HTTP comuns:

# get: obten dados de um servidor
# post: envia dados para o servidor
# put: atualiza dados no servidor
# delete: Remove dados no servidor

#Ferramentas que usaremos no python: requests: Para fazer requisições HTTP e consumir dados de APIs.
#openpyxl: para manipular arquivos excel (planilhas) com python.

import requests

# URL da API

url = "https://jsonplaceholder.typicode.com/users"

#fazendo a requisição GET para a API
response = requests.get(url)

#Verificando o status da requisição
print(response)
if response.status_code == 200:
    users = response.json() #convertendo a resposta em formoto JSON

    for user in users:
        if user['name'] == "Nicholas Runolfsdottir V":
            print(f"Nome: {user['name']}, Email: {user['email']}")
            print(f"Telefone; {user['phone']}, Endereço: {user['address']}")
else:
    print(f"Falha ao obter dados. Status code: {response.status_code}")