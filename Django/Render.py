Django
============
modify setting.py -->

add in final line:
#Template
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'Templates').replace('\\', '/'),
)

-----------
mkdir in setting.py directory -> "Templates" and add new file rename "index.html"
-----------

modify index.html -->
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8"/>
	<title>Hello world</title>
</head>
<body>
	<p style="color: LightSeaGreen"> {{ display_word }} 123</p>
</body>
</html>
-----------

and modify views.py

from django.http import HttpResponse
from datetime import *
from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request,'index.html',{'display_word':datetime.now()})
