# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

from flask import url_for, Markup
from flask.ext.sqlalchemy import SQLAlchemy, BaseQuery
from myapp import app
from datetime import datetime
import json
import simplejson as sj 

db=SQLAlchemy(app)

class UserQuery(BaseQuery):

    def getall(self):
        return self.all()

    def getcategory_id(self, id):
        return self.get(id)

    def to_json(self):
        return list(self.all())

class User(db.Model):
    __tablename__ = 'c_user'
    query_class = UserQuery
    id = db.Column(db.String(20), primary_key=True)
    name = db.Column(db.String(20))

    def __init__(self,id, name):
        super(User, self).__init__(*args, **kwargs)

    def __repr__(self):
        return '<user name %r>' % self.name

    def to_json(self):
        return dict(id=self.id, name=self.name)

		
		