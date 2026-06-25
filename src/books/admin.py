from django.contrib import admin
from .models import Book, Author, Category

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title',  'number_of_pages', 'published_date', 'language','author','category')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('language', 'published_date','author', 'category')
    search_fields = ('title', 'description', 'language', 'author__name', 'category__name')
    raw_id_fields = ('author',)
    date_hierarchy = 'published_date'
    list_select_related = ('author', 'category')

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
