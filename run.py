# web服务端,使用flask
from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

# 配置上传文件的保存路径
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# 允许上传的文件类型
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    # 检查是否有文件被上传
    if 'file' not in request.files:
        return jsonify({'message': 'No file part'}), 400

    file = request.files['file']

    # 如果用户没有选择文件，浏览器也会发送一个空的文件字段，因此也要检查文件名是否为空
    if file.filename == '':
        return jsonify({'message': 'No selected file'}), 400

    # 检查文件类型是否允许
    if file and allowed_file(file.filename):
        # 保存文件到指定目录
        if not os.path.exists(app.config['UPLOAD_FOLDER']):
            os.makedirs(app.config['UPLOAD_FOLDER'])
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        return jsonify({'message': 'File uploaded successfully'}), 200

    return jsonify({'message': 'Invalid file type'}), 400


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

