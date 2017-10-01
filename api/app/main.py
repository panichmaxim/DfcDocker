from flask import Flask
from flask import jsonify
from flask import request
import os
import uuid
import requests
import json

app = Flask(__name__)

@app.route("/")
def hello():
    return "Cool landing"

@app.route('/estimate', methods=['POST'])
def estimate():
    try:
        file = request.files['image']
        extension = os.path.splitext(file.filename)[1]
        f_name = str(uuid.uuid4()) + extension
        return jsonify({'filename': f_name})
    except Exception as err:
        return jsonify({'error': str(err)})

@app.route('/price', methods=['GET'])
def price():
    address = request.args.get("address")
    headers = {'Content-type': 'application/json', 'Authorization': 'Token f8f2767f4315a8ae3b9257fbbfd4b95e58400a08', 'X-Secret': 'e1fb2e2d850a06fce84de9c1a47e8f93b3b40edb'}
    data = [address]
    response = requests.post("https://dadata.ru/api/v2/clean/address", headers=headers, data=json.dumps(data))
    data = json.loads(response.content)
    return jsonify(data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False, port=80)
