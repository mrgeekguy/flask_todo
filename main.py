from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/todo")
def todo():
    return render_template("todo.html")

@app.route("/submit")
def submit():
    return render_template("submit.html")

@app.route("/submit_form", methods=["POST"])
def submit_form():
    data = (f'Topic: { request.form["topic"] } Info: {request.form["info"]}\n')
    
    return redirect("/todo")

def submit_data(data):
    with open("./data/data.txt", "w+") as f:
        f.write(data)

if __name__ == "__main__":
    app.run()

