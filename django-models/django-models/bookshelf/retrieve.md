## Retrieve Operation

### Command:
```python
from bookshelf.models import Book

book2 = Book.objects.get(id=new_book.id)
print(book2.title)
