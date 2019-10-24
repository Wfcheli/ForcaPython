from flask import Flask, render_template, url_for, request
from forca import Jogo

app = Flask(__name__)
jogo = Jogo("palavras.txt")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/jogar', methods=['GET', 'POST'])
def jogar():
    if request.method == 'POST':
        if not jogo.ganhou() and not jogo.perdeu():
            jogo.chutar(request.form['letra'])
    else:
        jogo.novo_jogo("palavras.txt")
    return render_template('game.html',  jogo=jogo)

if (__name__ == "__main__"):
    app.run(debug=True)
