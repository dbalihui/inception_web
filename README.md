# 数据库运维平台

## 已实现功能:
>表结构语法审核
## 环境配置
>python2.7 + flask
>
>先安装依赖模块
>
> pip install flask_wtf    
>
> pip install flask-script    
>
> pip install flask-debugtoolbar
>
> pip install MySQL-python
## 使用方法
>先将app目录中的inception.py文件里的账号密码改成自己的
>
>记得use sql_check这里要改成自己的数据库名字
>
>在inception_web目录下运行./run.py runserver --host 0.0.0.0
>
>使用浏览器访问你的IP  http://192.168.xx.xxx:5000/
>
>运行报错的话是因为没有安装flask组件，请使用pip install xx安装相关组件
