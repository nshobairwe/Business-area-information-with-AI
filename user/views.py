from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from user.forms import CreateUserForm
from django import forms
from django.contrib.auth.models import User
from .forms import CommentForm
from django.core.paginator import Paginator
from .models import Location

# Define your views below

def homepage(request):
    values = [1, 2, 3, 4]
    frontend_list = {'numbers': values}
    return render(request, 'homeU.html', frontend_list)


def registerPage(request):
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('log')
            
        context = {'form':form}
        return render(request, 'reg.html', context)

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Use the 'user' object, not 'User'
            login(request, user)
            return redirect('dash')
        else:
            messages.info(request, 'Username or password is not correct')
    context = {}  # Define the context dictionary with any necessary data
    return render(request, 'login.html', context)


def logoutUser(request):
    # When the user logs out, set a session variable to indicate they have logged out.
    request.session['logout'] = True
    logout(request)  # Log the user out using Django's built-in logout function.
    return redirect('home')  # Redirect the user to the login page after logout.



@login_required  # This decorator ensures that only authenticated users can access the view.
def dashboardU(request):
    if request.session.get('logout', False):
        # If the user has logged out, redirect them to the login page.
        return redirect('login')  # Replace 'login' with your actual login URL.
    if request.user.is_authenticated:
        user_name = request.user.username if request.user.is_authenticated else None


    # Fetch all data from the Location model
    all_locations = Location.objects.all()

    # Paginate the data with 5 items per page
    paginator = Paginator(all_locations, 6)

    # Get the current page number from the request's GET parameters
    page_number = request.GET.get('page')

    # Get the Page object for the current page number
    locations = paginator.get_page(page_number)

    # Pass data to the template context
    context = {
        'user_name': user_name,
        'locations': locations,  # Pass the Page object to the template
    }

    return render(request, 'dashboardU.html', context)


def forgetpass(request):
    values = [1, 2, 3, 4]
    frontend_list = {'numbers': values}
    return render(request, 'forgetpass.html', frontend_list)

def submit_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Maoni yako yamefika. Asante!')
            return redirect('home')  # Redirect to a thank you page or any other desired page
    else:
        form = CommentForm()

    return render(request, 'homeU.html', {'form': form})


