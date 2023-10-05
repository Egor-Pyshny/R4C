from django.urls import path

from customers import views

urlpatterns = [
    path("make_order/", views.make_order),
]
