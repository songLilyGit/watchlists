1  #!/usr/bin/env python
2  # -*- coding:utf-8 -*- 
3  #宋丽丽

from flask import Flask
from flask import url_for
app=Flask(__name__)

@app.route('/')
@app.route('/home')
@app.route('/index')
def hello():
    return '<h1>Hewewewellorsdsdsdse Totorodfdfdfdf!!!!</h1><img src="http://helloflask.co m/totoro.gif">'

@app.route('/user/<name>')
def user_page(name):
    return 'USER is %s'% name

@app.route('/test')
def test_url_for():
    print(url_for('hello'))
    print(url_for('user_page',name='songlili'))
    print(url_for('test_url_for'))
    print(url_for('test_url_for',num=2))
    return  'test page'

