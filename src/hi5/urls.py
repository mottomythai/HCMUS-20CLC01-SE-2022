from . import views
from django.urls import path


urlpatterns = [
    path("", views.home),
    path("product/", views.product),
    path("customer/", views.customer),
]
