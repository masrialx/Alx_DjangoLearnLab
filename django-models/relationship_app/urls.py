from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),  # Use Django’s built-in login view
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),  # Use Django’s built-in logout view
    path('register/', views.user_register, name='register'),  # Keep custom register view
]
