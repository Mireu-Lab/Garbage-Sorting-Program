from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from models import *

app = Flask(__name__)

@app.route('/')
def info_pages():
    if request.method == "GET":
        return render_template("info.html")
    else:
        return "Incorrect connection method"

# 파일 업로드
@app.route('/app', methods=['POST'])
def app_file_upload():
    file = request.get_data()

    with open("Data/1.png", "wb") as f:
        f.write(file)
        f.close()

    return model_run_main("Data/1.png")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
