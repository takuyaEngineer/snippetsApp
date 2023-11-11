from django.urls import path

from snippets import views

urlpatterns = [
    path('new/', views.snippet_new, name="snippets_new"),
    path('<int:snippet_id>/', views.snippet_detail, name="snippets_detail"),
    path('edit/<int:snippet_id>/', views.snippet_edit, name="snippets_edit"),
]
