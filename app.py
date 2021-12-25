from flask import Flask
from functions import addNumbers

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, CODE!'

@app.route('/add/<int:a>/<int:b>/<int:c>')
def add(a, b, c):
    return str(addNumbers(a,b,c))


if __name__ == '__main__':
    app.run(debug=True)
