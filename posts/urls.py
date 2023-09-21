from . import views
from django.urls import path

urlpatterns = [
    path('homepage/',views.homepage,name='homepage'),
    path('listcreatepost/',views.listcreatepost.as_view(),name='listcreatepost'),
    path('retrievedeleteupdatepost/<int:pk>/',views.retrievedeleteupdatepost.as_view(),name='retrievedeleteupdatepost'),
    # path('retrievedeleteupdatepost/<int:post_id>/',views.retrievedeleteupdatepost.as_view(),name='retrievedeleteupdatepost'),
    # path('Updatepost/<int:postid>/',views.Updatepost,name='Updatepost'),
    # path('Deletepost/<int:postid>/',views.Deletepost,name='Deletepost'),
]