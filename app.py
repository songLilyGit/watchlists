1  #!/usr/bin/env python
2  # -*- coding:utf-8 -*- 
3  #宋丽丽

from flask import Flask,render_template
from flask import url_for
app=Flask(__name__)


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

name = 'songlili'
movies = [ {'title': 'My Neighbor Totoro', 'year': '1988'},
           {'title': 'Dead Poets Society', 'year': '1989'},
           {'title': 'A Perfect World', 'year': '1993'},
           {'title': 'Leon', 'year': '1994'},
           {'title': 'Mahjong', 'year': '1996'},
           {'title': 'Swallowtail Butterfly', 'year': '1996'},
           {'title': 'King of Comedy', 'year': '1999'},
           {'title': 'Devils on the Doorstep', 'year': '1999'},
           {'title': 'WALL-E', 'year': '2008'},
           {'title': 'The Pork of Music', 'year': '2012'},
           {'title': 'The Pork of Music of ', 'year': '2013'},
           ]

@app.route('/dd')
def index():
    return render_template('index.html',name=name,movies=movies)

@app.route('/result')
def result():
    dict={"phy":50,"che":20,"maths":30}
    return  render_template("hello.html",result=dict)

@app.route('/guolv')
def hello_world():
    student={"name":"lili","age":-18}
    goods=[
        {'name':'怪味少女'},
        {'name':'复杂牛仔'},
        {'name':'秋天外套'},
        {'name':'冬天羽绒服'}
    ]
    return render_template("guolv.html",**student,goods=goods)

def do_index_class(index):
    if index%3==0:
        return 'line'
    else:
        return ''

app.add_template_filter(do_index_class,'index_class')

@app.route('/macro')
def hello_macro():
    return  render_template("hong.html")

@app.route('/jicheng')
def jicheng():
    return  render_template("jicheng.html")

@app.route('/product')
def product():
    return  render_template("product.html")