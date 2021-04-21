from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.views import LoginView
from blog.models import Article
from mysite.forms import UserCreationForm, ProfileForm
from django.contrib import messages

def index(request):
  objs = Article.objects.all()[:3]
  context = {
    'title': 'Rrally Site',
    'articles': objs,
  }
  return render(request, 'mysite/index.html', context)

class Login(LoginView):
  template_name = 'mysite/auth.html'

  def form_valid(self, form):
    messages.success(self.request, 'ログイン完了！！！')
    return super().form_valid(form)

  def form_invalid(self, form):
    messages.error(self.request, 'エラーログイン失敗')
    return super().form_invalid(form)

def signup(request):
  context = {}
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save(commit=False)
      # user.is_active = False
      user.save()
      messages.success(request, '登録完了！！！')
      return redirect('/')
  return render(request, 'mysite/auth.html', context)

def mypage(request):
  context = {}
  if request.method == 'POST':
    form = ProfileForm(request.POST)
    if form.is_valid():
      profile = form.save(commit=False)
      profile.user = request.user
      profile.save()
      messages.success(request, '更新完了！！！')

  return render(request, 'mysite/mypage.html',context)