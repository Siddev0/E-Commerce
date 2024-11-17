from django.shortcuts import render

from .forms import BookForm, AuthorForm
from .models import Book, Cart
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    books = Book.objects.all()
    return render(request, 'index.html', {'books': books})

def createBook(request):
    if request.method=='POST':
        form=BookForm(request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form=BookForm()
    return render(request,'index.html', {'form':form})


def createAuthor(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = AuthorForm()
    return render(request, 'author.html', {'form': form})

def registerUser(request):
    if request.method == "POST":
        username=request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')

        if password != cpassword:
            messages.error(request, 'Password mismatch')
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken')
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already taken')
            return redirect('register')

        user=User.objects.create_user(username=username, first_name=fname, last_name=lname, email=email, password=password)
        user.save()
        login(request, user)
        messages.success(request, "Registration Success")
        return redirect('login')

    return render(request, 'register.html')

def loginUser(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login Successful")
            return redirect('/')
        else:
            messages.error(request, "Please Try Again")
            return redirect('login')

    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect('/')

def aboutUser(request):
    return render(request, 'about.html')

def contactUser(request):
    return render(request, 'contact.html')

def cartUser(request):
    cart = Cart.objects.filter(user=request.user).first()
    if cart:
        cart_items = cart.items.all()
    else:
        cart_items = []

    return render(request, 'cart.html', {'cart_items': cart_items})