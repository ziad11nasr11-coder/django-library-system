from django.urls import path
from . import views
urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('update/<slug:slug>/', views.update_book, name='update_book'),
    path('delete/<slug:slug>/', views.delete_book, name='delete_book'),
    
]