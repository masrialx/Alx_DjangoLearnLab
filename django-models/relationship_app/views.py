# relationship_app/views.py

from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book 
from .models import Library

def list_books(request):
    # Retrieve all books from the database
    books = Book.objects.all()
    # Render the list_books.html template with the books data
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    # Specify the model to use for the detail view
    model = Library
    # Specify the template name to render
    template_name = 'relationship_app/library_detail.html'
    # Specify the context object name for the template
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        # Get the context data for the detail view
        context = super().get_context_data(**kwargs)
        # Add all books related to this library to the context
        context['books'] = self.object.books.all()  # Assumes a reverse relation from Library to Book
        return context
