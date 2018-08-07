from django.contrib import admin

# Register your models here.
from Library.models import *

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(BookInstance)
admin.site.register(Publisher)
admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Users)
admin.site.register(book_issue)
admin.site.register(feedback)
admin.site.site_header="Library Admin"