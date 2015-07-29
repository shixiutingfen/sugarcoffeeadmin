# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

from flask import url_for, Markup
from flask.ext.sqlalchemy import SQLAlchemy, BaseQuery
from myapp import app
from datetime import datetime
import datetime,time

db=SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'c_user'
    userid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20),unique=True,nullable=False)
    password = db.Column(db.String(40),nullable=False)
    chinesename = db.Column(db.String(20))
    email = db.Column(db.String(25))
    address = db.Column(db.String(50))
    phone = db.Column(db.Integer)
    mobile = db.Column(db.Integer)
    sex = db.Column(db.Integer)
    age = db.Column(db.Integer)
    qq = db.Column(db.Integer)
    headpic = db.Column(db.String(50))
    logintimes = db.Column(db.Integer,default=1)
    userlevel = db.Column(db.Integer)
    lastlogintime = db.Column(db.String(20))
    createtime = db.Column(db.String(20),default=time.strftime("%Y-%m-%d %H:%M:%S"))

    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)

    def __repr__(self):
        return '<user username %r>' % self.username

    def adduser(self):
        db.session.add(self)
        db.session.commit()

    def deleteuser(self,userid):
        user = User.query.filter_by(userid=userid).first()
        db.session.delete(user)
        db.session.commit()

    def to_json(self):
        return dict(userid=self.userid, username=self.username,password=self.password,
            chinesename=self.chinesename,email=self.email,address=self.address,phone=self.phone,
            mobile=self.mobile,sex=self.sex,age=self.age,qq=self.qq,headpic=self.headpic,
            logintimes=self.logintimes,userlevel=self.userlevel,lastlogintime=self.lastlogintime,
            createtime=self.createtime)

class Catagory(db.Model):
    __tablename__ = 'c_catagory'
    catagoryid = db.Column(db.Integer, primary_key=True)
    catagoryname = db.Column(db.String(20),nullable=False)
    belongto = db.Column(db.Integer)
    createtype = db.Column(db.Integer)
    createuser = db.Column(db.Integer)
    createtime = db.Column(db.String(20),default=time.strftime("%Y-%m-%d %H:%M:%S"))

    def __init__(self, *args, **kwargs):
        super(Catagory, self).__init__(*args, **kwargs)

    def __repr__(self):
        return '<catagory name %r>' % self.catagoryname

    def addcatagory(self):
        db.session.add(self)
        db.session.commit()

    def deletecatagory(self,catagoryid):
        catagory = Catagory.query.filter_by(catagoryid=catagoryid).first()
        db.session.delete(user)
        db.session.commit()

    def to_json(self):
        return dict(catagoryid=self.catagoryid, catagoryname=self.catagoryname,
            belongto=self.belongto,createtype=self.createtype,createuser=self.createuser,
            createtime=self.createtime)

class CatagoryRef(db.Model):
    __tablename__ = 'c_catagoryref'
    refid = db.Column(db.Integer, primary_key=True)
    catagoryid = db.Column(db.Integer,nullable=False )
    relateid = db.Column(db.Integer,nullable=False)

    def __init__(self, *args, **kwargs):
        super(CatagoryRef, self).__init__(*args, **kwargs)

    def __repr__(self):
        return '<CatagoryRef name %r>' % self.refid

    def addcatagoryref(self):
        db.session.add(self)
        db.session.commit()

    def deletecatagoryref(self,catagoryid):
        catagoryref = CatagoryRef.query.filter_by(refid=refid).first()
        db.session.delete(catagoryref)
        db.session.commit()

    def to_json(self):
        return dict(refid=self.refid, catagoryid=self.catagoryid,
            relateid=self.relateid)

class Article(db.Model):
    __tablename__ = 'c_article'
    articleid = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30))
    content = db.Column(db.Text)
    pic = db.Column(db.String(30))
    istop = db.Column(db.Integer)
    createuser = db.Column(db.Integer)
    createtime = db.Column(db.String(20),default=time.strftime("%Y-%m-%d %H:%M:%S"))

    def __init__(self, *args, **kwargs):
        super(Article, self).__init__(*args, **kwargs)

    def __repr__(self):
        return '<article id %r>' % self.articleid

    def addarticle(self):
        db.session.add(self)
        db.session.commit()

    def deletearticle(self,catagoryid):
        article = Article.query.filter_by(articleid=articleid).first()
        db.session.delete(article)
        db.session.commit()

    def to_json(self):
        return dict(articleid=self.articleid, title=self.title,
            content=self.content,pic=self.pic,istop=self.istop,
            createuser=self.createuser,createtime=self.createtime)

class Attach(db.Model):
    __tablename__ = 'c_attach'
    attachid = db.Column(db.Integer, primary_key=True)
    relateid = db.Column(db.String(30))
    realpath = db.Column(db.String(50))
    attachpath = db.Column(db.String(50))
    realname = db.Column(db.String(50))
    attachname = db.Column(db.String(50))

    def __init__(self, *args, **kwargs):
        super(Attach, self).__init__(*args, **kwargs)

    def __repr__(self):
        return '<Attach id %r>' % self.attachid

    def addattach(self):
        db.session.add(self)
        db.session.commit()

    def deleteattach(self,catagoryid):
        attach = Attach.query.filter_by(attachid=attachid).first()
        db.session.delete(attach)
        db.session.commit()

    def to_json(self):
        return dict(attachid=self.attachid, relateid=self.relateid,
            realpath=self.realpath,attachpath=self.attachpath,realname=self.realname,
            attachname=self.attachname)

class Faq(db.Model):
    __tablename__ = 'c_faq'
    faqid = db.Column(db.Integer, primary_key=True)
    faqtype = db.Column(db.String(2))
    picture = db.Column(db.String(30))
    title = db.Column(db.String(100))
    content = db.Column(db.Text)
    readtimes = db.Column(db.Integer)
    createtime = db.Column(db.String(20),default=time.strftime("%Y-%m-%d %H:%M:%S"))

    def __init__(self, *args, **kwargs):
        super(Faq, self).__init__(*args, **kwargs)

    def __repr__(self):
        return '<Faq id %r>' % self.faqid

    def addattach(self):
        db.session.add(self)
        db.session.commit()

    def deleteattach(self,catagoryid):
        faq = Faq.query.filter_by(faqid=faqid).first()
        db.session.delete(faq)
        db.session.commit()

    def to_json(self):
        return dict(faqid=self.faqid, faqtype=self.faqtype,
            picture=self.picture,title=self.title,content=self.content,
            readtimes=self.readtimes,createtime=createtime)

class Friend(db.Model):
    __tablename__ = 'c_friend'
    friendid = db.Column(db.Integer, primary_key=True)
    friendusername = db.Column(db.String(20))
    userid = db.Column(db.Integer)
    status = db.Column(db.Integer)
    level = db.Column(db.Integer)
    createuser = db.Column(db.Integer)
    createtime = db.Column(db.String(20),default=time.strftime("%Y-%m-%d %H:%M:%S"))

    def __init__(self, *args, **kwargs):
        super(Friend, self).__init__(*args, **kwargs)

    def __repr__(self):
        return '<Friend id %r>' % self.friendid

    def addfriend(self):
        db.session.add(self)
        db.session.commit()

    def deletefriend(self,catagoryid):
        friend = Friend.query.filter_by(friendid=friendid).first()
        db.session.delete(faq)
        db.session.commit()

    def to_json(self):
        return dict(friendid=self.friendid, friendusername=self.friendusername,
            userid=self.userid,status=self.status,level=self.level,
            createuser=self.createuser,createtime=createtime)

		
		