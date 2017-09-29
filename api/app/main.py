from flask import Flask
from flask import jsonify
from flask import request
import os
import uuid

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
        
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False, port=80)