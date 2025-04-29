from django.shortcuts import render, redirect
from .forms import UserRegistrationForm

# Create your views here.
def user_registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_login')
    form = UserRegistrationForm()
    return render(request, 'user_auths/registration_page.html', {'form' : form})
    