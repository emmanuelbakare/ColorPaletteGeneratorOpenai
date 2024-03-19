from openai import OpenAI
from flask import Flask, render_template, request, redirect, url_for
from chats.colorPalette import generate_colors
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__,
            template_folder="templates" 
            )

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/palette", methods = ["POST"])
def get_color():
    query = request.form.get("query")
    colors = generate_colors(query)
    return {"colors":colors}

@app.route("/login", methods=["POST","GET"])
def login():
    if request.method=="POST":
        name = request.form.get("name")
        return redirect(url_for('user', usr=name))
    else:
        return render_template("login.html")
    
@app.route("/<usr>")
def user(usr):
    return f"<h1>{user}</h1>" 


if __name__ =="__main__":
    app.run(debug=True)