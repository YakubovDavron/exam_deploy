from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


# Create your models here.
class About(models.Model):
    title = models.CharField(max_length=212)
    description = models.TextField()
    image = models.ImageField(upload_to='about')
    video = models.FileField(upload_to='about_video')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=+True)

    def __str__(self):
        return self.title


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        # You can add more fields here as needed

        user = User.objects.create_user(username, email, password)
        # You can customize this further if you have additional fields

        # Automatically log in the user after registration
        login(request, user)

        return redirect('home')  # Redirect to the homepage after successful registration
    else:
        return render(request, 'registration/register.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to the homepage after successful login
        else:
            # Handle invalid login
            return render(request, 'registration/login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'registration/login.html')