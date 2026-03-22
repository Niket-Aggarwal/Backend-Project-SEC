from django.shortcuts import render
from login.models import Restaurant
from django.db.models import Q

# Create your views here.
def userpage(request):
    q=request.GET.get('q','')
    restaurants=Restaurant.objects.all()
    if q:
        restaurants=Restaurant.objects.filter(
            Q(restaurant_name__icontains=q)|
            Q(specification__icontains=q)|
            Q(description__icontains=q)
        )
    context={'restaurants':restaurants}
    return render(request,'user/user_page.html',context)

def restaurant_detail(request, pk):
    restaurant = Restaurant.objects.get(restaurant_name=pk)

    context = {
        'restaurant': restaurant
    }

    return render(request, 'user/restaurant_detail.html', context)