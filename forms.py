1  #!/usr/bin/env python
2  # -*- coding:utf-8 -*- 
3  #宋丽丽

from flask import Flask
from flask_wtf import FlaskForm
from wtforms import  StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import DataRequired,Length
from flask_wtf.file import FileAllowed, FileField,FileRequired
from flask_ckeditor import CKEditorField,CKEditor
# import app
app=Flask(__name__)
app.config['WTF_I18N_ENABLED']=False
ckeditor=CKEditor(app)
class MyBaseForm(FlaskForm):
    class Meta:
        locals=['ZH']
class LoginForm(MyBaseForm):
    username=StringField('Username',validators=[DataRequired()])
    password=PasswordField('password',validators=[DataRequired(),Length(8,128)])
    rember=BooleanField('Rember me')
    sumbit=SubmitField("Login")
class RegisterForm(MyBaseForm):
    username=StringField('Username',validators=[DataRequired()])
    phone=StringField('Username',validators=[DataRequired()])
    password=PasswordField('password',validators=[DataRequired(),Length(8,128)])
    sumbit=SubmitField("Login")

class UploadForm(FlaskForm):
    ###服务器端验证类型FileAllowed
    ##render_kw 客户端验证
    photo=FileField('upload image:',validators=[FileRequired(),FileAllowed(['jpg','jpeg','png','gif'])],render_kw={'accept':'.jpg,.png,.jpeg'})
    submit=SubmitField("upload")

class RichTextForm(FlaskForm):
    title=StringField("tile",validators=[DataRequired(),Length(1,50)])
    body=CKEditorField("body",validators=[DataRequired()])
    submit=SubmitField()
