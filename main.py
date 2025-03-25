from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'título': 'O Senhor do Aneis - A Sociedade do Anel',
        'autor': 'J.R.R Tokien'
    }, 
    {
        'id': 2,
        'título': 'Harry Potter e a Pedra Filosofal',
        'autor': 'J.K Howling'
    }, 
    {
        'id': 3,
        'título': 'James Clear',
        'autor': 'Hábitos Atômicos'
    }, 
]

@app.route('/livros')
def obter_livros ():
    return jsonify(livros)

app.run(port=5000,host='localhost',debug=True)