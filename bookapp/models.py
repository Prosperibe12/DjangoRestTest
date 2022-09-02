from django.db import models
from .managers import *

# author model
class Author(models.Model):
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50,  null=False, blank=False)
    date_created = models.DateField(auto_now_add=True)
    
    # assign custom manager to default class manager
    objects = AuthorManager()
    
    def __str__(self):
        return f'{self.first_name}'
    
# book model
class Book(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    isbn = models.CharField(max_length=200, blank=True, null=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=False, blank=False)
    date_created = models.DateField(auto_now_add=True)
    
    # assign custom manager to default class manager
    objects = BookManager()
    
    def __str__(self):
        return f'{self.name}'
