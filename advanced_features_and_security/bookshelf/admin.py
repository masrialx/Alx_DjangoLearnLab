# bookshelf/admin.py
from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Ensure this matches your model
    list_filter = ('publication_year',)  # Ensure this matches your model
    search_fields = ('title', 'author')  # Ensure this matches your model
