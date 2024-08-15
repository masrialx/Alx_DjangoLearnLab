## Delete

**Command:**
```python
from bookshelf.models import Book

# Retrieve and delete a specific book with the title "1984"
book = Book.objects.get(title="1984")
book.delete()

# Confirm deletion by trying to retrieve all books with the title "1984"
books = Book.objects.filter(title="1984")
print(books.count())  # Should print 0 if the book is deleted
