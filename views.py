# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

from myapp import app
from flask import render_template, url_for, redirect, request, flash, session, g, abort
from model import User
from flask import  jsonify
import json

@app.route('/')
@app.route('/index')
def index():
	users = User.query.getall()
	return render_template("test.html",users = users)


@app.route('/home')
def home():
    #user = {'nickname': 'Miguel'}
    #posts=[{'author':'shixiuting','title':'husband'},{'author':'yangsaifen','title':'wife'}]
    return render_template("index.html",title = 'Home')


@app.route('/usermanage')
def learn():
    return render_template("usermanage.html",title = 'learn')

@app.route('/getusers', methods=['GET'])
def get_users():
	users = User.query.getall()
	userlist = []
	for user in users:
		userlist.append(user.to_json())
	return (jsonify(rows=userlist,results=len(userlist)))

@app.route('/adduser', methods=['GET','POST'])
def adduser():
	#username=request.form['username']
	return render_template("success.html",title = 'Home',action='/usermanage')







