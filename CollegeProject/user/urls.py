from django.urls import path,include
from user import views

urlpatterns = [
    path("",views.userpage,name="user_page"),
    path('restaurant/<str:pk>/', views.restaurant_detail, name="restaurant_detail"),
]

