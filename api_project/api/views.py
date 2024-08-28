from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .serializers import BookSerializer
from api.models import Book

class BookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
# Create your views here.
