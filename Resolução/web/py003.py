from flask import Flask, render_template, request, redirect
from alunos import Alunos

pagina_nome = 'Lista alunos'
app = Flask(__name__)
aluno1 = Alunos ('Luis', 'Eduardo Bonatti', 47997245404)
aluno2 = Alunos ('Cristiane', 'Ortiz', 47999480775)
aluno3 = Alunos ('Hercules', 'Bonatti', 47996244034)
aluno4 = Alunos ('Ivone', 'Granemann Thibes Bonatti', 47999474923)
aluno5 = Alunos ('Nayara', 'Granemann Thibes Bonatti', 47996087699)
lista_alunos = [aluno1, aluno2, aluno3, aluno4, aluno5]

@app.route("/")
def inicio():
    return render_template('index.html', Nome=pagina_nome, lista=lista_alunos)

@app.route ("/novo")    
def novo ():
    return render_template ('novo.html')
@app.route (("/salvar"), methods=['POST'])
def salvar():
    nome = request.form ['nome']
    sobrenome = request.form ['sobrenome']
    telefone = request.form ['telefone']
    novo_aluno = Alunos(nome, sobrenome, telefone)
    lista_alunos.append (novo_aluno)
    return redirect ('/')

app.run()