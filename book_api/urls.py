from django.urls import path 
from . import views 


urlpatterns = [
    path('', views.getBooks),
    path('authors/', views.getAuthors),
    path('author/', views.addAuthor),
    path('book/', views.addBook),
    path('book/<str:id>/', views.listBook),
    path('author/<str:id>/', views.listAuthor),
    path('update-author/<str:id>/', views.updateAuthor),
    path('update-book/<str:id>/',views.updateBook)
]