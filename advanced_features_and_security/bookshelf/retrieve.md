## Retrieve

**Command:**
```python
from bookshelf.models import Book

# Retrieve all books
books = Book.objects.all()
for b in books:
    print(b.title, b.author, b.publication_year)

# Retrieve a specific book by title
book = Book.objects.get(title="1984")
print(book.title, book.author, book.publication_year)
