from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator,RegexValidator

# Create your models here.

from django.urls import reverse  # Used to generate urls by reversing the URL patterns
from datetime import datetime

class Genre(models.Model):
    """
    Model representing a book genre (e.g. Science Fiction, Non Fiction).
    """
    name = models.CharField(max_length=200, help_text="Enter a book genre (e.g. Science Fiction, French Poetry etc.)")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name


class Language(models.Model):
    """
    Model representing a Language (e.g. English, French, Japanese, etc.)
    """
    name = models.CharField(max_length=200,
                            help_text="Enter a the book's natural language (e.g. English, French, Japanese etc.)")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name

class Users(models.Model):
    """
    Model representing an author.
    """
    usn=models.CharField(max_length=10,validators=[RegexValidator(regex='^[0-9]+[a-zA-Z]*$')], error_messages={'invalid' : 'Invalid USN'},primary_key='true',blank='false')
    first_name = models.CharField(max_length=150,validators=[RegexValidator(regex='^[a-zA-Z]*$')], error_messages={'invalid' : 'Invalid First Name'})
    last_name = models.CharField(max_length=100,validators=[RegexValidator(regex='^[a-zA-Z]*$')], error_messages={'invalid' : 'Invalid Last Name'})
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=20)
    #user_type = models.CharField(max_length=20,null=True)
    user = models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    contact_no = models.IntegerField()
    #date_of_birth = models.DateField(null=True, blank=True)
    #date_of_death = models.DateField(null=True, blank=True)

    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('users-detail', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s, %s' % ((self.first_name,self.last_name))

    def get_user_type(self):
        if self.user_type == 'student':
            return 1
        else:
            return 0



class Book(models.Model):

    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author',null=True)
    summary = models.TextField(max_length=10000, help_text="Enter a brief description of the book")
    isbn = models.CharField('ISBN', max_length=13,
                            help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)
    publisher = models.ForeignKey('Publisher', on_delete=models.SET_NULL, null=True)
    image = models.ImageField(null=True)
    number_of_books = models.IntegerField(null=True,blank=True)
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)
    publication_date = models.DateField(null=True)
    request_user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    def display_genre(self):
        return ', '.join([genre.name for genre in self.genre.all()[:3]])
        display_genre.short_description = 'Genre'

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])

    def __str__(self):

        return self.title


import uuid  # Required for unique book instances
from datetime import date

from django.contrib.auth.models import User  # Required to assign User as a borrower


class BookInstance(models.Model):
    """
    Model representing a specific copy of a book (i.e. that can be borrowed from the library).
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Unique ID for this particular book across whole library")
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    @property
    def is_overdue(self):
        if self.due_back and date.today() > self.due_back:
            return True
        return False

    LOAN_STATUS = (
        #('d', 'Maintenance'),
        #('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='a', help_text='Book availability')

    class Meta:
        ordering = ["due_back"]
        permissions = (("can_mark_returned", "Set book as returned"),)

    def __str__(self):
        """
        String for representing the Model object.
        """
        return "%s " % self.book.title


class Author(models.Model):
    """
    Model representing an author.
    """
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(primary_key='true', blank='false')
    contact_no = models.IntegerField()
    #date_of_birth = models.DateField(null=True, blank=True)
    #date_of_death = models.DateField(null=True, blank=True)

    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s, %s' % ((self.first_name,self.last_name))

class Publisher(models.Model):
    """
    Model representing an author.
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(primary_key='true', blank='false')
    contact_no = models.IntegerField()
    #date_of_birth = models.DateField(null=True, blank=True)
    #date_of_death = models.DateField(null=True, blank=True)

    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('publisher-detail', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s, %s' % (self.first_name,self.last_name)
from django.db import models
class book_issue(models.Model):

    book = models.ForeignKey(Book,on_delete=models.SET_NULL,blank=True,null=True)
    user = models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True)
    book_issued = models.CharField(max_length=2 , null=True , blank=True)
    datetime = models.TimeField(null=True,blank=True)
    @classmethod
    def create(cls):
        book = cls()
        # do something with the book
        return book

    def calculate(self):
         if (self.datetime.minute) + 1 < datetime.now().minute:
             n = datetime.now().minute-self.datetime.minute
             return n
         else:
             return 0

class feedback(models.Model):
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    rating = models.IntegerField(default=5, validators=[MaxValueValidator(5), MinValueValidator(1)])
    text = models.CharField(max_length=500, blank=True, null=True)

class Fine(models.Model):
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    fine = models.IntegerField(null=True,blank=True)

    @classmethod
    def create(cls):
        book = cls()
        # do something with the book
        return book