from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/campeões.html')
def campeões():
    return render_template("campeões.html")

app.run()
