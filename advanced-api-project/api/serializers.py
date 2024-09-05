
from rest_framework import serializers
from .models import Author, Book
from datetime import date

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        if value > date.today().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):  # Ensure this name matches what you import
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']




