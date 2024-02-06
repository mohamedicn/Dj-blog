from django.urls import path 
from .views import *
from . import views
app_name='blog'


urlpatterns = [
    path('',views.home,name='home'),
    path('<slug:slug>',views.blog_content,name='blog_content'),
    path('is-like/<slug:slug>',views.is_like,name='is_like'),
    path('is-likeee/<slug:slug>',views.is_like_blog,name='is_like_blog'),
    path('add-comment/<slug:slug>',views.add_comment,name='add_comment'),
    path('blog/<slug:slug>',views.blog_user,name='blog_user'),
    path('blog/follow/<slug:slug>',views.add_follow,name='add_follow'),
    path('blog/un-follow/<slug:slug>',views.un_follow,name='un_follow'),
    
    path('create/<slug:slug>/create-blog',Upload_post.as_view(),name='create_blog'),
    
    path('all/user',views.all_user,name='all_user'),
    
]
