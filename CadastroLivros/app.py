from flask import Flask, render_template, request, redirect


class cadhistoria:
    def __init__(self,idlivro,titulo,autor,ano,genero,faixa):
        self.idlivro = idlivro
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.genero = genero
        self.faixa = faixa


lista = []

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Cadastro de Livros!'


@app.route('/cadastro')
def cadastro():
    return render_template('Cadastro.html', Titulo='Cadastro de Livros')


@app.route('/criar', methods=['POST'])
def criar():
    idlivro = request.form['ID-Livros']
    titulo = request.form['Titulo']
    autor = request.form['Autor']
    ano = request.form['Ano']
    genero = request.form['Genero']
    faixa = request.form['Faixa']
    obj = cadhistoria(idlivro,titulo,autor,ano,genero,faixa)
    lista.append(obj)
    return redirect('/livros')


@app.route('/livros')
def livros():
    return render_template('livros.html', Titulo='Livros', listalivro=lista)


@app.route('/excluir/<idliv>', methods=['GET','DELETE'])
def excluir(idliv):
    for i, liv in enumerate(lista):
        if liv.idlivro == idliv:
            lista.pop(i)
            break
    return redirect('/livros')



@app.route('/editar/<idliv>', methods=['GET'])
def editar(idliv):
    for i, liv in enumerate(lista):
        if liv.idlivro == idliv:
            return render_template('editar.html', Titulo="Editar Historias", livro=liv)


@app.route('/alterar', methods=['PUT', 'POST'])
def alterar():
    id = request.form['ID-Livros']
    for i, liv in enumerate(lista):
        if liv.idlivro == id:
            liv.titulo = request.form['Titulo']
            liv.autor = request.form['Autor']
            liv.ano = request.form['Ano']
            liv.genero = request.form['Genero']
            liv.faixa = request.form['Faixa']
        return redirect('/livros')


if __name__ == '__main__':
    app.run()
