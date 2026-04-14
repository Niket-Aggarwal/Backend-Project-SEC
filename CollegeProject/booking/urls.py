from django.urls import path
from . import views

urlpatterns = [
    path('', views.booking_page, name='booking'),
    path('logout/',views.restaurant_logout,name="restaurant_logout"),
    path('delete/',views.delete_restaurant,name="delete_restaurant"),
    path('detail/<int:bookingid>/',views.bookingdetail,name="bookingdetail"),
    path('update/<int:bookingid>/',views.updatebooking,name="updatebooking"),
]