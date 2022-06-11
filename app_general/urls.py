from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('food',views.food,name='food'),
    path('foodmenu',views.foodmenu,name='foodmenu'),
    path('login_view',views.login_view,name='login_view'),
    path('register',views.register,name='register'),
    path('add_user',views.add_user,name='add_user'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('orderfood',views.orderfood,name='orderfood'),
    path('buynow',views.buynow,name='buynow'),
    path('services',views.services,name='services'),
    
]

