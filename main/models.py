from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    isbn = models.CharField(max_length=100)
    pages = models.IntegerField()

    def __str__(self):
        return self.title
    #To customize the table name
    class Meta:
        db_table = "book"

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    message = models.TextField()

    def __str__(self):
        return f'Feedback from {self.name} ({self.email})'
    
    class Meta:
        db_table = 'feedback'