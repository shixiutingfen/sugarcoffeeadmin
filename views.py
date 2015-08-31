# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

from myapp import app
from flask import render_template, url_for, redirect, request, flash, session, g, abort
from model import User,db
from flask import  jsonify
import json
import urllib
import random
import os
import re
import datetime
import utils
from urllib import unquote

@app.route('/')
@app.route('/index')
def index():
	users = User.query.getall()
	return render_template("test.html",users = users)


@app.route('/home')
def home():
    return render_template("index.html",title = 'Home')


@app.route('/usermanage', methods=['GET','POST'])
def usermanage():
    return render_template("usermanage.html",title = 'Home',action='/usermanage')


@app.route('/getusers', methods=['GET','POST'])
def get_users():
	user=User()
	pageIndexParam = request.form['pageIndex']
	sex=request.form['sex']
	username=request.form['username']
	query=User.query
	###条件查询####
	if sex:
		query=query.filter(User.sex == sex)
	if username:
		query=query.filter(User.username == username)
	pageIndexParam=int(pageIndexParam)+1
	total=len(query.all())
	paginate = query.paginate(pageIndexParam, 10, False) 
	users = paginate.items
	userlist = []
	for user in users:
		userlist.append(user.to_json())
	return (jsonify(rows=userlist,results=total))

@app.route('/delusers',methods=['GET','POST'])
def delusers():
	user=User()
	requeststr = request.query_string
	ids=utils.getAjaxIds(unquote(requeststr))
	for userid in ids:
		print userid
		user.deleteuser(userid)
	return(jsonify(msg='0000'))

@app.route('/adduser', methods=['GET','POST'])
def adduser():
    user=User()
    requeststr = request.query_string
    params=utils.getparam(unquote(requeststr))
    user.username=params['username']
    user.email=params['email']
    user.password=params['password']
    user.sex=params['sex']
    user.adduser()
    return jsonify(msg='0000')

@app.route('/edituser',methods=['GET','POST'])
def edituser():
	user=User()
	requeststr=request.query_string
	params=utils.getparam(unquote(requeststr))
	paramdict={}
	paramdict["userid"]=params['userid']
	paramdict["username"]=params['username']
	paramdict["email"]=params['email']
	paramdict["password"]=params['password']
	paramdict["sex"]=params['sex']
	user.updateuser(paramdict)
	return jsonify(msg='0000')


@app.route('/faq', methods=['GET', 'POST'])
def faq():
    return render_template("faq.html",title = 'faq',action='/faq')









