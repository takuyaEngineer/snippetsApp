from django.urls import path

from snippet import views

urlpatterns = [
    path('', views.SnippetIndex, name="snippet/index"),
    path('new/', views.SnippetNew, name="snippet/new"),
    path('create/', views.snippetCreate, name="snippet/create"),
    path('<int:snippet_id>/', views.snippet_detail, name="snippets_detail"),
    path('edit/<int:snippet_id>/', views.snippet_edit, name="snippets_edit"),
]
