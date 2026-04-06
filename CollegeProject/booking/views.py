from django.shortcuts import render,redirect
from login .models import Restaurant

def booking_page(request):
    restaurant_name=request.session.get("restaurant_name")
    if not restaurant_name:
        return redirect('restaurantauth')
    restaurant=Restaurant.objects.get(restaurant_name=restaurant_name)
    context={
        'restaurant':restaurant
    }
    return render(request, "booking/booking_page.html",context)

def restaurant_logout(request):
    request.session.flush()
    return redirect('restaurantauth')

def delete_restaurant(request):
    restaurant_name=request.session.get("restaurant_name")

    if restaurant_name:
        restaurant=Restaurant.objects.get(restaurant_name=restaurant_name)
        restaurant.delete()

    request.session.flush()
    return redirect("restaurantauth")