from django.test import TestCase

# Create your tests here.
from django.urls import reverse

from books.models import Book
from users.models import CustomUser


class BookTestCase(TestCase):
    def test_no_books(self):
        response=self.client.get(reverse('books:list'))

        self.assertContains(response,'No books found')
    def test_books_list(self):
        book1= Book.objects.create(title='books1',description='books1',isbn='1234')
        book2=Book.objects.create(title='books2',description='books2',isbn='1234')
        book3=Book.objects.create(title='books3',description='books3',isbn='12344')
        response=self.client.get(reverse('books:list') + '?page_size=2')


        for book in [book1,book2]:
            self.assertContains(response,book.title)
        self.assertNotContains(response,book3.title)
        response=self.client.get(reverse('books:list') + '?page=2&page_size=2')
        self.assertContains(response,book3.title)
    def test_detail_page(self):
        book= Book.objects.create(title='books1',description='books1',isbn='1234')
        response=self.client.get(reverse('books:detail' , kwargs={'id':book.id}))
        self.assertContains(response,book.title)
        self.assertContains(response,book.description)
    def test_book_search(self):
        book1 = Book.objects.create(title='sport', description='books1', isbn='1234')
        book2 = Book.objects.create(title='diniy', description='books2', isbn='1234')
        book3 = Book.objects.create(title='dunyoviy', description='books3', isbn='12344')

        response=self.client.get(reverse('books:list') + '?q=sport')
        self.assertContains(response,book1.title)
        self.assertNotContains(response,book2.title)
        self.assertNotContains(response,book3.title)

        response=self.client.get(reverse('books:list') + '?q=Diniy')
        self.assertContains(response,book2.title)
        self.assertNotContains(response,book1.title)
        self.assertNotContains(response,book3.title)

        response=self.client.get(reverse('books:list') + '?q=Dunyoviy')
        self.assertContains(response,book3.title)
        self.assertNotContains(response,book1.title)
        self.assertNotContains(response,book2.title)


class BookReviewTestCase(TestCase):
    def test_add_review(self):
        book= Book.objects.create(title='books1',description='books1',isbn='1234')
        user = CustomUser.objects.create(
            username='Nodirbek', first_name='Nodirbek1', last_name='Hakimjonov', email='admin@gmail.com'
        )
        user.set_password('somepass')
        user.save()

        self.client.login(username='Nodirbek', password='somepass')

        self.client.post(reverse('books:reviews', kwargs={'id':book.id}),data={
            'stars_given':3,
            'comment':'Nice book'
        })
        book_reviews=book.bookreview_set.all()

        self.assertEqual(book_reviews.count(), 1)
        self.assertEqual(book_reviews[0].stars_given, 3)
        self.assertEqual(book_reviews[0].comment, 'Nice book')
        self.assertEqual(book_reviews[0].book, book)
        self.assertEqual(book_reviews[0].user, user)





