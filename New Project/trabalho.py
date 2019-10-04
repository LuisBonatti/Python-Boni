from flask import Flask, render_template

app = Flask(__name__)

Nome = "Luis Bonatti"

@app.route ("/")
def teste ():
    return render_template("index1.html")

app.run()