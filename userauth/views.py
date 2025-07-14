from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User

from userauth.forms import CustomUserCreationForm,CustomUserLoginForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def userlogin(request):
    context={
        'title':'loginpage',
    }

    if request.method == "POST":
        user_data = CustomUserLoginForm(data=request.POST)
        if user_data.is_valid():
            user = user_data.get_user()
            login(request, user)
            return redirect('home')

        else:
            messages.error(request, "Error in login. Please try again.")
            context['form'] = user_data

    else:
        context['form'] = CustomUserLoginForm()

    return render(request, 'userlogin.html', context)






def userregister(request):
    context={
        'title':'registerpage',
    }
    if request.method == "POST":
        newuser = CustomUserCreationForm(request.POST)
        if newuser.is_valid():
            user = newuser.save()
            return redirect('userlogin')

        else:
            messages.error(request, "Error in registration. Please try again.")
            messages.error(request, newuser.errors)
            context['form'] = newuser

    else:
        context['form'] = CustomUserCreationForm()

    return render(request,'userregister.html',context)




@login_required
def userlogout(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('home')