## Create

**Command:**
```python
from bookshelf.models import Book

# Using Book.objects.create() to create and save a new book in one step
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
