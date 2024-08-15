import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def query_books_by_author(author_name):
    books = Book.objects.filter(author__name=author_name)
    for book in books:
        print(book.title)

def list_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    for book in books:
        print(book.title)

def retrieve_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = library.librarian
    print(librarian.name)

if __name__ == "__main__":
    print("Books by Author 'Author Name':")
    query_books_by_author('Author Name')
    print("\nBooks in Library 'Library Name':")
    list_books_in_library('Library Name')
    print("\nLibrarian for Library 'Library Name':")
    retrieve_librarian_for_library('Library Name')
