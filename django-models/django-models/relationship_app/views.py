from django.shortcuts import render
<<<<<<< HEAD

# Create your views here.
=======
from .models import Book
from django.views.generic import DetailView
from .models import Library

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'


def list_books(request):
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})



>>>>>>> 23e1809ff25d80895580e7745bbc99bab855e18d
