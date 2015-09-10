# -*- coding:utf-8 -*-
#coding=utf-8
__author__ = 'lihui'

from flask_wtf import Form
from wtforms import TextAreaField,SubmitField,validators
from wtforms.validators import Required

class InceptionTableStructure(Form):
    table_name = TextAreaField('请输入需要评审的表结构: ', validators=[Required()])
    submit = SubmitField('Submit')
