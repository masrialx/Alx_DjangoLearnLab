# api/urls.py

from django.db import router
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet

router = DefaultRouter()

router.register(r'books', BookViewSet)

# Include the router's URLs in the urlpatterns

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('', include(router.urls)),
]
