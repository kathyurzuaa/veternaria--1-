from flask import Flask, render_template, request, redirect, url_for, flash
import pymysql

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/PERRO')
def PERRO():
    return render_template("PERRO.html")

@app.route('/CONEJO')
def CONEJO():
    return render_template("CONEJO.html")

@app.route('/GATO')
def GATO():
    return render_template("GATO.html")



if __name__ == "__main__":
    app.run(debug=True)
