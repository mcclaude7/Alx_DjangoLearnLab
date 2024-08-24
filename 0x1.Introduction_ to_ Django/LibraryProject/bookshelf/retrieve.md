## Retrieve Operation

### Command:
```python
new_book = Book.objects.get(id=1)
print(new_book.title, new_book.author, new_book.publication_year)
