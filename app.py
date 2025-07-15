from flask import Flask, request
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['image']
    text = request.form['text_input']

    file.save(os.path.join(UPLOAD_FOLDER, file.filename))

    with open('text.txt', 'w') as f:
        f.write(text)

    return '上傳成功！'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
