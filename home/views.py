from django.contrib import messages
from django.shortcuts import redirect, render, HttpResponse
from .models import Blog
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db.utils import IntegrityError

# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, "about.html")

def blogHome(request):
    blogs = Blog.objects.all()
    params = {'blogs': blogs}
    return render(request, "blogHome.html", params)

def blogPost(request, slug):
    if request.user.is_authenticated:
        blog = Blog.objects.filter(slug=slug).first()
        params = {'blog': blog}
        return render(request, "blogPost.html", params)
    else:
        messages.warning(request, "Please Log in to see blogs!")
        return redirect("/login")

def login_(request):
    if request.user.is_authenticated:
        messages.warning(request, "You are already logged in!")
        return redirect("/")
    else:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You have been succesfully logged in!")
                return redirect("/")
            else:
                messages.warning(request, "Invalid Credentials!")
                return redirect("/login")
        return render(request, 'login.html')

def register(request):
    if request.user.is_authenticated:
        messages.warning(request, "You are already logged in!")
        return redirect("/")
    else:
        if request.method == "POST":
            try:
                email = request.POST['email']
                password = request.POST['password']
                username = request.POST['username']
                fname = request.POST['fname']
                lname = request.POST['lname']

                # Validations
                if len(str(username)) > 15:
                    messages.warning(request, "Username must contain under 15 chars")
                    return redirect("/register")
                
                # Creating the user
                myuser = User.objects.create_user(email=email, password=password, username=username)
                myuser.first_name = fname
                myuser.last_name = lname
                myuser.save()
            except IntegrityError:
                messages.error(request, "This username is already taken!")
                return redirect('/register')
            messages.success(request, "Your DebCoder Account has been succesfully created!  Now you can login!")
            return redirect("/login")
        return render(request, "register.html")

def logout_(request):
    logout(request)
    messages.success(request, "Succesfully Logged Out!")
    return redirect("/")

def search(request):
    query = request.GET['search']
    if len(query) > 78:
        blogs = Blog.objects.none()
    else:
        blogsTitle = Blog.objects.filter(title__icontains=query)
        blogsDesc = Blog.objects.filter(desc__icontains=query)
        blogsCategory = Blog.objects.filter(category__icontains=query)
        blogs = blogsTitle.union(blogsDesc, blogsCategory)
    params = {'query': query, 'blogs': blogs}
    return render(request, "search.html", params)