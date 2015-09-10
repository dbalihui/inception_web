# -*- coding:utf-8 -*-
#coding=utf-8
__author__ = 'lihui'

from app import app
from flask import render_template, flash, redirect,session,url_for,request
from forms import InceptionTableStructure
import MySQLdb
import inception

#首页
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

#Inception_表结构评审
@app.route('/inception_table_structure',methods=['GET','POST'])
def inception_table_structure():
    form = InceptionTableStructure()
    sql_review = {}
    if request.method == "POST":
        mysql_structure = request.form.get('mysql_structure')
        sql_review = inception.table_structure(mysql_structure)
        return render_template('dba_tool/inception_table_structure.html',sql_review = sql_review,abc = mysql_structure)
    return render_template('dba_tool/inception_table_structure.html')
