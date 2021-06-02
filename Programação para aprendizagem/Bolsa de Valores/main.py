# -*- coding: utf-8 -*-
print("----------------------------------")
print("- Bem-Vindo a carteira de ações! -")
print("----------------------------------")

'''
    Cotação de ação
    Número de ações 
    Posição inicial (investimento - lucro)
    Posição final (investimento + lucro)
    !

'''
acoes = []

def adicionar():
    # Adiciona os valores nas variaveis
    n = str(input("Insira o nome da Ação: "))
    c = str(input("Insira o código da Ação: "))
    q = int(input("Insira a quantidade de ações: "))
    p = float(input("Insira o preço da Ação: "))

    # Adiciona as variaveis no dicionário que adiciona em uma lista
    acoes.append(dict(nome = n,codigo = c,quantidade = q,preco = p))
    print("Adicionado com sucesso!!")

def editar():
    return
def excluir():
    return
def exibir():
    return
def main():
    while(True):
        escolha = int(input("Escolha qual opção você quer, 1- Adicionar, 2- Editar, 3- Excluir, 4- Exibir, 5- Sair: "))
        if(escolha == 1):
            adicionar()
        elif(escolha == 2):
            print("Você entrou em editar!!")
main()
