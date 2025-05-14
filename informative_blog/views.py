from django.shortcuts import render,redirect
from blogs.models import Category,Blogs
from .forms import RegistrationForm
# from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm

def home(request):
    categories = Category.objects.all()
    featured_post = Blogs.objects.filter(is_featured=True,status='published')
    posts = Blogs.objects.filter(is_featured=False,status='published')
    #print(posts)
    #print(featured_post)
    context = {
        'categories':categories,
        'featured_post':featured_post,
        'posts':posts
    }
    return render(request,'home.html', context)
#Registration
def register(request):
    if request.method=="POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register') 
    else:
        form = RegistrationForm()
    context = {
        'form':form
    }
    return render(request, 'register.html',context)    
#login
def login(request):
    if request.method=="POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request,user)
                return redirect('dashboard')

    else:    
        form = AuthenticationForm()
    context = {
        'form':form
    }
    return render(request, 'login.html',context)
    
#logout
def logout(request):
    auth.logout(request)
    return redirect('home')