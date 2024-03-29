from flask import Flask
from routes import backend_bp
import os


app = Flask(__name__)
app.register_blueprint(backend_bp)

UPLOAD_FOLDER = os.path.join('staticFiles', 'uploads') 
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if __name__ == '__main__':
    app.run()