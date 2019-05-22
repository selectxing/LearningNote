# 开始Django

[教程地址](https://www.runoob.com/django/django-first-app.html)

- Django是一个开放源代码的Web应用框架，由Python写成。
- Django遵守BSD版权，初次发布于2005年7月, 并于2008年9月发布了第一个正式版本1.0。
- Django采用了MVC的软件设计模式。

## 安装

使用pip安装Django

```
pip install django
```

安装后，将以下目录添加至系统环境变量：

- *python目录\Lib\site-packages\django*
- *python目录\Scripts*

## 验证

```python
import django
django.get_version()
```

可以输出正确的Django版本号则安装成功。

## HelloWorld

使用管理工具django-amdin创建第一个Django程序。新建项目路径默认为：*C:\Users\Administrator*。

```python
django-admin startproject HelloWorld
```

HelloWorld目录结构：

- HelloWorld: 项目的容器。
- manage.py: 一个实用的命令行工具，可让你以各种方式与该 Django 项目进行交互。
- HelloWorld/\__init__.py: 一个空文件，告诉 Python 该目录是一个 Python 包。
- HelloWorld/settings.py: 该 Django 项目的设置/配置。
- HelloWorld/urls.py: 该 Django 项目的 URL 声明; 一份由 Django 驱动的网站"目录"。
- HelloWorld/wsgi.py:0 一个 WSGI 兼容的 Web 服务器的入口，以便运行你的项目。

cd进入该目录并启动服务器，浏览器输入*127.0.0.1:8000*，即可访问django网页。*注：网页代码修改后，无需手动重启服务器。*

```python
python3 manage.py runserver 0.0.0.0:8000
```
创建view.py文件

```python
from django.http import HttpResponse
def hello(request):
    return HttpResponse("hello world")
```

修改urls.py文件

```python
from django.urls import path
from . import view
urlpatterns = [
    path('hello/', view.hello),
]
```

path()方法可以接收四个参数，分别是两个必选参数：route、view 和两个可选参数：kwargs、name

```
path(route, view, kwargs=None, name=None)
```

- route: 字符串，表示 URL 规则，与之匹配的 URL 会执行对应的第二个参数 view。
- view: 用于执行与正则表达式匹配的 URL 请求。
- kwargs: 视图使用的字典类型的参数。
- name: 用来反向获取 URL。

## Web应用程序实操

[教程：在Django中构建Oracle支持的Web应用程序](https://www.oracle.com/technetwork/articles/vasiliev-django-100817-zhs.html)

*Django基于将Web应用程序逻辑分为模型、视图和模板的概念，因此有效地将业务逻辑和展示分离开来。通常，这类似于当今许多其他 Web框架中使用的模型-视图-控制器 (MVC) 范例。然而，在Django中，视图更像控制器，介于模型和模板之间。而Django模板更接近于MVC视图，因为这些模板负责使用从模型中获得的数据生成适当的用户界面。*

![Django支持的web程序](https://www.oracle.com/ocom/groups/public/@otn/documents/digitalasset/113150.gif)

### 模型

#### 数据库配置

settings.py中DATABASES的Oracle配置

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}
```

#### 定义模型

创建app

```python
django-admin startapp TestModel
```

TestModel目录结构：

- models.py :在 django.db.models.Model 类之上构建的 Python 类，每个模型都映射到一个数据库表。

- views.py :包含视图（Python 函数），每个视图返回 HttpResponse 对象，或者引发 HTTP 异常。

### 模板

模板用于分离文档的表现形式和内容。