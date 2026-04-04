from django.shortcuts import render,redirect
from login.models import User,Restaurant
from django.db.models import Q
from django.contrib.auth import logout
from .models import Booking
from .booking import BookingForm

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

def booktable(request, restaurantname):
    username = request.session.get("username")
    user = User.objects.get(username=username)
    restaurant = Restaurant.objects.get(restaurant_name=restaurantname)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = user
            booking.restaurant = restaurant
            booking.status = 'pending'
            booking.save()
            return redirect('user_page')
    else:
        form = BookingForm()
    context = {
        'form': form,
        'restaurant': restaurant
    }
    return render(request, 'user/bookingform.html', context)

def mybookings(request):
    username = request.session.get("username")
    user = User.objects.get(username=username)
    bookings = Booking.objects.filter(user=user)
    return render(request, 'user/status.html', {'bookings': bookings})