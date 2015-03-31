#views.py

from django.http import HttpResponse

def index(request):
  print (request.REQUEST) #Return Object type like:{}
  print (request.method) #GET or POST
