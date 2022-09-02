from dataclasses import field
from rest_framework import serializers 
from bookapp.models import Author, Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book 
        fields = ['id','name','isbn','author']
        
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author 
        fields = ['id','first_name','last_name']