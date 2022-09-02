from django.db import models 

# custom queryset for app
class AppQuerySet(models.QuerySet):
    def get_single_book(self,id):
        if id is None:
            self.none()
        return self.get(id=id)
    
    def get_single_author(self,id):
        if id is None:
            self.none()
        return self.get(id=id)

# manager for book model
class BookManager(models.Manager):
    
    def get_queryset(self):
        return AppQuerySet(self.model, using=self._db)
    
    def get_single_book(self,id):
        return self.get_queryset().get_single_book(id=id)

# manager for author model   
class AuthorManager(models.Manager):
    
    def get_queryset(self):
        return AppQuerySet(self.model, using=self._db)
    
    def get_single_author(self,id):
        return self.get_queryset().get_single_author(id=id)