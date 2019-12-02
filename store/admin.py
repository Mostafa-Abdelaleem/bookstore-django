from django.contrib import admin
from .models import Book
# Register your models here.


class Book_Admin(admin.ModelAdmin):
    list_display = ( 'title' , 'author' )

admin.site.register(Book, Book_Admin)