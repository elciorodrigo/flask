from flask import Flask, jsonify, request
import xmltodict
import os
app = Flask(__name__)

@app.route('/')
def index():
    return "simple xml reader"

@app.route("/nfe/upload", methods = ['POST'])
def upload():
   if request.method == 'POST':
       f = request.files['file']
       doc = xmltodict.parse(f)
       dest = {"cpf": doc["nfeProc"]["NFe"]["infNFe"]["dest"]["CPF"],"nome": doc["nfeProc"]["NFe"]["infNFe"]["dest"]["CPF"] }
       emit = {"CNPJ": doc["nfeProc"]["NFe"]["infNFe"]["emit"]["CNPJ"], "razão": doc["nfeProc"]["NFe"]["infNFe"]["emit"]["xNome"] }
       product = {"produtos": doc["nfeProc"]["NFe"]["infNFe"]["det"]["prod"]}
       nfeValues = {"Valores nfe" : doc["nfeProc"]["NFe"]["infNFe"]["total"]}
       return jsonify({"emissor" : emit , "destinatario": dest,"nfe": nfeValues, "produto": product})

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)