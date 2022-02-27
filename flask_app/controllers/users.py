from flask_app import app
from flask_app.models import user, recipe
from flask import render_template, redirect,  session, request, flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template("reglog.html")



#create user route
@app.route('/makeuser', methods=['POST'])
def makeuser():
    if user.User.validate_user(request.form)==False:
        return redirect('/')
    hashedpassword = bcrypt.generate_password_hash(request.form["password"])
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "password": hashedpassword,
        "email" : request.form["email"]
    }
    user_in_database = user.User.save(data) #the return value of save is the id of the user
    print(user_in_database)
    session['user_id'] = user_in_database
    return redirect('/dash')
#display user(dashboard) route

@app.route('/login', methods=['POST'])
def login():
    data = {
        "email": request.form['email'],
    }
    user_in_database = user.User.get_by_email(data)
    if not user_in_database :
        flash("Invalid Email/Password", 'email')
        return redirect('/')
    if not bcrypt.check_password_hash(user_in_database.password, request.form['password']):
        flash("Invalid Email/Password", 'email')
        return redirect('/')
    session['user_id'] = user_in_database.id
    return redirect('/dash')

@app.route("/dash", methods=['GET'])
def dashboard():
    data = {
        'id': session['user_id']
    }
    return render_template('dashboard.html', currentuser = user.User.get_one(data), all_recipes = recipe.Recipe.get_all_recipes())

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
#delete user route

#edit user route
