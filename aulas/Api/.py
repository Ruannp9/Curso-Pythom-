import requests

    
url = "https://loteriascaixa-api.herokuapp.com/api/maismilionaria"

response = requests.get(url)

if response.status_code == 200:
    users = response.json()
        
    for user in users:
            print(f"loterias: {user['loteria']}, ")
            
else:
    print(f"Falha ao obter dados. Status code: {response.status_code}")