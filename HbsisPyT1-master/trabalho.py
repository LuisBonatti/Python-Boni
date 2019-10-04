from flask import Flask, render_template, request, redirect
from Breja import Cerveja
from Breja import Novas

app=Flask(__name__)
lista_cervejas = []
Nova_breja = []

@app.route('/')
def inc():
    return render_template('tbl.html', titulo_pagina='Home')

@app.route('/listar')
def listar():
    return render_template('listar.html', titulo_pagina='Listar', lista=lista_cervejas)

@app.route('/cadastrar')
def cadastrar():
    return render_template('cadastrar.html', titulo_pagina='Cadastrar')

@app.route('/fazer-pedido')
def pedido():
    return render_template('fazer-pedido.html', titulo_pagina='Pedidos' )

@app.route('/salvar', methods=['POST'])
def salvar():
    nome = request.form['nome']
    tipo = request.form['tipo']
    preco = request.form['preco']
    validade = request.form['validade']
    codigo = request.form ['codigo']
    nova_cerveja = Cerveja(nome, tipo, preco, validade, codigo)
    lista_cervejas.append (nova_cerveja)

    return redirect ('/listar')
@app.route ('/pedido', methods=['POST'])
def pedir():
    nome = request.form ['nome']
    tipo = request.form ['tipo']
    pedido_breja = Novas(nome, tipo)
    Nova_breja.append (pedido_breja)
    return redirect ('/feito')
            
app.run()