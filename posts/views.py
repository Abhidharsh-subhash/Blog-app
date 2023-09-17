from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Post
from .serializer import PostSerializer
from django.shortcuts import get_object_or_404


# def homepage(request:HttpRequest):
#     response = {'message':'Hello world'}
#     return JsonResponse(data=response)

# posts=[
#     {
#         "id":1,
#         'title':'is programming difficult ?',
#         'description':'Programming is simple because it needs only logic to build something.'
#     },
#     {
#         'id':2,
#         'title':'Learn Python',
#         'description':'Python is a high level programming language.'
#     }
# ]

@api_view(http_method_names=['GET','POST'])
def homepage(request:Request):

    if request.method == 'POST':
        data=request.data
        response = {'message':'Hello world, POST',"data":data}
        return Response(data=response,status=status.HTTP_201_CREATED)
    
    response = {'message':'Hello world, GET'}
    return Response(data=response,status=status.HTTP_200_OK)

@api_view(http_method_names=['GET','POST'])
def listposts(request:Request):
    posts=Post.objects.all()
    if request.method == 'POST':
        data=request.data
        serializer=PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            response={
                'message':'Post created successfully',
                'data':serializer.data
            }
            return Response(data=response,status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    serializer=PostSerializer(instance=posts,many=True)
    response={
        'message':'All posts',
        'data':serializer.data
    }
    return Response(data=response,status=status.HTTP_200_OK)

@api_view(http_method_names=['GET'])
def postdetail(request:Request,postid:int):
        data=get_object_or_404(Post,id=postid)
        serialzer=PostSerializer(instance=data)
        response={
             'message':'Post detail',
             'data':serialzer.data
        }
        return Response(data=response,status=status.HTTP_200_OK)

@api_view(http_method_names=['PUT'])
def Updatepost(reqeust:Request,postid:int):
     post=get_object_or_404(Post,id=postid)
     data=reqeust.data
     serializer=PostSerializer(instance=post,data=data)
     if serializer.is_valid():
          serializer.save()
          response={
               'message':'Post updated successfully',
               'data':serializer.data
          }
          return Response(data=response,status=status.HTTP_302_FOUND)
     return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(http_method_names=['DELETE'])
def Deletepost(request:Request,postid:int):
     post=get_object_or_404(Post,id=postid)
     post.delete()
     response={
          'message':'Post deleted successfully'
     }
     return Response(data=response,status=status.HTTP_200_OK)