from django.contrib import admin
from . import views
from django.urls import path
from accouts import views as accout 
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.home, name=''),
    path("contact/", views.contact, name='contact'),
    path("login/", views.loginpage,name='login'),
    path("logout/", views.logoutpage,name='logout'),
    path("user/", accout.infuser,name='user'),
    path("guide/", views.guide,name='guide'),
    path("login/", views.productitem,name='login'),
    path("product_item/", views.productitem,name='producitem'),
    path("password/", accout.PasswordChange,name='password'),
]
admin.site.site_header='Hi5'