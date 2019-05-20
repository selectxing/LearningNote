# 开始Django

[教程地址](https://www.runoob.com/django/django-first-app.html)

## 安装

```python
pip install django
```

安装后，将以下目录添加至系统环境变量

- *python目录\Lib\site-packages\django*
- *python目录\Scripts*

## 验证

```python
import django
django.get_version()
```

可以输出正确的django版本号则安装成功

## 第一个Django程序

使用管理工具django-amdin创建第一个Django程序。新建项目路径默认为：*C:\Users\Administrator*

```python
django-admin startproject HelloWorld
```

cd进入该目录并启动服务器，浏览器输入*127.0.0.1:8000*，即可访问django网页

```python
python3 manage.py runserver 0.0.0.0:8000
```

