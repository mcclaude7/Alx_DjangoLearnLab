from relationship_app.models import Author, Book, Library, Librarian

<<<<<<< HEAD
author = Author.objects.get(name="Author Name")
books_by_author = Book.objects.filter(author=author)

library = Library.objects.get(name="Library Name")
books_in_library = library.books.all()

library = Library.objects.get(name="Library Name")
books_in_library = library.books.all()
=======
# Query all books by a specific author
def books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    return Book.objects.filter(author=author)

# List all books in a library
def books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()

# Retrieve the librarian for a library
def librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.Librarian
>>>>>>> 23e1809ff25d80895580e7745bbc99bab855e18d
