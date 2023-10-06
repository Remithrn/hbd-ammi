
from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name='home'),
    path('cake/',views.cake,name='cake'),
    path('wish',views.wish,name='wish')
   
]