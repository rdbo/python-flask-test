from flask import Flask, url_for, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy

app = Flask("test")
@app.route("/")
@app.route("/index.html")
def index():
    return render_template("index.html")

@app.route("/test.html/<name>")
def test(name):
    return render_template("test.html", input_name=name)

@app.route("/create-entry", methods=["GET", "POST"])
def create_entry():
    if(request.method=="POST"):
        val = request.form["input_name"]
        return redirect(url_for("test", name=val))
    else:
        return "<h1>!POST invalid</h1>"

if __name__ == "__main__":
    app.run()