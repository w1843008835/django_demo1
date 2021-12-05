Django基本命令  
django-admin  
django-admin startproject 【projectname】 #创建一个django项目  
python manage.py startapp 【appname】 #创建一个django应用  

python manage.py runserver #本地简易运行django项目  
shell #进入django项目的python shell环境  
test #执行django用例测试  
python manage.py　makemigrations #创建模型变更的迁移文件  
python manage.py　migrate #执行上一个命令创建的迁移文件  
dumpdata #把数据库数据导出到文件  
loaddata #把文件数据导入到数据库  

项目目录
项目配置文件：settings.py  
项目路由配置文件：urls.py    
项目管理文件：manage.py    

应用目录  
视图处理的地方：views.py  
定义应用模型的地方:models.py  
定义admin模块管理对象的地方:admin.py  
声明应用的地方：apps.py  
编写应用测试用例的地方：tests.py  
管理应用路由的地方（自行创建）：urls.py  
 
模型层定义字段  
数字类型：IntegerField  
文本类型：TextField  
日期类型：DateTimeField  
自增id：AutoField  
主键定义：primary_key  

进入django shell控制台：python manage.py shell  
导入models：from blog.models import Articles  
声明对象：a = Articles()  
设置属性： a.title = 'Test django shell'  
保存到数据库：a.save()  
查询所有数据：articles = Articles.objects.all()  
打印数据： print(articles[0].title)  

admin模块  
创建超级用户：python manage.py createsuperuser  
admin　password  
启动服务：python manage.py runserver  
admin登录：http://127.0.0.1:8000/admin/  
admin.py里面把数据模型注册到admin管理模块：  
from .models import Articles  
admin.site.register(Articles)  




