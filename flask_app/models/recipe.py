from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt
import re

class Recipe:
    db_name='recipes'
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.u30 = data['u30']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.user = None
        #for linking users to recipes


#add recipe method
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO recipes ( name , description, instructions, u30, user_id, created_at, updated_at ) VALUES ( %(name)s, %(description)s, %(instructions)s, %(u30)s, %(user_id)s, NOW(), NOW());"
        return connectToMySQL(cls.db_name).query_db( query, data )

#display recipe method
    @classmethod
    def get_one(cls,data):
        query  = "SELECT * FROM recipes WHERE id = %(id)s";
        result = connectToMySQL(cls.db_name).query_db(query,data)
       # if result[0]['u30'] == 0:
       #     result[0]['u30'] = "no"
       # else:
       #     result[0]['u30']= "yes"
        return cls(result[0])
#edit recipe method
   # @classmethod
   # def get_all_recipes(cls):
    #    query = "SELECT * FROM recipes";
    #    results = connectToMySQL(cls.db_name).query_db(query)
     #   user_recipes = []
     #   if results==False:
     #       return []
      #  for row in results:
      #      user_recipes.append( cls(row) )
      #      print(user_recipes)
     #   return user_recipes
      #  #return cls(result[0])

    @classmethod
    def get_all_recipes(cls):
        query = "SELECT * FROM recipes;"
        results =  connectToMySQL(cls.db_name).query_db(query)
        all_recipes = []
        for row in results:
            (print(row))
          #  if row['u30'] == 0:
           #     row['u30'] = "no"
           # else:
           #     row['u30']= "yes"
            all_recipes.append( cls(row) )
        print(all_recipes)
        return all_recipes

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM recipes WHERE id=%(id)s"
        return connectToMySQL(cls.db_name).query_db(query, data)

#delete recipe method
    @classmethod
    def update(cls,data):
        query = "UPDATE recipes SET name=%(name)s,description=%(description)s,instructions=%(instructions)s, u30=%(u30)s, updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)

    

  #  @staticmethod
  #  def validate_recipe(data):
  #      is_valid = True # we assume this is true
   #     if len(data['name']) < 1:
   #         flash('You must fill out recipe name')
   #         is_valid = False
     #   if len(data['description']) < 1:
    #        flash('You must provide a description of your recipe')
    #        is_valid = False
     #   if len(data['instructions']) < 1:
     #       flash('You must provice instructions for your recipe')
     #       is_valid = False
     #   if len(data['u30']) < 1:
       #     flash("please select yes or no")
     #       is_valid=False
    #    # test whether a field matches the pattern
    #    return is_valid