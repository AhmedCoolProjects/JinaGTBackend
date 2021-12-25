from flask import Flask, request
from functions import coloration2

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1 style='color:red' >Hellooooooooo!</h1>"


@app.route('/colaration', methods=['POST'])
def coloration():
    g = request.get_json("mygraph")
    return {"response":coloration2(g["mygraph"])}

'''
@app.route('/colaration', methods=['POST'])
@app.route('/dijkstra', methods=['POST'])
@app.route('/bellman', methods=['POST'])
@app.route('/kruskal', methods=['POST'])
'''


if __name__ == '__main__':
    app.run(debug=True)

