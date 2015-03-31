views.py
________
from django.http import HttpResponse
from datetime import *
from django.shortcuts import render
from app.models import Post

# Create your views here.
def index(request):
	post_list = Post.objects.all()
	return render(request,'index.html',{'display_word':post_list})
global post
post = Post.objects.all()
def post_detail(request,id):
	return render(request,'post.html',{'post':post[int(id)]})
_______
template -> template/index.html
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8"/>
	<title>Hello world</title>
</head>
<body>
	{% for i in display_word %}
	<p style="color: LightSeaGreen">標題: {{i}} ,內容: {{i.content}},地點: {{i.location}}</p>
	{% endfor %}
</body>
</html>
__________
template/post.html -->
<!DOCTYPE html>
<html>
<head>
	<meta charset='utf-8' />
	<title>{{ post.title }}</title>
</head>
<body>
<p style='color:LightSeaGreen'>標題: {{post.title}} ,內容: {{post.content}} ,地點: {{post.location}}</p>
</body>
</html>
__________
settings.py
add in INSTALLED_APPS = (...) add in final line: 'app' <- your project name

and add in file final line
#Template
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'Templates').replace('\\', '/'),
)
_________
models.py
from django.db import models

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField(blank=True)
	photo = models.URLField(blank=True)
	location = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title
____________
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Filckr.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','app.views.index'),
    url(r'^post/(?P<id>\d+)/$', 'app.views.post_detail',name='post_detail'),
)
________
command line: python manage.py migrate (if you're not first time run the command ,enter: mkaemigrations)
and test shell: python manage.py shell:
>>> from app.models import Post
>>> Post.objects.create(title="xx",content="xx",location="xx")
________
Now you can run server -> python manage.py runserver
