from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World from Flask"

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=80)
    
@app.route('/estimate', methods=['POST'])
def upload():
    try:
        imagefile = flask.request.files.get('imagefile', '')
        return jsonify({'estimate': imagefile})
    except Exception as err:
        return jsonify({'error': "Error loading file"})