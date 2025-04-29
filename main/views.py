from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Book, Feedback
from .forms import UserFeedbackForm

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