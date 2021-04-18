from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.views import LoginView
from blog.models import Article

def index(request):
  objs = Article.objects.all()
  context = {
    'title': 'Rrally Site',
    'articles': objs,
  }
  return render(request, 'mysite/index.html', context)

class Login(LoginView):
  template_name = 'mysite/login.html'