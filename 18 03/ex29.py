def exibir_menu():
    print("Bem Vindo ao menu de cadastro")
    print("1 - Novo cadastro")
    print("2 - Ver cadastro")
    print("3 - Sair")
    Print("---------")

def cadastrar_pessoa(cadastros): 
    nome = input("NOME")
    idade = input("IDADE")
    turma = input("TURMA")
    curso = input("CURSO")
    cadastros.append({"nome": nome, "IDADE": idade, "turma"})
    print("Cadastro realizado com sucesso")