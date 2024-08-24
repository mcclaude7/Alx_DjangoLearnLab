## Retrieve Operation

### Command:
```python
from bookshelf.models import Book

book2 = Book.objects.get(id=new_book.id)
print(book2.title, book2.author, book2.publication_year)
