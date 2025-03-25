from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'título': 'O Senhor do Aneis - A Sociedade do Anel',
        'autor': 'J.R.R Tokien'
    }, 
]