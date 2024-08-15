from django.urls import path
from . import views
from .views import list_books

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('login/', list_books, name='login'),
    path('logout/', list_books, name='logout'),
    path('register/', list_books, name='register'),
    path('library/<pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

]