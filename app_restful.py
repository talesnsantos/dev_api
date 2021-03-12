from flask import Flask, request
from flask_restful import Resource,Api
import json

app = Flask(__name__)
api = Api(app)

desenvolvedores = [{'id':0,'Nome':'Tales','Habilidades':['Python','Flask','Java','MySQL','MongoDB']}]


class desenvolvedor(Resource):
    def get(self,id):
        try:
            response = desenvolvedores[id]

        except IndexError:
            mensagem = f'Desenvolvedor de ID {id} nao existe'
            response = {'Status': 'Erro', 'Mensagem': mensagem}

        except Exception:
            mensagem = 'Erro desconhecido, procure o Administrador da API'
            response = {'Status': 'Erro', 'Mensagem': mensagem}

        return response


    def put(self,id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados

    def delete(self,id):
        desenvolvedores.pop(id)
        return {'status':'Sucesso','mensagem':'registro excluido'}


class lista_desenvolvedores(Resource):
    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return {'status': 'Sucesso', 'mensagem': 'Registro inserido'}

    def get(self):
        return desenvolvedores



api.add_resource(desenvolvedor,'/dev/<int:id>')
api.add_resource(lista_desenvolvedores,'/dev/')

if __name__ == '__main__':
    app.run(debug=True)