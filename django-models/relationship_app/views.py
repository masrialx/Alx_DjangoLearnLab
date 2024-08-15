# relationship_app/views.py

from django.shortcuts import render
from .models import Book
from django.views.generic.detail import DetailView
from .models import Library


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'list_books.html.html'
    context_object_name = 'library'