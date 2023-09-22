import os
from flask import Flask, flash, request, redirect, url_for, session
from werkzeug.utils import secure_filename
from flask_cors import CORS, cross_origin
from read_input import compare
import logging

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger('HELLO WORLD')

UPLOAD_FOLDER = './uploads'

app = Flask(__name__)
CORS(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
target=os.path.join(UPLOAD_FOLDER,'csv')
if not os.path.isdir(target):
    os.mkdir(target)

@app.route('/upload_catalog', methods=['POST'])
def catalogUpload():
    file = request.files['file']
    filename = secure_filename("catalog.csv")
    destination="/".join([target, filename])
    file.save(destination)
    return {}

@app.route('/upload_dictionary', methods=['POST'])
def dictionaryUpload():
    file = request.files['file']
    filename = secure_filename("dictionary.csv")
    destination="/".join([target, filename])
    file.save(destination)
    return {}

@app.route('/compare', methods=['POST'])
def compare_cat_dic():
    return compare()

@app.route('/health', methods=['GET'])
def healthCheck():
    return {"message":"Hello"}

if __name__ == "__main__":
    app.secret_key = os.urandom(24)
    app.run(debug=True,port=8000,host="0.0.0.0",use_reloader=False)

