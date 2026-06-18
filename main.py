#importando as funções do arquivo funcoes.py
import funcoes
import json

#Criando lista de participantes

participantes = funcoes.carregar_dados()

#Criar um loop até o usuario escolher sair
while True:
    #Exibir o menu de opções
    escolha = input("""Bem vindo ao sistema de gestão de eventos!

                Escolha uma opção:
1- Cadastrar usuario
2- Remover usuario
3- Listar usuarios
4- Sair
""")
    if escolha == "4":
        print("Saindo do sistema...")
        break
    if escolha == "1":
        funcoes.cadastrar_usuario(participantes)
    elif escolha == "3":
        funcoes.listar_usuarios(participantes)
    elif escolha == "2":
        funcoes.remover_usuario(participantes)
    else:
        print("-" * 30)
        print("Opção inválida! Selecione uma opção válida.")
        print("-" * 30)