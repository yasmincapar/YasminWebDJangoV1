from django.urls import path
from . import views#h

urlpatterns=[
    path('',views.playerlist,name='playerlist'),#this is the path
#name of the link is playerlist python 
    path('<int:pk>/',views.playerdetail,name='playerdetail'),#this is the path 
]
#in django we are trying to get a hold on the player and in player
#MVT view model template

