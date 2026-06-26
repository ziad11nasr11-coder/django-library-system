from django.shortcuts import render
from books.forms import CategoryForm
from books.models import Book, Category

def book_list(request):
    if request.method == 'POST':
        category_form = CategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
    context = {
        'books': Book.objects.all(),
        'categories': Category.objects.all(),
        'category_form': CategoryForm()
    }
    return render(request, 'books/books_list.html', context)

def update_book(request, slug):
    return render(request, 'books/update_book.html', {'slug': slug})

def delete_book(request, slug):
    return render(request, 'books/delete_book.html', {'slug': slug})