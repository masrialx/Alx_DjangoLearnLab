# LibraryProject/bookshelf/forms.py

from django import forms
from .models import Book  # Import your model if needed

class ExampleForm(forms.Form):
    title = forms.CharField(max_length=200, label='Book Title')
    author = forms.CharField(max_length=100, label='Author')
    publication_year = forms.IntegerField(label='Publication Year')
    # You can add more fields as needed

    def clean_publication_year(self):
        year = self.cleaned_data.get('publication_year')
        if year < 0:
            raise forms.ValidationError("Publication year cannot be negative.")
        return year
