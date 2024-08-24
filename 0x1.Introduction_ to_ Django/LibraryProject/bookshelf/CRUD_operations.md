### Command:
```python
from bookshelf.models import Book

new_book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)
new_book.save()


## Retrieve Operation

### Command:
```python
new_book = Book.objects.get(id=1)
print(new_book.title, new_book.author, new_book.publication_year)


## Update Operation

### Command:
```python
new_book.title = "Nineteen Eighty-Four"
retrieved_book.save()
print(retrieved_book.title)

## Delete Operation

### Command:
```python
retrieved_book.delete()

all_books = Book.objects.all()
print(all_books)




  

 