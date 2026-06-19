#importando json
import json
import re

#criando funções
def cadastrar_usuario(participantes):
    participante = {}
    nome = input("Digite o nome do usuario: ")
    cpf = input("Digite o cpf do usuario: ")
    cpf = re.sub(r'\D', '', cpf)
    if nome == "" or cpf == "":
        print("Nome ou CPF inválido!")
    elif len(cpf) != 11:
        print("CPF deve ter 11 dígitos!")
    encontrado = False
    encontrado = any(p["cpf"] == cpf for p in participantes)
    if encontrado:
        print("CPF já existente!")
    else:
        participantes.append({"nome": nome, "cpf": cpf})
        salvar_arquivos()
        print(f"Usuário {nome} cadastrado com sucesso!")
    

def remover_usuario(participantes):
    cpf_remover = input("Digite o cpf do usuario que deseja remover: ")
    encontrado = False
    for participante in participantes:
        if participante["cpf"] == cpf_remover:
            encontrado = True
            print("-" * 30)
            decisao = input(f"""Usuario encontrado: Nome: {participante['nome']} - CPF: {participante['cpf']}
Deseja remover esse usuario? (s/n)""")
            if decisao == "s":
                participantes.remove(participante)
                print("-" * 30)
                print(f"{participante['nome']} com cpf {cpf_remover} removido com sucesso!")
                print("-" * 30)
                salvar_arquivos(participantes)
            elif decisao == "n":
                print("-" * 30)
                print("Operação cancelada!")
                print("-" * 30)
            else:
                print("-" * 30)
                print("Opção inválida! Escolha 's' para sim ou 'n' para não.")
                print("-" * 30)
    if not encontrado:
        print("-" * 30)
        print("Usuario não encontrado! Digite um cpf válido.")
        print("-" * 30)
    

def listar_usuarios(participantes):
    if len(participantes) == 0:
        print("-" * 30)
        print("Nenhum usuario cadastrado!")
        print("-" * 30)
    else:
        print("-" * 30)
        print("Lista de usuarios cadastrados:")
        for usuario in participantes:
            print(f"Nome: {usuario['nome']} - CPF: {usuario['cpf']}")
        print("-" * 30)

def carregar_dados():
    try:
        with open("participantes.json", "r") as arquivo:
            return json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def salvar_arquivos(participantes):
    with open("participantes.json", "w") as arquivo:
        json.dump(participantes, arquivo, indent=4)
        