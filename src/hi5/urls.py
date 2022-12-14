from . import views
from django.urls import path


urlpatterns = [
    path("", views.home),
    path("contact/", views.contact),
    path("login/", views.login),
    path("guide/", views.guide),
    path("product_item/", views.product_item),
    
]
