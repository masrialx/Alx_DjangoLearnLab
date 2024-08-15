import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def query_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        print(f"Books by {author_name}:")
        for book in books:
            print(f"- {book.title}")
    except Author.DoesNotExist:
        print(f"No author found with the name {author_name}.")
def list_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        print(f"Books in {library_name}:")
        for book in books:
            print(f"- {book.title}")
    except Library.DoesNotExist:
        print(f"No library found with the name {library_name}.")
def retrieve_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)
        print(f"Librarian for {library_name}: {librarian.name}")
    except Library.DoesNotExist:
        print(f"No library found with the name {library_name}.")
    except Librarian.DoesNotExist:
        print(f"No librarian found for {library_name}.")
if __name__ == "__main__":
    print("Sample Queries:")
    print("\nQuery all books by a specific author:")
    query_books_by_author('Author Name')  # Replace 'Author Name' with an actual author name
    
    print("\nList all books in a library:")
    list_books_in_library('Library Name')  # Replace 'Library Name' with an actual library name
    
    print("\nRetrieve the librarian for a library:")
    retrieve_librarian_for_library('Library Name')  # Replace 'Library Name' with an actual library name
