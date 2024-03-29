from flask import Flask
from routes import backend_bp


app = Flask(__name__)
app.register_blueprint(backend_bp)


if __name__ == '__main__':
    app.run()