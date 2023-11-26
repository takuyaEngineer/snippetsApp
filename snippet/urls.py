from django.urls import path

from snippet import views

urlpatterns = [
    path('', views.SnippetIndex, name="snippet/index"),
    path('new/', views.SnippetNew, name="snippet/new"),
    path('create/', views.snippetCreate, name="snippet/create"),
    path('detail/<int:snippet_id>/', views.snippetDetail, name="snippet/detail"),
    path('edit/<int:snippet_id>/', views.snippetEdit, name="snippet/edit"),
    path('update/', views.snippetEdit, name="snippet/edit"),
]
