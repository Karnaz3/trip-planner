# user/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm  # For creating Django's built-in User
from .models import User, Profile
from .form import UserProfileForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)  # Django's User form
        profile_form = UserProfileForm(request.POST, request.FILES)  # Your Profile form

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()  # Save the User
            profile = profile_form.save(commit=False)
            profile.user = user  # Link the Profile to the User
            profile.save() # Save the Profile

            return redirect('login')  # Redirect to login page
    else:
        user_form = UserCreationForm()
        profile_form = UserProfileForm()
    return render(request, 'user/register.html', {'user_form': user_form, 'profile_form': profile_form})


@login_required # Protect this view
def profile(request):
    try:
        profile = request.user.profile  # Get the user's profile
    except Profile.DoesNotExist:  # create profile if doesn't exist
        profile = Profile(user=request.user)
        profile.save()


    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('profile')  # Redirect to profile page
    else:
        profile_form = UserProfileForm(instance=profile)

    return render(request, 'user/profile.html', {'profile_form': profile_form})

