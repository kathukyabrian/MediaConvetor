from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mediaconvertor2020'
app.config['VIDEO_EXTENSIONS'] = ['.mkv', '.mp4','.mov','.wmv','.flv','.avi','.webm']