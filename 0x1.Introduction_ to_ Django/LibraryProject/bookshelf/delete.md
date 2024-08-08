## Delete

**Command:**
```python
from bookshelf.models import Book

# Retrieve all books with the title "1984"
books = Book.objects.filter(title="1984")

# Delete all books with the title "1984"
books.delete()
