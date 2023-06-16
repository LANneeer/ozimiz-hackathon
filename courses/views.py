from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from courses.models import Course
from ozimiz_hackathon.settings import BASE_DIR


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            # Check if the username is available
            if User.objects.filter(username=username).exists():
                error_message = 'Username already exists'
            else:
                # Create a new user
                user = User.objects.create_user(username=username, password=password)
                # Additional logic if needed (e.g., login the user, redirect to a success page, etc.)
                return render(request, BASE_DIR / 'templates/registration_success.html')
        else:
            error_message = 'Passwords do not match'
    else:
        error_message = None

    context = {'error_message': error_message}
    return render(request, BASE_DIR / 'templates/registration.html', context)


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to the courses page after login
    else:
        form = AuthenticationForm()

    return render(request, BASE_DIR / 'templates/login.html', {'form': form})


def courses(request):
    courses = Course.objects.all()
    context = {'courses': courses}
    return render(request, BASE_DIR / 'templates/home.html', context)
