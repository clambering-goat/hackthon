import os
from flask import Flask, request
from werkzeug.utils import secure_filename
from flask_cors import CORS
from dictionary_catalog_matching import compare


UPLOAD_FOLDER = './uploads'
target = os.path.join(UPLOAD_FOLDER, 'csv')
if not os.path.isdir(target):
    os.mkdir(target)

app = Flask(__name__)
CORS(app)

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    file_name = request.form['file_name']
    destination = "/".join([target, secure_filename(file_name)])
    file.save(destination)
    return {}


@app.route('/compare', methods=['POST'])
def compare_cat_dic():
    return compare(0, 2, 3)


@app.route('/health', methods=['GET'])
def health_check():
    return {"message": "OK"}


if __name__ == "__main__":
    app.run(debug=True, port=8000, host="0.0.0.0", use_reloader=False)
