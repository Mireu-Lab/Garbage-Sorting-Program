from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from models import *

app = Flask(__name__)

# 파일 업로드
@app.route('/appinventor', methods=['POST'])
def file_upload():
    file = request.get_data()

    with open("Data/1.png", "wb") as f:
        f.write(file)
        f.close()

    return model_run_main("Data/1.png")

@app.route('/fileupload', methods=['POST'])
def file_upload():
    image_path = "./Data/"
    file = request.files['file']
    	
    filename = secure_filename(file.filename)
    os.makedirs(image_path, exists_ok=True)
    file.save(os.path.join(image_path, filename))
    
    return model_run_main(image_path+filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8090)
