from flask import Flask

app = Flask(__name__)

@app.route('/')
def hola_mundo():
    return 'Hola mundo, mi primera app Flask'

if __name__ == '__main__':
    app.run('localhost',5000, debug=True)