from django.urls import path

from snippet import views

urlpatterns = [
    path('', views.SnippetIndex, name="snippet/index"),
    path('new/', views.SnippetNew, name="snippet/new"),
    path('create/', views.SnippetCreate, name="snippet/create"),
    path('detail/<int:snippet_id>/', views.SnippetDetail, name="snippet/detail"),
    path('edit/<int:snippet_id>/', views.SnippetEdit, name="snippet/edit"),
    path('update/<int:snippet_id>/', views.SnippetUpdate, name="snippet/update"),
]
