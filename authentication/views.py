from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login

def authentication(request):
    return render(request, "authentication/authentication.html")

def signup(request):

    if request.method == "POST":
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()

        messages.success(request, "Your account has been successfully created!")

        return redirect('signin')

    return render(request, "authentication/signup.html")

def signin(request):

    if request.method == "POST":
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')

        user = authenticate(username=username, password=pass1)  # returns none response or not none response

        if user is not None:
            login(request, user)
            fname = user.first_name
            return redirect('authentication', {'fname': fname})
        else:
            messages.error(request, "Incorrect Credentials")
            return redirect('authentication')


    return render(request, "authentication/signin.html")

def signout(request):
    pass