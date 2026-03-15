from django.shortcuts import render, redirect
from .Customer_form import CustomerSignupForm, CustomerSigninForm
from .Restaruant_form import RestaurantSignupStep1Form, RestaurantSignupStep2Form, RestrauntSigninForm
from .models import User, Restaurant


def selectrole(request):
    return render(request, 'login/Roleselect.html')

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
    signup_form = RestaurantSignupStep1Form()
    signin_form = RestrauntSigninForm()
    if request.method == "POST":
        if "signup" in request.POST:
            signup_form = RestaurantSignupStep1Form(request.POST)
            if signup_form.is_valid():
                request.session["restaurant_data"] = signup_form.cleaned_data
                return redirect("/restaurantstep2/")
        if "signin" in request.POST:
            signin_form = RestrauntSigninForm(request.POST)
            if signin_form.is_valid():
                username = signin_form.cleaned_data["restaurant_name"]
                password = signin_form.cleaned_data["password"]
                try:
                    user = Restaurant.objects.get(
                        restaurant_name=username,
                        password=password
                    )
                    request.session["username"] = user.restaurant_name
                    return redirect("/booking/")
                except Restaurant.DoesNotExist:
                    signin_form.add_error(None, "Invalid Username or Password")
    context = {
        "signup_form": signup_form,
        "signin_form": signin_form
    }
    return render(request, 'login/Restrauant.html', context)

def restaurant_step2(request):
    step1_data = request.session.get("restaurant_data")
    if not step1_data:
        return redirect("/restaurant/")
    form = RestaurantSignupStep2Form()
    if request.method == "POST":
        form = RestaurantSignupStep2Form(request.POST, request.FILES)
        if form.is_valid():
            restaurant = form.save(commit=False)
            restaurant.restaurant_name = step1_data["restaurant_name"]
            restaurant.password = step1_data["password"]
            restaurant.phone_number = step1_data["phone_number"]
            restaurant.address = step1_data["address"]
            restaurant.save()
            del request.session["restaurant_data"]
            request.session["username"] = restaurant.restaurant_name
            return redirect("/booking/")
    context = {"form": form}
    return render(request, "login/RestaurantStep2.html", context)