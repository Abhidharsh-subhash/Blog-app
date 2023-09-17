from . import views
from django.urls import path

urlpatterns = [
    path('homepage/',views.homepage,name='homepage'),
    path('listposts/',views.listposts,name='listposts'),
    path('postdetail/<int:postid>/',views.postdetail,name='postdetail'),
    path('Updatepost/<int:postid>/',views.Updatepost,name='Updatepost'),
    path('Deletepost/<int:postid>/',views.Deletepost,name='Deletepost'),
]