from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('login/', views.user_login, name='login'),  # Use your custom login view
    path('logout/', views.user_logout, name='logout'),  # Use your custom logout view
    path('register/', views.user_register, name='register'),  # Use your custom register view
]
