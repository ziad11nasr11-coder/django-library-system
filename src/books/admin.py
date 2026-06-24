from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title',  'number_of_pages', 'published_date', 'language',#'author',
                    )
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('language', 'published_date',#'author'
                    )
    search_fields = ('title', 'description', 'language', #'author'
                        )
    #raw_id_fields = ('author',)
    date_hierarchy = 'published_date'
