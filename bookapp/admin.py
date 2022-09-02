from django.contrib import admin
from .models import Author, Book
# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'date_created',
    )
    
class BookAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'isbn',
        'author',
        'date_created',
    )

admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)