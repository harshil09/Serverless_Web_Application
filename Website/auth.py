from .__init__ import create_app
from flask import Blueprint, render_template, request, flash, jsonify
#from markupsafe import re
from flask_pymongo import PyMongo
from .models import postData, validatelogin

auth = Blueprint('auth', __name__)

@auth.route('/login', methods= ['GET','POST'])
def login():
  if request.method == 'POST':
      email = request.form.get('email')
      password = request.form.get('password ')
      flask_obj = create_app()
      Mongo = PyMongo(flask_obj)
      currentcollection = Mongo.db.Banking

      if currentcollection.find_one({'email': email}) and currentcollection.find_one({'password1': password}):
          return jsonify({'email': email, 'password1': password})
      else:
          return jsonify({'error': 'cant find'})
   
  return render_template("login.html")

@auth.route('/logout')
def logout():
    return "li"

@auth.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        phonenumber = request.form.get('phonenumber')
        DOB = request.form.get('DOB')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')


        if len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(firstname) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif len(lastname) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif len(phonenumber) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif len(DOB) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords dont match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            flash('Account created!', category='success')

       
        return postData(firstname, lastname, phonenumber, DOB, email, password1)

    return render_template("sign.html")
