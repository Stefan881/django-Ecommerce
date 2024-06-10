from django.shortcuts import render, redirect
from .models import Product, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import SignUpForm


# Create your views here.
def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def about(request):
    return render(request, 'about.html', {})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have been logged in...')
            return redirect('index-url')
        else:
            messages.success(request, 'There was an error logging in please try again...')
            return redirect('login-url')
    else:
        return render(request, 'login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logges out....')
    return redirect('index-url')


def register_user(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # log in user
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'You have successfully register!!Welcome!')
            return redirect('login-url')
        else:
            messages.success(request, 'Whoops!There was an error registering!Please try again!!!')
            return redirect('register-url')
    else:
        return render(request, 'register.html', {'form': form})


def product(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'product.html', {'product': product})


def category(request, foo):
    # Replace hyphens with spaces
    foo = foo.replace('-', ' ')
    # Grab the category from the url
    try:
        # Lookup in the category
        category = Category.objects.get(name=foo)
        products = Product.objects.filter(category=category)
        return render(request, 'category.html', {'products': products, 'category': category})
    except:
        messages.success(request, 'That category does not exixts!!!!')
        return redirect('index-url')
