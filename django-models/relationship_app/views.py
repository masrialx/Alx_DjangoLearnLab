# relationship_app/views.py

from django.shortcuts import render
from .models import Book, Library
from django.views.generic.detail import DetailView

def list_books(request):
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.all()  # Add this line to include all books in the context
        return context
