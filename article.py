# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

from myapp import app
from flask import render_template, url_for, redirect, request, flash, session, g, abort
from model import Catagory,db,Article
from flask import  jsonify
import json
import urllib
import random
import os,sys
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
	query=Catagory.query
	###条件查询####
	if belongto:
		query=query.filter(Catagory.belongto == belongto)
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
	catagory=Catagory()
	requeststr = request.query_string
	ids=utils.getAjaxIds(unquote(requeststr))
	for catagoryid in ids:
		catagory.deletecatagory(catagoryid)
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
	catagory=Catagory()
	requeststr=request.query_string
	params=utils.getparam(unquote(requeststr))
	paramdict={}
	paramdict["catagoryid"]=params['catagoryid']
	paramdict["catagoryname"]=params['catagoryname']
	paramdict["belongto"]=params['belongto']
	catagory.updatecatagory(paramdict)
	return jsonify(msg='0000')

@app.route('/article/addarticle')
def addarticle():
	article=Article()
	requeststr=request.query_string
	params=utils.getArticleStr(unquote(requeststr))
	article.title=params[0]
	article.catagoryrelateid=params[1]
	article.content=params[2]
	article.addarticle()
	return jsonify(msg='0000')

@app.route('/article/getArticle')
def getArticle():
	article=Article()
	articlelist=Article.query.all()
	articles=[]
	for article in articlelist:
		articles.append(article.to_json())
	return (jsonify(rows=articles))


@app.route('/article/articlemanage', methods=['GET','POST'])
def articlemanage():
    return render_template("articlemanage.html",title = 'Home',action='/catagorymanage')





