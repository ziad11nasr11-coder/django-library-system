from django.shortcuts import render

from books.models import Book, Category

def book_list(request):
    context = {
        'books': Book.objects.all(),
        'categories': Category.objects.all()
    }
    return render(request, 'books/books_list.html', context)

def update_book(request, slug):
    return render(request, 'books/update_book.html', {'slug': slug})

def delete_book(request, slug):
    return render(request, 'books/delete_book.html', {'slug': slug})