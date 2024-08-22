from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    def __str__(self):
        return f"{self.title} by {self.author}"

