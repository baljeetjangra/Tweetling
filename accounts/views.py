from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth import get_user_model


def signup_view(request):
    User = get_user_model()
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email'].lower()
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if User.objects.filter(email=email):
            messages.warning(request, "Email already exists", extra_tags="exist")
            return redirect('accounts:signup')

        if password1 != password2:
            messages.warning(request, "Password mismatch",extra_tags='mismatch')
            return redirect('accounts:signup')
        
        user = User(first_name=first_name,last_name=last_name, email=email)
        # user.save(commit=false)
        user.set_password(password1)
        user.save()
        return redirect('accounts:login')
        

            

    return render(request, 'accounts/signup.html')

def login_view(request):
    if request.method == "POST":
        email = request.POST['email'].lower()
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.warning(request, "Please enter correct email and password !")
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('accounts:login')