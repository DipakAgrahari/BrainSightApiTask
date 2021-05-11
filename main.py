
from flask import Flask, jsonify
import numpy
import nilearn
import timeit

app = Flask(__name__)



@app.route('/module/<string:name>', methods=['GET'])
def get(name):
    if name == 'numpy':
        a = dir(numpy)
        return jsonify(a)
    
    if name == 'nilearn':
        a = dir(nilearn)
        return jsonify(a)
    
    if name == 'timeit':
        a = dir(timeit)
        return jsonify(a)


if __name__ == '__main__':
    app.run(debug=True)
