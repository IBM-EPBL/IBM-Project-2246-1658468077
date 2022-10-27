from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/sign-up", methods = ['POST', 'GET'])
def hello_world():
    if request.method == 'POST':
        data = request.form;
        return render_template('profile.html', name = data["user_name"], email = data["email"], phone = data["mobile"])
    else:
        return render_template('register.html')

@app.route("/sign-in")
def toSignUpPage():
    return render_template('signin.html')

@app.route("/")
def toHomePage():
    return render_template('home.html')  


