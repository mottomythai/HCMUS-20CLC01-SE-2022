from . import views
from django.urls import path


urlpatterns = [
    path('', views.home, name=''),
    path("contact/", views.contact, name='contact'),
    path("login/", views.login,name='login'),
    path("guide/", views.guide,name='guide'),
    path("product_item/", views.product_item,name='product_item'),
]
