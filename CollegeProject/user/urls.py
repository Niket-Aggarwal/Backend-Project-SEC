from django.urls import path,include
from user import views

urlpatterns = [
    path("",views.userpage,name="user_page"),
    path('restaurant/<str:pk>/', views.restaurant_detail, name="restaurant_detail"),
    path('logout/',views.logoutPage,name='logout'),
    path('delete/',views.delete_account,name='delete'),
    path('book/<str:restaurantname>/', views.booktable, name='booktable'),
    path('mybookings/', views.mybookings, name='mybookings'),
]

