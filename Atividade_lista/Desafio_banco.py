informações_clientes = {}

while True:
    escolha = (input("1 - Criar conta \n2 - Verificar saldo \n3 - Depositar dinheiro \n4 - Sacar dinheiro \n5 - Encerrar o atendimento"))

    if escolha == "1":
        def criar_conta():
            nome_user = (input("insira seu nome: "))
            senha_user = (input("Insira sua senha: "))
            informações_clientes[nome_user] = {"Senha": senha_user, "Saldo": 0}
            print(f"Conta criada com sucesso: {informações_clientes}")
            
        criar_conta()

    elif escolha == "2":
        def verificar_saldo():
            nome_user = input("Digite seu nome: ")
            senha_user = input("Insira sua senha.")
            if nome_user in informações_clientes:  
                if informações_clientes[nome_user]["Senha"] == senha_user:   
                    saldo = informações_clientes[nome_user]["Saldo"]
                    print(saldo)
                else:
                    print("Senha incorreta.")
                        
            else:
                print("Usuário não encontrado.")
          
        verificar_saldo()   
        
    elif escolha == "3":
        def depositar_dinheiro():
            nome_user = input("insira seu nome para depositar o saldo: ")
            if nome_user in informações_clientes:
                depositar = float(input("Insira o valor que deseja depositar: "))
                informações_clientes[nome_user]["Saldo"] += depositar #cliente inseriu em deposito
                print(f"O deposito de {depositar:.2f} foi feito com sucesso.")#mensagem mostrando que o deposito foi bem sucedido

            else:# caso o nome de usuario não existir em 'informações_cliente'. vai imprimir a mensagem abaixo.
                print("Conta de usuario não existe.")
                
        depositar_dinheiro()
                
    elif escolha == "4":
        def sacar_dinheiro():
            nome_user = input("Insira seu nome para sacar o dinheiro.")       
            if nome_user in informações_clientes:
                sacar = float(input("Insera o valor que desejar sacar: "))
                informações_clientes[nome_user]["Saldo"] += sacar
                print(f"O saque de {sacar:.2f} foi feito com sucesso.")
                
            else:
                print("Conta de usario não existe.")
                
        sacar_dinheiro()
        
    elif escolha == "5":
        break
    print("Sistema encerrado.")
            

            
            
            
    
        