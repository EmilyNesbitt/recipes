from crypt import methods
from tarfile import HeaderError
from flask_app import app
from flask_app.models import user, recipe
from flask import render_template, redirect,  session, request, flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/newrecipe', methods=['POST'])
def newrecipe():
    data = {
        "name": request.form["name"],
        "description": request.form["description"],
        "instructions": request.form["instructions"],
        "u30" : request.form["u30"],
        "user_id": session['user_id']
    }
    print (data)
    recipe.Recipe.save(data)
    return redirect('/dash')

@app.route("/create", methods=['GET'])
def create():
    data = {
        'id': session['user_id']
    }
    return render_template('add_recipe.html', currentuser = user.User.get_one(data))

#@app.route('/one_recipe', methods=['GET'])
#def onerecipe():
 #   data = {
 #       'id': WHERE DO I GET THE RECIPE ID session.id
 #   }
 #   return render_template('display_recipe.html', recipe = recipe.Recipe.get_one(data))
#display recipe controller
@app.route('/delete_recipe/<int:id>', methods=['POST'])
def deleterecipe(id):
    data = {
        "id":id
    }
    recipe.Recipe.delete(data)
    return redirect('/dash')
#delete recipe controller

@app.route('/edit_one_recipe/<int:id>', methods = ['GET'])
def editpage(id):
    data = {
        'id':id
    }
    return render_template('edit_recipe.html', onerecipe=recipe.Recipe.get_one(data))

@app.route('/edit_recipe/<int:id>', methods=['POST'])
def editrecipe(id):
    #if recipe.Recipe.validate_recipe(request.form)==False:
      #  return redirect('/edit_recipe')
    (print(id))
    data = {
        "name": request.form["name"],
        "description": request.form["description"],
        "instructions": request.form["instructions"],
        "u30" : request.form["u30"],
        "user_id": session['user_id'],
        "id":id
    }
    recipe.Recipe.update(data)
    print(data)
    return redirect('/dash')
#edit recipe controller

@app.route('/onerecipe/<int:id>', methods = ['GET'])
def onerecipe(id):
    data = {
        "id":id
    }
    return render_template ('display_recipe.html', onerecipe=recipe.Recipe.get_one(data) )
