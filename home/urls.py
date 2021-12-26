from home import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('blogHome', views.blogHome, name='blogHome'),
    path('blogPost/<slug>', views.blogPost, name='blogPost'),
    path('register', views.register, name='register'),
    path('login', views.login_, name='login'),
    path('logout', views.logout_, name='logout'),
    path('search', views.search, name='search'),
]