from fastapi import FastAPI, HTTPException
from typing import List

app = FastAPI()

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

@app.get("/livros")
def obter_livros():
    return livros

@app.get("/livros/{id}")
def obter_livro_por_id(id: int):
    for livro in livros:
        if livro.get('id') == id:
            return livro
    raise HTTPException(status_code=404, detail="Livro não encontrado")

@app.put("/livros/{id}")
def editar_livro_por_id(id: int, livro_alterado: dict):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return livros[indice]
    raise HTTPException(status_code=404, detail="Livro não encontrado")

@app.post("/livros")
def adicionar_livro(livro: dict):
    # Criar um ID novo
    novo_id = max([livro['id'] for livro in livros]) + 1 if livros else 1
    livro['id'] = novo_id
    livros.append(livro)
    return livro

@app.get("/livros/vazio")
def obter_livros_vazio():
    # Simula o cenário de uma lista vazia
    return []
