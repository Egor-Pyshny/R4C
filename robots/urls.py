from django.urls import path

from robots import views

urlpatterns = [
    path("add/", views.add),
    path("report/", views.report),
]
