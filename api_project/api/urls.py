#from .views import BookList
#pythonCopy codefrom django.urls import path
from django.urls import path

#urlpatterns = [
    #path('books/', BookList.as_view(), name = 'book-list'),
#]
#pythonCopy codefrom django.urls import path
from .views import BookListCreateAPIView

urlpatterns = [
    path("books/", BookListCreateAPIView.as_view(), name="book_list_create"),
]

