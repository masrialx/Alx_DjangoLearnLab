# api/urls.py

from django.db import router
from django.urls import include, path
from .views import BookList

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('', include(router.urls)),
]
