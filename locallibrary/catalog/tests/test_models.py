from django.test import TestCase
from django import forms

from catalog.models import Author, Book, BookInstance, Genre

# Create your tests here.
class AuthorModelTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Author.objects.create(first_name='Big', last_name='Bob')

    def test_first_name_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('first_name').verbose_name
        self.assertEqual(field_label, 'first name')

    def test_last_name_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('last_name').verbose_name
        self.assertEqual(field_label, 'last name')

    def test_date_of_birth_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('date_of_birth').verbose_name
        self.assertEqual(field_label, 'date of birth')

    def test_date_of_death_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('date_of_death').verbose_name
        self.assertEqual(field_label, 'Died')

    def test_first_name_max_length(self):
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field('first_name').max_length
        self.assertEqual(max_length, 100)

    def test_last_name_max_length(self):
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field('last_name').max_length
        self.assertEqual(max_length, 100)

    def test_object_name_is_last_name_comma_first_name(self):
        author = Author.objects.get(id=1)
        expected_object_name = f'{author.first_name}, {author.last_name}'
        self.assertEqual(str(author), expected_object_name)

    def test_get_absolute_url(self):
        author = Author.objects.get(id=1)
        self.assertEqual(author.get_absolute_url(), '/catalog/author/1')

# class BookModelTest(TestCase):
    
#     @classmethod
#     def setUpTestData(cls):
#         # Set up non-modified objects used by all test methods
#         author = Author.objects.create(first_name='John', last_name='Doe')
#         genre = Genre.objects.create(name='Science Fiction')
#         book = Book.objects.create(
#             title='Test Book',
#             summary='A test book summary.',
#             isbn='1234567890123',
#             author=author,
#         )
#         book.genre.add(genre)

#     def test_title_label(self):
#         book = Book.objects.get(id=1)
#         field_label = book._meta.get_field('title').verbose_name
#         self.assertEqual(field_label, 'title')

#     def test_summary_label(self):
#         book = Book.objects.get(id=1)
#         field_label = book._meta.get_field('summary').verbose_name
#         self.assertEqual(field_label, 'summary')

#     def test_isbn_label(self):
#         book = Book.objects.get(id=1)
#         field_label = book._meta.get_field('isbn').verbose_name
#         self.assertEqual(field_label, 'ISBN')

#     def test_title_max_length(self):
#         book = Book.objects.get(id=1)
#         max_length = book._meta.get_field('title').max_length
#         self.assertEqual(max_length, 200)

#     def test_isbn_max_length(self):
#         book = Book.objects.get(id=1)
#         max_length = book._meta.get_field('isbn').max_length
#         self.assertEqual(max_length, 13)

#     def test_object_name_is_title(self):
#         book = Book.objects.get(id=1)
#         expected_object_name = book.title
#         self.assertEqual(str(book), expected_object_name)

#     def test_get_absolute_url(self):
#         book = Book.objects.get(id=1)
#         self.assertEqual(book.get_absolute_url(), '/catalog/book/1')

# class BookInstanceModelTest(TestCase):
    
#     @classmethod
#     def setUpTestData(cls):
#         # Set up non-modified objects used by all test methods
#         author = Author.objects.create(first_name='Jane', last_name='Smith')
#         book = Book.objects.create(
#             title='Another Test Book',
#             summary='Another test book summary.',
#             isbn='9876543210987',
#             author=author,
#         )
#         cls.book_instance = BookInstance.objects.create(
#             book=book,
#             imprint='First Edition',
#             status='a',
#         )

#     def test_imprint_label(self):
#         book_instance = BookInstanceModelTest.book_instance
#         field_label = book_instance._meta.get_field('imprint').verbose_name
#         self.assertEqual(field_label, 'imprint')

#     def test_status_label(self):
#         book_instance = BookInstanceModelTest.book_instance
#         field_label = book_instance._meta.get_field('status').verbose_name
#         self.assertEqual(field_label, 'status')

#     def test_object_name_is_id(self):
#         book_instance = BookInstanceModelTest.book_instance
#         expected_object_name = str(book_instance.id)
#         self.assertEqual(str(book_instance), expected_object_name)

#     def test_is_overdue_property(self):
#         book_instance = BookInstanceModelTest.book_instance
#         book_instance.due_back = None
#         self.assertFalse(book_instance.is_overdue)
#         import datetime
#         book_instance.due_back = datetime.date.today() - datetime.timedelta(days=1)
#         self.assertTrue(book_instance.is_overdue)
#         book_instance.due_back = datetime.date.today() + datetime.timedelta(days=1)
#         self.assertFalse(book_instance.is_overdue)

# class GenreModelTest(TestCase):
    
#     @classmethod
#     def setUpTestData(cls):
#         # Set up non-modified objects used by all test methods
#         Genre.objects.create(name='Fantasy')

#     def test_name_label(self):
#         genre = Genre.objects.get(id=1)
#         field_label = genre._meta.get_field('name').verbose_name
#         self.assertEqual(field_label, 'name')

#     def test_name_max_length(self):
#         genre = Genre.objects.get(id=1)
#         max_length = genre._meta.get_field('name').max_length
#         self.assertEqual(max_length, 200)

#     def test_object_name_is_name(self):
#         genre = Genre.objects.get(id=1)
#         expected_object_name = genre.name
#         self.assertEqual(str(genre), expected_object_name)

#     def test_get_absolute_url(self):
#         genre = Genre.objects.get(id=1)
#         self.assertEqual(genre.get_absolute_url(), '/catalog/language/1') 


class RenewBookForm(forms.Form):
    """Form for a librarian to renew books."""
    renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")

    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']

        # Check if date is not in the past.
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal in the past '))

        # Check if a date is in the allowed range (+4 weeks from today).
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))

        # Returning the cleaned data.
        return data
