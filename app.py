1  #!/usr/bin/env python
2  # -*- coding:utf-8 -*- 
3  #宋丽丽

from flask import Flask,request
from flask import url_for

app=Flask(__name__)

@app.before_request
def befor_all():
    print("before request")

@app.after_request
def after_all(environ):
    return environ





@app.route('/home')
@app.route('/index')
def hello():
    return '<h1>Hewewewellorsdsdsdse Totorodfdfdfdf!!!!</h1>'

@app.route('/user/<name>')
def user_page(name):
    return 'USER is %s'% name

@app.route('/test')
def test_url_for():
    print(url_for('hello'))
    print(url_for('user_page',name='songlili'))
    print(url_for('test_url_for'))
    print(url_for('test_url_for',num=2))
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

from flask import render_template,flash,redirect,send_from_directory
from forms import LoginForm,UploadForm,RichTextForm,RegisterForm
from config import Config
from flask_wtf import FlaskForm
app.config.from_object(Config)

@app.route('/register')
def register():
    return render_template("register.html")


@app.route('/login',methods=['GET', 'POST'])
def basic():
    form=LoginForm()
    if form.validate_on_submit():
        form.data
        flash('Login requested for usr {},rember={}'.format(form.username.data,form.rember.data))
        return redirect(url_for('index'))
    return  render_template('login.html',title='Sign In', form=form)

import os

import uuid
app.config['MAX_CONTENT_LENGHT']=1024*1024
app.config['UPLOAD_PATH']=os.path.join(app.root_path,'uploads')
@app.route('/upload',methods=['GET','POST'])
def upload_image():
    form=UploadForm()
    if form.validate_on_submit():
        f=form.photo.data
        ext=os.path.splitext(f.filename)[1]
        filename=uuid.uuid4().hex+ext
        f.save(os.path.join(app.root_path,'upload',filename))
        return redirect(url_for('show_image',filename=filename))
    return render_template("upload.html",form=form)
@app.route('/show_image/<filename>')
def show_image(filename):
    return render_template("show_image.html",filepath='/upload/'+filename)

@app.route("/upload/<path:filename>")
def get_file(filename):
    return send_from_directory(os.path.join(app.root_path,"upload"),filename)

from wtforms import  StringField,PasswordField,BooleanField,SubmitField
from flask_ckeditor import CKEditorField,CKEditor
from wtforms.validators import DataRequired,Length

class RichTextForm(FlaskForm):
    title=StringField("tile",validators=[DataRequired(),Length(1,50)])
    body=CKEditorField("body",validators=[DataRequired()])
    save=SubmitField("save")
    publish = SubmitField("publish")
ckeditor=CKEditor(app)

@app.route('/ckeditor',methods=['GET','POST'])
def test_ckeditor():
    form=RichTextForm()
    if form.validate_on_submit():
        if form.publish.data:
            title=form.title.data
            body=form.body.data
            return render_template("post_rich.html", title=title, body=body)
        elif form.save.data:
            print("dianjilesave")

    return  render_template("ckeditor.html",form=form)
