# -*- coding: utf-8 -*-

from flask import Flask
app = Flask(__name__)
app.config.from_object('config')
from views import *
from uploadview import *
from article import *
if __name__ == '__main__':
	app.run(host='localhost', port=7070)
