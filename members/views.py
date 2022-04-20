from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth


def register_user(request):
    if(request.method == "POST"):
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if(password == confirm_password):
            if(User.objects.filter(email=email).exists()):
                messages.info(request, "Email already used!!!")
                return redirect('register')
            elif(User.objects.filter(username=username).exists()):
                messages.info(request, "Username already used!!!")
                return redirect('register')
            else:
                user = User.objects.create_user(
                    username=username, email=email, password=password)
                user.save()
                messages.success(request, "User registered ruccessfully...")
                return redirect('login')
        else:
            messages.info(request, "Passwords does not match!!!")
            return redirect('register')
    else:
        return render(request, 'authenticate/register.html')


def login_user(request):
    if(request.method == "POST"):
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, "User logged in successfully...")
            return redirect('home')
        else:
            messages.error(request, "Inavlid login! Try again...")
            return render(request, 'authenticate/login.html')
    else:
        return render(request, 'authenticate/login.html')


def logout_user(request):
    auth.logout(request)
    messages.success(request, "User logged out successfully...")
    return redirect('/')
