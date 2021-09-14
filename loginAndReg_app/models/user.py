from loginAndReg_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.confirm_password = data['confirm_password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @staticmethod
    def validate_user(user):
        is_valid = True
        if not EMAIL_REGEX.match(user['email']):
            flash('Invalid email address!', 'email')
            is_valid = False
        if len(user['first_name']) < 2:
            flash('First name must be at least 2 characters.', 'first_name')
            is_valid = False
        if len(user['last_name']) < 2:
            flash('Last name must be at least 2 characters.', 'last_name')
            is_valid = False
        
    @classmethod
    def add_user(cls, data):
        query = 'INSERT INTO users (first_name, last_name, email, password, confirm_password) VALUES ( %(first_name)s, %(last_name)s , %(email)s , %(password)s , %(confirm_password)s );'
        new_user = connectToMySQL("loginAndReg_schema").query_db(query, data)
        return new_user
        