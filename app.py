from flask import Flask,jsonify,request
import json

app = Flask(__name__)

desenvolvedores = [{'id':0,'Nome':'Tales','Habilidades':['Python','Flask','Java','MySQL','MongoDB']}]


# manipula desenvolvedores pelo ID
@app.route('/dev/<int:id>/', methods = ['GET','PUT','DELETE'])
def desenvolvedor(id):
    

    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            __mensagem = f'desenvolvedor de ID {id} nao existe'
            response = {'Status': 'Erro', 'Mensagem': __mensagem}
        return jsonify(response)

    # put altera
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)

    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status':'Sucesso','mensagem':'registro excluido'})


# lista e cadastra os desenvolvedores
@app.route('/dev/', methods = ['POST', 'GET'])
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        desenvolvedores.append(dados)
        return jsonify({'status': 'Sucesso', 'mensagem': 'Registro inserido'})

    elif request.method == 'GET':
        return jsonify(desenvolvedores)







if __name__ == '__main__':
    app.run(debug= True)