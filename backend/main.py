from flask import Flask
app = Flask(__name__)


@app.route('/')
def saludo():
    return 'Hola mundo Flask, está chilero!'


if __name__ == '__main__':
    app.run()
