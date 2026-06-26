from django.shortcuts import render
from books.models import Book, Category
def index(request):
    context = {
        'books': Book.objects.all(),
        'categories': Category.objects.all()
    }
    return render(request, 'core/index.html', context)