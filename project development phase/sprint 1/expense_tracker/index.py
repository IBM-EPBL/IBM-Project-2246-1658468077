from flask import Flask, render_template

app = Flask(__name__)

@app.route("/sign-up")
def hello_world():
    return render_template('register.html')

@app.route("/sign-in")
def toSignUpPage():
    return render_template('signin.html')