informações_clientes = {}

while True:
    escolha = (input("1 - Criar conta \n2 - Verificar saldo \n3 - Depositar dinheiro \n4 - Sacar dinheiro \n5 - Encerrar o atendimento"))

    if escolha == "1":
        def criar_conta():
            nome_user = (input("insira seu nome: "))
            senha_user = (input("Insira sua senha: "))
            informações_clientes[nome_user] = {"Senha": senha_user, "Saldo": 0}
            print(f"Conta criada com sucesso: {informações_clientes}")

    if escolha == "2":
        def verificar_saldo():
            nome_user = input("Digite seu nome: ")
            if nome_user in informações_clientes:  
                    if informações_clientes[nome_user]["Senha"] == senha_user:   
                        saldo = informações_clientes[nome_user]["Saldo"]
                    else:
                        print("Senha incorreta.")
                        
                else:
                    print("Usuário não encontrado.")
                
    if escolha == "3":
        def depositar_dinheiro(nome_usar):
            valor_deposito = float(input("Digite o valor"))
            
    
        