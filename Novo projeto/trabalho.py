from flask import Flask, render_template

app = Flask(__name__)

Nome = "Luis Bonatti"

@app.route ("/")
def testando ():
    return Nome

@app.route ("/index")
def teste ():
    return render_template("index1.html")

app.run()