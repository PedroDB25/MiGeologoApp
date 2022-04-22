from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/<edad>")
def hello(edad=0):
    agno = 2022 - int(edad)
    return f"Hello, you were born the year {agno}!"

@app.route('/hello/')
@app.route('/hello/<name>')
def hello2(name=None):
    return render_template('hello.html', name=name)