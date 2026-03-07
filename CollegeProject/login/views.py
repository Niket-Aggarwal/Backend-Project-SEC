from django.shortcuts import render, redirect
from .Customer_form import CustomerSignupForm, CustomerSigninForm
from .models import User


def selectrole(request):
    username = request.session.get("username")
    return render(request, 'login/Roleselect.html', {"username": username})

def customer(request):
    signup_form = CustomerSignupForm()
    signin_form = CustomerSigninForm()
    if request.method == "POST":
        if "signup" in request.POST:
            signup_form = CustomerSignupForm(request.POST)
            if signup_form.is_valid():
                user = signup_form.save()
                request.session["username"] = user.username
                return redirect("/user/")
        if "signin" in request.POST:
            signin_form = CustomerSigninForm(request.POST)
            if signin_form.is_valid():
                username = signin_form.cleaned_data["username"]
                password = signin_form.cleaned_data["password"]
                try:
                    user = User.objects.get(username=username, password=password)
                    request.session["username"] = user.username
                    return redirect("/user/")
                except User.DoesNotExist:
                    signin_form.add_error(None, "Invalid Username or Password")
    context = {
        "signup_form": signup_form,
        "signin_form": signin_form
    }
    return render(request, 'login/Customer.html', context)

def restaurant(request):
    return render(request, 'login/Restrauant.html')