from rest_framework.response import Response
from rest_framework.decorators import api_view
from bookapp.models import Author, Book 
from .serializers import AuthorSerializer, BookSerializer
from book_api import serializers


# add author
@api_view(['POST'])
def addAuthor(request):

    # get data from request data
    authorserializer = AuthorSerializer(data=request.data)
    # call the valid method to valid posted data
    if authorserializer.is_valid():
        authorserializer.save()
    
    return Response(authorserializer.data)

# add book
@api_view(['POST'])
def addBook(request):
    # get data from post data
    bookserializer = BookSerializer(data=request.data)
    # validate request data
    if bookserializer.is_valid():
        bookserializer.save()
        
    return Response(bookserializer.data)

# get list of authors
@api_view(['GET'])
def getAuthors(request):
    
    author = Author.objects.all()
    authorserializer = AuthorSerializer(author, many=True)
    
    return Response(authorserializer.data)

# get list of books
@api_view(['GET'])
def getBooks(request):
    
    book = Book.objects.all()
    bookserializer = BookSerializer(book, many=True)
    
    return Response(bookserializer.data)


# get single book
@api_view(['GET'])
def listBook(request, id):
    
    # booklist = Book.objects.get_single_book(id=id)
    try:
        booklist = Book.objects.get_single_book(id=id)
    except Book.DoesNotExist:
        return Response(status=404)
    
    bookserializer = BookSerializer(booklist)
    
    return Response(bookserializer.data)

# get single author
@api_view(['GET'])
def listAuthor(request, id):
    
    # authorlist = Author.objects.get_single_author(id=id)
    try:
        authorlist = Author.objects.get_single_author(id=id)
    except Author.DoesNotExist:
        return Response(status=404)
    
    authorserializer = AuthorSerializer(authorlist)
    
    return Response(authorserializer.data)

# update author
@api_view(['PUT'])
def updateAuthor(request, id):
    
    try:
        authorlist = Author.objects.get_single_author(id=id)
    except Author.DoesNotExist:
        return Response(status=404)
    
    authorserializer = AuthorSerializer(instance=authorlist, data=request.data)
    if authorserializer.is_valid():
        authorserializer.save()
    
    return Response(authorserializer.data)

# update book
@api_view(['PUT'])
def updateBook(request, id):
    
    try:
        booklist = Book.objects.get_single_book(id=id)
    except Book.DoesNotExist:
        return Response(status=404)
    
    bookserializer = BookSerializer(instance=booklist, data=request.data)
    if bookserializer.is_valid():
        bookserializer.save()
    
    return Response(bookserializer.data)