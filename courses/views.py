from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect

from ozimiz_hackathon.settings import BASE_DIR
from .forms import CourseForm
from .models import Course
from .models import CourseCompletion


def index(request):
    return render(request, BASE_DIR / 'templates/index.html')


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
                return redirect('courses')  # Redirect to the courses page after login
    else:
        form = AuthenticationForm()

    return render(request, BASE_DIR / 'templates/login.html', {'form': form})


def courses(request):
    courses = Course.objects.filter(students=request.user)
    context = {'courses': courses}
    return render(request, BASE_DIR / 'templates/courses.html', context)


@login_required
def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    is_completed = CourseCompletion.objects.filter(user=request.user, course=course).exists()

    if request.method == 'POST' and not is_completed:
        completion = CourseCompletion(user=request.user, course=course)
        completion.save()
        return redirect('course_detail', pk=pk)

    return render(request, BASE_DIR / 'templates/course_detail.html', {'course': course, 'is_completed': is_completed})


@user_passes_test(lambda u: u.is_superuser)
def course_edit(request, pk):
    course = get_object_or_404(Course, pk=pk)

    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course_detail', pk=pk)
    else:
        form = CourseForm(instance=course)

    return render(request, BASE_DIR / 'templates/course_edit.html', {'form': form, 'course': course})


@login_required
def course_complete(request, pk):
    course = get_object_or_404(Course, pk=pk)
    is_completed = CourseCompletion.objects.filter(user=request.user, course=course).exists()

    if request.method == 'POST' and not is_completed:
        completion = CourseCompletion(user=request.user, course=course)
        completion.save()

    return redirect('course_detail', pk=pk)
