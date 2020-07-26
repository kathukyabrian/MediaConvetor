import os
from config import app
from flask import render_template, request, abort, flash, redirect, url_for
import subprocess
# from werkzeug import secure_filename

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/video',methods=['GET','POST'])
def video():
    if request.method == "POST":
        f = request.files['file']
        filename = f.filename
        if f:
            if filename != '':
                file_ext = os.path.splitext(filename)[1]
                
                if file_ext not in app.config['VIDEO_EXTENSIONS']:
                    flash('File format not supported',category='danger')
                    return redirect(url_for('video'))
                else:
                    if 'tomp3' in request.form:
                        try:
                            cmd = 'ffmpeg -i $HOME/Downloads/Video/{} $HOME/Downloads/Music/{}'.format(filename,os.path.splitext(filename)[0]+".mp3")
                            subprocess.run(cmd,shell=True)
                            flash("Video conversion completed successfully",category="success")
                        except:
                            flash('The video could not be converted, try again!',category='danger')
                            return redirect(url_for('video'))
                    elif 'to720' in request.form:
                        try:
                            cmd = 'ffmpeg -y -i $HOME/Downloads/Video/{} -c:a aac -ac 2 -ab 128k -c:v libx264 -x264opts keyint=24:min-keyint=24:no-scenecut -b:v 1500k -maxrate 1500k -bufsize 1500k -vf scale=720:-2 $HOME/Downloads/Video/{}'.format(filename,os.path.splitext(filename)[0]+"720"+os.path.splitext(filename)[1])
                            subprocess.run(cmd,shell=True)
                            flash("Video was converted to 720p", category="success")
                        except:
                            flash("The conversion could not be completed, try again!",category="danger")
                            return redirect(url_for('video'))
                    elif 'to540' in request.form:
                        try:
                            cmd = 'ffmpeg -y -i $HOME/Downloads/Video/{} -c:a aac -ac 2 -ab 128k -c:v libx264 -x264opts keyint=24:min-keyint=24:no-scenecut -b:v 1500k -maxrate 1500k -bufsize 1500k -vf scale=540:-2 $HOME/Downloads/Video/{}'.format(filename,os.path.splitext(filename)[0]+"540"+os.path.splitext(filename)[1])
                            subprocess.run(cmd,shell=True)
                            flash("Video was converted to 540p", category="success")
                        except:
                            flash("The conversion could not be completed, try again!",category="danger")
                            return redirect(url_for('video'))
                    elif 'to360' in request.form:
                        try:
                            cmd = 'ffmpeg -y -i $HOME/Downloads/Video/{} -c:a aac -ac 2 -ab 128k -c:v libx264 -x264opts keyint=24:min-keyint=24:no-scenecut -b:v 1500k -maxrate 1500k -bufsize 1500k -vf scale=360:-2 $HOME/Downloads/Video/{}'.format(filename,os.path.splitext(filename)[0]+"360"+os.path.splitext(filename)[1]) 
                            subprocess.run(cmd,shell=True)
                            flash("Video was successfully converted to 360p",category="success")
                        except:
                            flash('The conversion could not complete',category="danger")
                            return redirect(url_for('video'))
                    elif 'to144' in request.form:
                        try:
                            cmd = 'ffmpeg -y -i $HOME/Downloads/Video/{} -c:a aac -ac 2 -ab 128k -c:v libx264 -x264opts keyint=24:min-keyint=24:no-scenecut -b:v 1500k -maxrate 1500k -bufsize 1500k -vf scale=144:-2 $HOME/Downloads/Video/{}'.format(filename,os.path.splitext(filename)[0]+"144"+os.path.splitext(filename)[1]) 
                            subprocess.run(cmd,shell=True)
                            flash("Video was successfully converted to 144p",category="success")
                        except:
                            flash('The conversion could not complete',category="danger")
                            return redirect(url_for('video'))
        else:           
            flash('No file was provided',category='danger')
    return render_template('video.html')

@app.route('/audio')
def audio():
    return render_template('audio.html')

if __name__ == "__main__":
    app.run(debug=True)