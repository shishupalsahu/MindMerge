from django.urls import path
from main import views

urlpatterns = [
    path('',views.home,name='home'),
    path('search/',views.search,name='search'),
    path('profilepage/',views.profile,name='profile'),
    path('addpost/',views.addpost,name='addpost'),
    path('userprofile/<int:uid>/',views.userprofile,name='userprofile'),
    path('editpost/<int:post_id>/',views.editpost,name='editpost'),
    path('deletepost/<int:post_id>/',views.deletepost,name='deletepost'),
    path('edituser/<int:user_id>/',views.edituser,name='edituser'),
    path('review/<int:post_id>',views.review,name='review'),
    path('deletereview/<int:review_id>',views.deletereview,name='deletereview'),

]