from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Book, Feedback
from .forms import UserFeedbackForm, BookCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    books = Book.objects.all()  #This will return all Books in the DB

    context = {
        'books': books,
    }
    return render(request, 'main/index.html', context)

@login_required
def add_book(request):
    if request.method == 'POST':
        form = BookCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book Added Successfully')
            return redirect('index')
        else:
            # If form is not valid, return the form with errors
            # messages.error(request, 'Please correct the errors below.')
            return render(request, 'main/create_book.html', {'form': form})
    form = BookCreationForm()
    return render(request, 'main/create_book.html', {'form': form})


@login_required
def book_details(request, id):
    book = Book.objects.get(id=id)

    context = {
        'book':book,
    }
    return render(request, 'main/book_details.html', context)


@login_required
def user_feedback(request):
    if request.method == 'POST':
        form = UserFeedbackForm(request.POST)
        if form.is_valid():
            feedback = Feedback(
                name = form.cleaned_data['name'],
                email = form.cleaned_data['email'],
                age = form.cleaned_data['age'],
                message = form.cleaned_data['message']
            )
            feedback.save()
            messages.success(request, 'Thank You for your feedback')
            return redirect('index')
        else:
            messages.error(request, 'Please correct the errors!')
    else:
        form = UserFeedbackForm()
    context = {
        'form':form
    }
    return render(request, 'main/feedback_form.html', context)