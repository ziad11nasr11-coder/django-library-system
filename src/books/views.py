from django.shortcuts import render

def book_list(request):
    return render(request, 'books/books_list.html')

def update_book(request, slug):
    return render(request, 'books/update_book.html', {'slug': slug})

def delete_book(request, slug):
    return render(request, 'books/delete_book.html', {'slug': slug})