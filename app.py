from flask import Flask, request
from flask_restful import Resource, Api

from models import Pessoas, Atividades

app = Flask(__name__)
api = Api(app)


class Pessoa(Resource):
    def get(self, nome):
        try:
            pessoa = Pessoas.query.filter_by(nome=nome).first()
            response = {
                'nome': pessoa.nome,
                'idade': pessoa.idade,
                'id': pessoa.id
            }
        except AttributeError:
            response = {'Status': 'Error',
                        'Mensagem': 'Pessoa nao encontrada.'}
        return response

    def put(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        dados = request.json
        if 'nome' in dados:
            pessoa.nome = dados['nome']
        if 'idade' in dados:
            pessoa.idade = dados['idade']
        pessoa.save()
        response = {'id': pessoa.id,
                    'nome': pessoa.nome,
                    'idade': pessoa.idade}
        return response

    def delete(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        pessoa.delete()
        msg = f'Pessoa {pessoa.nome} excluida com sucesso.'
        return {'status': 'sucesso', 'mensagem': msg}


class ListaPessoas(Resource):
    def get(self):
        pessoas = Pessoas.query.all()
        response = [{'id': pessoa.id, 'nome': pessoa.nome, 'idade': pessoa.idade} for pessoa in pessoas]
        return response

    def post(self):
        dados = request.json
        pessoa = Pessoas(nome=dados['nome'], idade=dados['idade'])
        pessoa.save()
        response = {'id': pessoa.id,
                    'nome': pessoa.nome,
                    'idade': pessoa.idade}
        return response


class ListaAtividade(Resource):
    def get(self):
        atividades = Atividades.query.all()
        response = [{'id': atv.id, 'nome': atv.nome, 'pessoa': atv.pessoa.nome} for atv in atividades]
        return response

    def post(self):
        dados = request.json
        pessoa = Pessoas.query.filter_by(nome=dados['pessoa']).first()
        atividade = Atividades(nome=dados['nome'], pessoa=pessoa)
        atividade.save()
        response = {
            'pessoa': atividade.pessoa.nome,
            'nome': atividade.nome
        }
        return response


class Atividade(Resource):
    def delete(self, nome):
        atividade = Atividades.query.filter_by(nome=nome).first()
        atividade.delete()
        msg = f'Atividade: {atividade.nome} excluida com sucesso.'
        return {'status': 'sucesso', 'mensagem': msg}


api.add_resource(Pessoa, '/pessoa/<string:nome>')
api.add_resource(Atividade, '/atividade/<string:nome>')
api.add_resource(ListaPessoas, '/listapessoas')
api.add_resource(ListaAtividade, '/atividades')

if __name__ == '__main__':
    app.run(debug=True)
