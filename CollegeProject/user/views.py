from django.shortcuts import render
from login.models import Restaurant

# Create your views here.
def userpage(request):
    restaurants=Restaurant.objects.all()
    context={'restaurants':restaurants}
    return render(request,'user/user_page.html',context)

def restaurant_detail(request, pk):
    restaurant = Restaurant.objects.get(restaurant_name=pk)

    context = {
        'restaurant': restaurant
    }

    return render(request, 'user/restaurant_detail.html', context)