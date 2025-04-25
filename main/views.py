from django.shortcuts import render
from .models import Book

# Create your views here.
def index(request):
    books = Book.objects.all()  #This will return all Books in the DB

    context = {
        'books': books,
    }
    return render(request, 'main/index.html', context)

def book_details(request, id):
    book = Book.objects.get(id=id)

    context = {
        'book':book,
    }
    return render(request, 'main/book_details.html', context)