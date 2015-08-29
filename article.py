# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

from myapp import app
from flask import render_template, url_for, redirect, request, flash, session, g, abort
from model import Catagory,db
from flask import  jsonify
import json
import urllib
import random
import os
import re
import datetime
import utils
from urllib import unquote


@app.route('/article/catagorymanage', methods=['GET','POST'])
def catagorymanage():
    return render_template("catagorymanage.html",title = 'Home',action='/catagorymanage')

@app.route('/article/getcatagorys', methods=['GET','POST'])
def getcatagorys():
	catagory=Catagory()
	pageIndexParam = request.form['pageIndex']
	belongto=request.form['belongto']
	catagoryname=unquote(request.form['catagoryname'])
	print belongto
	query=Catagory.query
	###条件查询####
	if belongto:
		query=query.filter(Catagory.belongto == belongto)
	if catagoryname:
		query=query.filter(Catagory.catagoryname.like(catagoryname))
	pageIndexParam=int(pageIndexParam)+1
	total=len(query.all())
	paginate = query.paginate(pageIndexParam, 10, False) 
	catagorys = paginate.items
	catagorylist = []
	for catagory in catagorys:
		catagorylist.append(catagory.to_json())
	return (jsonify(rows=catagorylist,results=total))

@app.route('/article/delcatagorys',methods=['GET','POST'])
def delcatagorys():
	user=User()
	requeststr = request.query_string
	ids=utils.getAjaxIds(unquote(requeststr))
	for userid in ids:
		print userid
		user.deleteuser(userid)
	return(jsonify(msg='0000'))

@app.route('/article/addcatagory', methods=['GET','POST'])
def addcatagory():
    catagory=Catagory()
    requeststr = request.query_string
    print unquote(requeststr)
    params=utils.getparam(unquote(requeststr))
    catagory.catagoryname=params['catagoryname']
    catagory.belongto=params['belongto']
    catagory.addcatagory()
    return jsonify(msg='0000')

@app.route('/article/editcatagory',methods=['GET','POST'])
def editcatagory():
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










