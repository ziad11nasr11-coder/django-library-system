from django.shortcuts import render
from books.models import Book, Category
from books.forms import BookForm, CategoryForm
def index(request):
    if request.method == 'POST':
        add_book = BookForm(request.POST, request.FILES)
        if add_book.is_valid():
            add_book.save()
            
    if request.method == 'POST':
        category_form = CategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
    
    context = {
        'books': Book.objects.all(),
        'categories': Category.objects.all(),
        'form': BookForm(),
        'category_form': CategoryForm(),
    }
    return render(request, 'core/index.html', context)