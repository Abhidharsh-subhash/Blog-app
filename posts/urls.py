from . import views
from django.urls import path

urlpatterns = [
    path('homepage/',views.homepage,name='homepage'),
    path('listposts/',views.listposts,name='listposts'),
    path('postdetail/<int:postindex>/',views.postdetail,name='postdetail'),
]