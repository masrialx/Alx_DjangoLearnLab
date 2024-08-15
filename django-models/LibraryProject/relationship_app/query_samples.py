import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = author.books.all()
    for book in books:
        print(book.title)

# List all books in a library
def list_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    for book in books:
        print(book.title)

# Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = library.librarian
    print(librarian.name)

if __name__ == "__main__":
    print("Books by Author 'J.K. Rowling':")
    get_books_by_author('J.K. Rowling')
    
    print("\nBooks in Library 'Central Library':")
    list_books_in_library('Central Library')
    
    print("\nLibrarian for Library 'Central Library':")
    get_librarian_for_library('Central Library')
