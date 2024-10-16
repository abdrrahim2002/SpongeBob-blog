from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home),
    path('all_posts', views.all_posts),
    path('<number>', views.first)
]
