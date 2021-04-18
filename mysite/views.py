from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Article

def index(request):
  objs = Article.objects.all()
  context = {
    'title': 'Rrally Site',
    'articles': objs,
  }
  return render(request, 'mysite/index.html', context)