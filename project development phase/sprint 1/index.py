from flask import Flask, render_template, redirect


app = Flask(__name__)
app.secret_key = 'supersuper'

@app.route("/")
def homeRoute():
    return redirect("/login")

@app.route("/categories")
def categoriesRoute():
    return render_template('categories.html')             

@app.route("/login")
def loginRoute():
    return render_template('signin.html')              

@app.route("/sign-up")
def signupRoute():
    return render_template('signup.html')     
 