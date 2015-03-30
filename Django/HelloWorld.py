django
=======
django-admin startproject demoproj

cd demoproj

python manage.py startapp hello
-----------------
modify hello/views.py -->

from django.http import HttpResponse

def index(request):
	return HttpResponse("Hello World!")
	
-----------------
modify demoproj/urls.py -->

add line after "url(r'^admin/', include(admin.site.urls)),", new line:

url(r'^hello/$', 'AEEP.views.index'),

-----------------
python manage.py runserver
