from django.contrib import admin
from p_library.models import Book, Author, Publishing

# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(Publishing)
class PublishingAdmin(admin.ModelAdmin):
    pass