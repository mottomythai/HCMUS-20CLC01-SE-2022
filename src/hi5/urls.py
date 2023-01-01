from django.contrib import admin
from . import views
from django.urls import path


urlpatterns = [
    path('', views.home, name=''),
    path('', views.home, name=''),
    path("contact/", views.contact, name='contact'),
    path("login/", views.login,name='login'),
    path("guide/", views.guide,name='guide'),
     path("login/", views.productitem,name='login'),
    path("product_item/", views.productitem,name='producitem'),
]
admin.site.site_header='Hi5'