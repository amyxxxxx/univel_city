from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=300)
    no_of_pages = models.IntegerField(default=10)
    author = models.CharField(max_length=300)
    body = models.TextField()
    isbn = models.CharField(max_length=20, null=True, blank=True)
    date = models.DateTimeField()

    def __str__(self):
        return self.title

class Student(models.Model):
    name = models.CharField(max_length=25)
    age = models.PositiveIntegerField()
    course = models.CharField(max_length=25)
    date_of_birth = models.DateField()
    bio = models.TextField()

    def __str__(self):
        return self.name