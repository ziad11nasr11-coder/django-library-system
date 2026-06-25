from django.shortcuts import render
from books.models import Book
def index(request):
    context = {
        'books': Book.objects.all()
    }
    return render(request, 'core/index.html', context)