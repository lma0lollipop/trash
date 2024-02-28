from django.shortcuts import redirect
from django.shortcuts import render
from .forms import UserCreateForm
from django.http import HttpResponse
from .models import UserProfile
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
# Create your views here.
def home(request):
    context = {}
    return render(request, "base/home.html", context)

def signup(request):
    form = UserCreateForm(request.POST or None)
    print(request.POST)
    if request.method == "POST" and request.POST["password"] == request.POST["confirm_password"]:
        fname= request.POST["firstname"]
        lname= request.POST["lastname"]
        username=request.POST["username"]
        email= request.POST["email"]
        password=request.POST["password"]
        if request.POST["private"] == "no":
            privacy=False
        else:
            privacy=True
        user = User.objects.create(username=username, email=email, password=password, first_name=fname, last_name=lname)
        
        return redirect('base:home')
    context = {'form':form, 'errors':form.errors.as_ul}
    return render(request, "base/signup.html", context)


def login(request):
    page= 'base:login'
    if request.method == "POST":
        username = request.POST.get('username').lower()
        password = request.POST.get('password');print(password)

        try:
            user = User.objects.get(username=username)
        except:
            return HttpResponse('No User with such username found!')
        user = authenticate(username=username, password=password)
        print("2",user)
        if user is not None:
            login(request, user)
            return redirect('base:home')
        # else:
        #     return HttpResponse('Username or Password is invalid!')

    context = {'page':page}
    return render(request, "base/login.html", context)
    


def logoutUser(request):
    logout(request)
    return redirect('home')

