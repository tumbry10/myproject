from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, UserUpdateForm, UserProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def user_registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_login')
        else:
            # If form is not valid, return the form with errors
            return render(request, 'user_auths/registration_page.html', {'form': form})
    form = UserRegistrationForm()
    return render(request, 'user_auths/registration_page.html', {'form' : form})

@login_required
def user_profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance = request.user)
        profile_form = UserProfileUpdateForm(request.POST, request.FILES, instance = request.user.user_profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your Profile has been Updated Successfully!')
            return redirect('user_profile')
        else:
            # If form is not valid, return the form with errors
            context = {
            'user_form': user_form,
            'profile_form': profile_form
        }
        return render(request, 'user_auths/user_profile.html', context)
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = UserProfileUpdateForm(instance=request.user.user_profile)

        context = {
            'user_form': user_form,
            'profile_form': profile_form
        }
        return render(request, 'user_auths/user_profile.html', context)