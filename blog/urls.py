from . import views
from django.urls import path

urlpatterns = [

    path('post_comment', views.post_comment, name="post_comment"),
    path('<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('', views.blog_home, name='blog_home'),

]
