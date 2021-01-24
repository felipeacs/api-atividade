from models import Pessoas, Usuarios


def insere_pessoas(nome, idade):
    pessoa = Pessoas(nome=nome, idade=idade)
    print(pessoa)
    pessoa.save()


def consulta_all():
    pessoa_all = Pessoas.query.all()
    print(pessoa_all)


def consulta_nome_pessoa(nome):
    pessoa = Pessoas.query.filter_by(nome=nome).first()
    print(pessoa.idade)


def altera_pessoa(nome, idade):
    pessoa = Pessoas.query.filter_by(nome=nome).first()
    pessoa.idade = idade
    pessoa.save()

def exclui_pessoa(nome):
    pessoa = Pessoas.query.filter_by(nome=nome).first()
    pessoa.delete()

def insere_usuarios(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()

def consulta_todos_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)

if __name__ == '__main__':
    # insere_pessoas('Felipe Augusto', 26)
    # insere_pessoas('Augustos', 25)
    insere_usuarios('felipe', '123456')
    insere_usuarios('augusto', '321654')
    consulta_todos_usuarios()
    consulta_all()
    # exclui_pessoa('Augusto')
    altera_pessoa('Felipe', 20)
    consulta_nome_pessoa('Felipe')

