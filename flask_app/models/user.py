from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    db_name='recipes'
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.password = data['password']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.recipes = []
        #for linking recipes to users


    @staticmethod
    def validate_user(data):
        is_valid = True # we assume this is true
        if len(data['first_name']) < 2:
            flash('Oops! Name must be at least 2 characters.', 'first_name')
            is_valid = False
        if len(data['last_name']) < 2:
            flash('Oops! Name must be at least 2 characters.', 'last_name')
            is_valid = False
        if len(data['password']) < 8:
            flash("Oops! Password must have at least 8 characters.", 'password')
            is_valid = False
        if data['password']!=data['confirmpassword']:
            flash("passwords do not match")
            is_valid=False
        # test whether a field matches the pattern
        if not EMAIL_REGEX.match(data['email']): 
            flash("Invalid email address!", 'email')
            is_valid = False
        return is_valid

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO users ( first_name , last_name, email, password, created_at, updated_at ) VALUES ( %(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW())"
        return connectToMySQL(cls.db_name).query_db( query, data )

    @classmethod
    def get_one(cls,data):
        query  = "SELECT * FROM users WHERE id = %(id)s";
        result = connectToMySQL(cls.db_name).query_db(query,data)
        return cls(result[0])

    @classmethod
    def get_by_email(cls,data):
        query  = "SELECT * FROM users WHERE email = %(email)s";
        result = connectToMySQL(cls.db_name).query_db(query,data)
        if len(result)>0:
            return cls(result[0])
        else:
            return False

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM users WHERE id=%(id)s"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def update(cls,data):
        query = "UPDATE users SET first_name=%(first_name)s,last_name=%(last_name)s,email=%(email)s,updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)
