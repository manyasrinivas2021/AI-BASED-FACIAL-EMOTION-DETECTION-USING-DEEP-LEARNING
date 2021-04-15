import os
from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def indexnew():
    return render_template('dataloader.html')

@app.route('/preproc')
def preproc():
     #os.system("python emotions.py --mode display")
     os.system("python real_time_video.py --mode display")
     return render_template('dataloader.html')

#os.system("real_time_video")
if __name__ == '__main__':
    UPLOAD_FOLDER = 'D:/Upload'
    app.secret_key = "secret key"
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run()
