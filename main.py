from flask import Flask, render_template, request

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
    print(request.form)
    return "Hit Endpoint"

if __name__ == "__main__":
    app.run()

