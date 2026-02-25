from flask import Flask, render_template

app = Flask(__name__)

campeoes = {
    "kayn": {
        "nome": "Kayn",
        "titulo": "O Ceifador das Sombras",
        "descricao": "Um guerreiro de Ionia que luta pelo controle contra a foice Darkin Rhaast.",
        "imagem": "img/Kayn.jpeg",
        "historia": "Kayn trilha o caminho entre a luz e a escuridão...",
        "classe": "Assassino / Lutador",
        "dificuldade": "Alta"
    },
    "akali": {
        "nome": "Akali",
        "titulo": "A Assassina Renegada",
        "descricao": "Uma ninja letal que abandona a ordem Kinkou.",
        "imagem": "img/Akali.jpeg",
        "historia": "Sem mestre, Akali luta sozinha...",
        "classe": "Assassina",
        "dificuldade": "Alta"
    }
}

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/campeoes")
def lista_campeoes():
    return render_template("campeoes.html", campeoes=campeoes)

@app.route("/campeao/<nome>")
def pagina_campeao(nome):
    campeao = campeoes.get(nome.lower())
    if campeao:
        return render_template("campeao.html", campeao=campeao)
    else:
        return "Campeão não encontrado", 404

app.run(debug=True)
