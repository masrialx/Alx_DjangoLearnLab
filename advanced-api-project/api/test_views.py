from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book, Author

class BookTests(APITestCase):

    def setUp(self):
        # Set up initial test data
        self.author = Author.objects.create(name='Test Author')
        self.book = Book.objects.create(
            title='Test Book',
            publication_year=2023,
            author=self.author
        )
        self.book_url = reverse('book-list')  # URL for listing and creating books
        self.book_detail_url = reverse('book-detail', args=[self.book.id])  # URL for retrieving, updating, and deleting a book
        self.client.login
    def test_create_book(self):
        # Test the creation of a new book
        data = {
            'title': 'New Book',
            'publication_year': 2024,
            'author': self.author.id
        }
        response = self.client.post(self.book_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.get(id=response.data['id']).title, 'New Book')
        self.client.login
    def test_retrieve_book(self):
        # Test retrieving a single book's details
        response = self.client.get(self.book_detail_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book.title)
        self.assertEqual(response.data['publication_year'], self.book.publication_year)
        self.client.login
    def test_update_book(self):
        # Test updating an existing book
        data = {
            'title': 'Updated Book',
            'publication_year': 2025,
        }
        response = self.client.patch(self.book_detail_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Updated Book')
        self.client.login
    def test_delete_book(self):
        # Test deleting a book
        response = self.client.delete(self.book_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)
       
    def test_filter_books(self):
        # Test filtering books by title
        response = self.client.get(self.book_url, {'title': 'Test Book'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_search_books(self):
        # Test searching books by title
        response = self.client.get(self.book_url, {'search': 'Test Book'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_ordering_books(self):
        # Test ordering books by publication_year
        response = self.client.get(self.book_url, {'ordering': 'publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'][0]['publication_year'], 2023)

    def test_unauthenticated_access(self):
        # Test access control for unauthenticated users
        self.client.logout()
        response = self.client.post(self.book_url, {'title': 'New Book'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
