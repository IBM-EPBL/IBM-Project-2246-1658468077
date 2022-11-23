from flask import Flask, render_template, session, redirect, request
from controllers.login import signInUser
from controllers.signup import addNewUser


app = Flask(__name__)
app.secret_key = 'supersuper'

@app.route("/")
def homeRoute():
    if 'userId' in session:
        return render_template('daily.html')  
    else:
        return redirect("/login")

@app.route("/categories")
def categoriesRoute():
    if 'userId' in session:
        return render_template('categories.html')       
    else:
        return redirect("/")                

@app.route("/login", methods=['GET', 'POST'])
def loginRoute():
    if  not 'userId' in session:
        if request.method == 'GET':
            return render_template('signin.html')
        else:
            data = request.form
            respone = signInUser(data)
            if (respone != -1):
                return redirect("/")
            else:
                return render_template('signin.html')    
    else:
        return redirect("/")            

@app.route("/sign-up", methods=['GET', 'POST'])
def signupRoute():
    if  not 'userId' in session:
        if request.method == 'GET':
            return render_template('signup.html'); 
        else:
            data = request.form
            try:
                addNewUser(data)
                return redirect("/login")
            except:
                print('Exception Hello')
                return redirect("/sign-up")
    else:
        return redirect("/")        
 