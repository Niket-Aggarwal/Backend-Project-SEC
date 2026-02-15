from django.urls import path,include
from login import views

urlpatterns = [
    path('', views.selectrole, name='selectrole'),
    path('customer/', views.customer, name='customerauth'),
    path('restaurant/', views.restaurant, name='restaurantauth'),
]
