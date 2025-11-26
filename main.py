from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/campeoes.html')
def campeoes():
    return render_template("campeoes.html")

@app.route('/Kayn.html')
def Kayn():
    return render_template("Kayn.html")

@app.route('/base.html')
def base():
    return render_template("base.html")

app.run()
