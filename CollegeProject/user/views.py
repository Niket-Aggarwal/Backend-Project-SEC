from django.shortcuts import render,redirect
from login.models import User,Restaurant
from django.db.models import Q
from .models import Booking
from .booking import BookingForm
from datetime import datetime

# Create your views here.
def userpage(request):
    if request.session.get('username'):
        q=request.GET.get('q','')
        restaurants=Restaurant.objects.all()
        if q:
            restaurants=Restaurant.objects.filter(
                Q(restaurant_name__icontains=q)|
                Q(specification__icontains=q)|
                Q(description__icontains=q)|
                Q(address__icontains=q)
                )
        restaurant_count=restaurants.count()
        context={'restaurants':restaurants,'restaurant_count':restaurant_count}
        return render(request,'user/user_page.html',context)
    else:
        return redirect('/')

def restaurant_detail(request, pk):
    if request.session.get('username'):
        restaurant = Restaurant.objects.get(restaurant_name=pk)
        context = {'restaurant': restaurant}
        return render(request, 'user/restaurant_detail.html', context)
    else:
        return redirect('/')

def logoutPage(request):
    request.session.flush()
    return redirect('selectrole')

def delete_user(request):
    username = request.session.get("username")

    if not username:
        return redirect('selectrole')
    
    user=User.objects.get(username=username)

    if request.method == "POST":
        user.delete()
        request.session.flush()
        return redirect("selectrole")
    
    return render(request,"user/delete_confirm.html",{'user':user})


def booktable(request, restaurantname):
    if request.session.get('username'):
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
            context={'form': form,'restaurant': restaurant}
            return render(request, 'user/bookingform.html', context)
    else:
        return redirect("/")
    
def mybookings(request):
    if request.session.get("username"):
        username = request.session.get("username")
        user = User.objects.get(username=username)
        bookings = Booking.objects.filter(user=user)
        for b in bookings:
            booking_end = datetime.combine(b.date, b.endtime)
            if datetime.now() > booking_end:
                b.delete()
        bookings = Booking.objects.filter(user=user)
        return render(request, 'user/status.html', {'bookings': bookings})
    else:
        return redirect("/")

def update_booking(request,booking_id):
    username = request.session.get("username")
    if not username:
        return redirect("/")
    booking = Booking.objects.filter(id=booking_id,user__username=username).first()
    restaurant= booking.restaurant
    if booking.status != 'pending':
        return redirect('mybookings')
    if request.method == "POST":
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('mybookings')
    else:
        form = BookingForm(instance=booking)
    return render(request, 'user/bookingform.html', {'form': form, 'restaurant': restaurant})

def delete_booking(request, booking_id):
    username = request.session.get("username")
    if not username:
        return redirect("/")
    booking = Booking.objects.filter(id=booking_id, user__username=username).first()
    if booking:
        booking.delete()
    return redirect('mybookings')