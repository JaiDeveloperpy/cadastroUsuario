import os
from time import sleep

userInfo = []




def menu():
    
    print("MENU".center(50))
    opcao = int(input("\n1 - Cadastrar usuário \n2 - Procurar usuário \n3 - Deletar Usuarios \n4 - Fechar o programa \n"))
    return opcao

def calculoImposto(salario):
    # "impI" Significa o intermédiario do imposto, que servirá para calcular o imposto, e levar o resultado a sua devida variável
    if salario <= 1903.98:
        impI = salario * 0.275
    elif 1903.99 < salario <= 3751.05:
        impI = salario * 0.15
    elif 3751.06 < salario <= 4664.68:
        impI = salario * 0.225
    else:
        impI = salario * 0.275
    return impI

def cadastrar():
    # Menu principal onde será coletado todas a informações
    
    nome = input("Digite o nome do usuário: ")
    idade = int(input("Digite a idade do usuário: "))
    cpf = str(input("Digite o CPF do usuário: "))
    numero = input("Digite número de telefone do usuário: ")
    salario = float(input("Digite o salário do usuário: "))
    deletado = False
    imposto = calculoImposto(salario)
    criarUser(nome, idade, cpf, numero, deletado, salario, imposto)

def deletarUser():
    
    nome = input("Qual nome do usuário que deseja excluir? ")
    for users in userInfo:
        if users[0].lower() == nome.lower() and users[4] == False:
            users[4] = True
            print("Usuário deletado")
        else:
            print("Usuário não cadastrado!")
        

def criarUser(nome, idade, cpf, numero, deletado, salario, imposto):
    # Criada uma função que cria uma lista (USUÁRIO) e adiciona a matriz de usuários
    
    user = [nome, idade, cpf, numero, deletado, salario, imposto]
    userInfo.append(user)
    print("Usuário Criado")

def procurarNome(nome):
    # Função que procurará usuário pelo nome, sem return pois return pararia a função no primeiro nome encontrado, e existem pessoas com o mesmo nome
    for user in userInfo:
        if user[0].lower() == nome.lower() and user[4] == False:
            print("Usuário encontrado: \nNome: ", user[0], "Idade: ", user[1], "CPF: ", user[2], "Número: ", user[3], "Salário: ", user[5], "Imposto: ", user[6])
        else:
            print("Usuário não encontrado")

def procurarCpf(cpf):
    # Função de procurar o CPF, essa ja possui return pois CPF é unico, assim parando de rodar a função após encontrar o CPF, sem precisar verificar todas as listas, economizando ram
    for user in userInfo:
        if user[2] == cpf and user[4] == False:
            print("Usuário encontrado: \nNome: ", user[0], "Idade: ", user[1], "CPF: ", user[2], "Número: ", user[3], "Salário: ", user[5], "Imposto: ", user[6])
        else:
            print("Usuário não encontrado! ")

def procurar():
    # Funcao para escolher qual será o método de busca, CPF ou nome
    
    opcao2 = int(input("Deseja procurar por nome [Digite 1] \nCPF [Digite 2] \n"))
    match(opcao2):
        case 1:
            nome = input("Digite o nome: ")
            procurarNome(nome)
        case 2: 
            cpf = input("CPF ")
            procurarCpf(cpf)                        
    return

# Input padrão

# interface do terminal
while True:
    opcao = menu()

    match (opcao):
        case 1:
            cadastrar()
        case 2:
            procurar()
        case 3:
            deletarUser()
        case 4:
            print("Programa finalizado!")
            break
        case _:
            print("Número incorreto.")
            continue
            


