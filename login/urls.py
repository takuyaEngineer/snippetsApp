from django.urls import path

from login import views

urlpatterns = [
    path('', views.LoginIndex, name="login/index"),
]
