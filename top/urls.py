from django.urls import path

from top import views

urlpatterns = [
    path('', views.top, name="top/index"),
]
