from django.urls import path

from maintenance import views

urlpatterns = [
    path('except/', views.Except, name="maintenance/except"),
]
