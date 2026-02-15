from django.shortcuts import render

def selectrole(request):
    return render(request, 'login/Roleselect.html')

def customer(request):
    return render(request, 'login/Customer.html')

def restaurant(request):
    return render(request, 'login/Restrauant.html')
