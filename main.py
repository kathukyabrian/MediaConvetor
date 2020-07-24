import os
from config import app
from flask import render_template, request, abort
# from werkzeug import secure_filename

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/video',methods=['GET','POST'])
def video():
    if request.method == "POST":
        f = request.files['file']
        filename = f.filename
        if filename != '':
            file_ext = os.path.splitext(filename)[1]
            if file_ext not in app.config['UPLOAD_EXTENSIONS']:
                abort(400)
            else:
                os.system('ffmpeg -i $HOME/Downloads/Video/{} $HOME/Downloads/Music/{}'.format(filename,os.path.splitext(filename)[0]+".mp3"))
    return render_template('video.html')

@app.route('/audio')
def audio():
    return render_template('audio.html')

if __name__ == "__main__":
    app.run(debug=True)