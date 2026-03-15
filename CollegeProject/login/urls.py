from django.urls import path,include
from login import views

urlpatterns = [
    path('', views.selectrole, name='selectrole'),
    path('customer/', views.customer, name='customerauth'),
    path('restaurant/', views.restaurant, name='restaurantauth'),
    path('restaurantstep2/', views.restaurant_step2, name='restaurantauth2'),
    path("user/",include("user.urls")),
    path("booking/",include("booking.urls")),
]
