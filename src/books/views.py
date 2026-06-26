from django.shortcuts import redirect, render, get_object_or_404
from books.forms import BookForm, CategoryForm
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
    book = Book.objects.get(slug=slug)

    if request.method == 'POST':
        book_save = BookForm(request.POST, request.FILES, instance=book)
        if book_save.is_valid():
            book_save.save()
            return redirect('/')
    else:
        book_save = BookForm(instance=book)
    context = {
        'form': book_save,
        'slug': slug
    }
    return render(request, 'books/update_book.html', context)

def delete_book(request, slug):
    book = get_object_or_404(Book, slug=slug)
    if request.method == 'POST':
        book.delete()
        return redirect('/')
    
    return render(request, 'books/delete_book.html', {'slug': slug})