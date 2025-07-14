from django.urls import path
from userauth import views

urlpatterns = [
    path('userlogin/',views.userlogin,name='userlogin'),
    path('userregister/',views.userregister,name='userregister'),
    path('userlogout/',views.userlogout,name='userlogout'),
]