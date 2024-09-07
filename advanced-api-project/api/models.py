"""
Author Model: Represents an author with a name.
Book Model: Represents a book with a title, publication year, and an author (One-to-Many relationship).
"""


from django.db import models


# Author Model
class Author(models.Model):
    name = models.CharField(max_length=100)  # Field to store author's name

    def __str__(self):
        return self.name

# Book Model
class Book(models.Model):
    title = models.CharField(max_length=200)  # Field for book title
    publication_year = models.IntegerField()  # Field for year of publication
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)  # One-to-Many Relationship

    def __str__(self):
        return self.title
