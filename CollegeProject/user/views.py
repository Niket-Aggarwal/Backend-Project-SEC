from django.shortcuts import render,redirect
from login.models import User,Restaurant
from django.db.models import Q
from django.contrib.auth import logout

# Create your views here.
def userpage(request):
    q=request.GET.get('q','')
    restaurants=Restaurant.objects.all()
    if q:
        restaurants=Restaurant.objects.filter(
            Q(restaurant_name__icontains=q)|
            Q(specification__icontains=q)|
            Q(description__icontains=q)|
            Q(address__icontains=q)
        )
    context={'restaurants':restaurants}
    return render(request,'user/user_page.html',context)

def restaurant_detail(request, pk):
    restaurant = Restaurant.objects.get(restaurant_name=pk)

    context = {
        'restaurant': restaurant
    }

    return render(request, 'user/restaurant_detail.html', context)

def logoutPage(request):
    request.session.flush()
    return redirect('selectrole')

def delete_account(request):
    User.objects.filter(username=request.session.get("username")).delete()
    request.session.flush()
    return redirect('selectrole')