from django.shortcuts import render, redirect
from login.models import Restaurant
from user.models import Booking


def booking_page(request):
    restaurant_name = request.session.get("restaurant_name")

    if not restaurant_name:
        return redirect('selectrole')

    restaurant = Restaurant.objects.get(restaurant_name=restaurant_name)

    bookings = Booking.objects.filter(restaurant=restaurant)

    return render(request, "booking/booking_page.html", {
        'bookings': bookings,
        'restaurant': restaurant
    })


def restaurant_logout(request):
    request.session.flush()
    return redirect('selectrole')


def delete_restaurant(request):
    restaurant_name = request.session.get("restaurant_name")

    if not restaurant_name:
        return redirect('selectrole')
    
    restaurant=Restaurant.objects.get(restaurant_name=restaurant_name)

    if request.method == "POST":
        restaurant.delete()
        request.session.flush()
        return redirect("restaurantauth")
    
    return render(request,"booking/delete_confirm.html",{'restaurant':restaurant})


def bookingdetail(request, bookingid):
    restaurant_name = request.session.get("restaurant_name")

    if not restaurant_name:
        return redirect('selectrole')

    restaurant = Restaurant.objects.get(restaurant_name=restaurant_name)

    booking = Booking.objects.get(id=bookingid, restaurant=restaurant)

    return render(request, "booking/booking_detail.html", {
        "booking": booking
    })


def updatebooking(request, bookingid):   
    restaurant_name = request.session.get("restaurant_name")

    if not restaurant_name:
        return redirect("selectrole")

    restaurant = Restaurant.objects.get(restaurant_name=restaurant_name)

    booking = Booking.objects.get(id=bookingid, restaurant=restaurant)

    if request.method == "POST":
        booking.status = request.POST.get("status")
        booking.amount = request.POST.get("amount") or None
        booking.save()

    return redirect("booking")

