from django.contrib import admin
from .models import Book, Student

# Register your models here.
# admin.site.register(Book)
admin.site.register(Student)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'no_of_pages', 'date']
    list_editable = [ ]
    list_filter = ['date']
    list_per_page = 2
    search_fields = ['title', 'body', 'author']