from django.shortcuts import render
from books.models import Book, Category
from books.forms import BookForm
def index(request):
    if request.method == 'POST':
        add_book = BookForm(request.POST, request.FILES)
        if add_book.is_valid():
            add_book.save()
            
    context = {
        'books': Book.objects.all(),
        'categories': Category.objects.all(),
        'form': BookForm(),
    }
    return render(request, 'core/index.html', context)