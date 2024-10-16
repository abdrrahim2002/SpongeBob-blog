from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_page(request):
  return HttpResponse('hello world')

def first(request, number):
  return HttpResponse(f' page{number}')


def home(request):
  return render(request, 'blog/homepage.html')

def all_posts(request):
  return render(request, 'blog/all_posts.html')