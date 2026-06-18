#importando json
import json

#criando funções
def cadastrar_usuario(participantes):
    participante = {}
    nome = input("Digite o nome do usuario: ")
    cpf = input("Digite o cpf do usuario: ")
    cpf = cpf.strip(" ", "-", ".")
    if nome and cpf == "":
        print("Nome ou CPF inválido!")
    elif len(cpf) < 11 and len(cpf) > 11:
        print("CPF de tamanho inválido!")
    encontrado = False
    for participante in participantes:
        if participante["cpf"] == cpf:
            print("CPF já existente!")
    else:
        participante["nome"] = nome
        participante["cpf"] = cpf
        participantes.append(participante)
        print("-" * 30)
        print(f"Usuario {nome} cadastrado com sucesso!")
        print(f"{participante}")
        print("-" * 30)
        salvar_arquivos(participantes)
    

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
    with open("participantes.json", "r") as arquivo:
        participantes = json.load(arquivo)
        return participantes

def salvar_arquivos(participantes):
    with open("participantes.json", "w") as arquivo:
        json.dump(participantes, arquivo, indent=4)
        