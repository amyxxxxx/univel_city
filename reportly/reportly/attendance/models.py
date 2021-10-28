from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=25)
    age = models.PositiveIntegerField()
    course = models.CharField(max_length=25)
    date_of_birth = models.DateField()
    bio = models.TextField()

    def __str__(self):
        return self.name

# class Book(models.Model):
#     title = models.CharField(max_length=300)
#     no_of_pages = models.IntegerField(default=10)
#     author = models.CharField(max_length=300)
#     student = models.OneToOneField(Student, on_delete=models.CASCADE)
#     body = models.TextField()
#     isbn = models.CharField(max_length=20, null=True, blank=True)
#     date = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.title

class Book(models.Model):
    title = models.CharField(max_length=300)
    no_of_pages = models.IntegerField(default=10)
    author = models.CharField(max_length=300)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="books")
    body = models.TextField()
    isbn = models.CharField(max_length=20, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title