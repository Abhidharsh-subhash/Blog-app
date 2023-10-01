from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status,mixins
from rest_framework.generics import GenericAPIView
from rest_framework.decorators import api_view,APIView,permission_classes
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAuthenticatedOrReadOnly,IsAdminUser
from .models import Post
from .serializer import PostSerializer
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from accounts.serializer import CurrentUserPostsSerializer
from .permissions import ReadOnly,AuthorOrReadOnly


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
@permission_classes([AllowAny])
def homepage(request:Request):

    if request.method == 'POST':
        data=request.data
        response = {'message':'Hello world, POST',"data":data}
        return Response(data=response,status=status.HTTP_201_CREATED)
    
    response = {'message':'Hello world, GET'}
    return Response(data=response,status=status.HTTP_200_OK)

# @api_view(http_method_names=['GET','POST'])
# def listposts(request:Request):
#     posts=Post.objects.all()
#     if request.method == 'POST':
#         data=request.data
#         serializer=PostSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             response={
#                 'message':'Post created successfully',
#                 'data':serializer.data
#             }
#             return Response(data=response,status=status.HTTP_201_CREATED)
#         return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#     serializer=PostSerializer(instance=posts,many=True)
#     response={
#         'message':'All posts',
#         'data':serializer.data
#     }
#     return Response(data=response,status=status.HTTP_200_OK)

# class listcreatepost(APIView):
#      serializer_class=PostSerializer
#      def get(self,request:Request,*args,**kwargs):
#           posts=Post.objects.all()
#           serializer=self.serializer_class(instance=posts,many=True)
#           return Response(data=serializer.data,status=status.HTTP_200_OK)
#      def post(self,request:Request,*args,**kwargs):
#           data=request.data
#           serializer=self.serializer_class(data=data)
#           if serializer.is_valid():
#                serializer.save()
#                response={
#                     'message':'Post created successfully',
#                     'data':serializer.data
#                }
#                return Response(data=response,status=status.HTTP_201_CREATED)
#           return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class listcreatepost(GenericAPIView,
                    mixins.ListModelMixin,
                    mixins.CreateModelMixin):
     serializer_class = PostSerializer
     permission_classes=[ReadOnly]
     # permission_classes=[IsAuthenticatedOrReadOnly]#when we use this we dont need to be authenticated for reading the data's.
     queryset = Post.objects.all()

     #custom mixin hook for create method
     def perform_create(self, serializer):
          serializer.save(author=self.request.user)
          return super().perform_create(serializer)
     
     def get(self,request:Request,*args,**kwargs):
          return self.list(request,*args,**kwargs)
     
     def post(self,request:Request,*args,**kwargs):
          return self.create(request,*args,**kwargs)

# class postviewset(viewsets.ViewSet):

#      def list(self,request:Request):
#           queryset=Post.objects.all()
#           serializer=PostSerializer(instance=queryset,many=True)
#           return Response(data=serializer.data,status=status.HTTP_200_OK)
     
#      def retrieve(self,request:Request,pk=None):
#           queryset=get_object_or_404(Post,pk=pk)
#           serializer=PostSerializer(instance=queryset)
#           return Response(data=serializer.data,status=status.HTTP_200_OK)



# @api_view(http_method_names=['GET'])
# def postdetail(request:Request,postid:int):
#         data=get_object_or_404(Post,id=postid)
#         serialzer=PostSerializer(instance=data)
#         response={
#              'message':'Post detail',
#              'data':serialzer.data
#         }
#         return Response(data=response,status=status.HTTP_200_OK)

# @api_view(http_method_names=['PUT'])
# def Updatepost(reqeust:Request,postid:int):
#      post=get_object_or_404(Post,id=postid)
#      data=reqeust.data
#      serializer=PostSerializer(instance=post,data=data)
#      if serializer.is_valid():
#           serializer.save()
#           response={
#                'message':'Post updated successfully',
#                'data':serializer.data
#           }
#           return Response(data=response,status=status.HTTP_302_FOUND)
#      return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# @api_view(http_method_names=['DELETE'])
# def Deletepost(request:Request,postid:int):
#      post=get_object_or_404(Post,id=postid)
#      post.delete()
#      response={
#           'message':'Post deleted successfully'
#      }
#      return Response(data=response,status=status.HTTP_200_OK)

# class retrievedeleteupdatepost(APIView):
#      serializer_class = PostSerializer
#      def get(self,request:Request,post_id:int):
#           post=get_object_or_404(Post,pk=post_id)
#           serializer=self.serializer_class(instance=post)
#           return Response(data=serializer.data,status=status.HTTP_200_OK)
     
#      def put(self,request:Request,post_id:int):
#           post=get_object_or_404(Post,pk=post_id)
#           data=request.data
#           serializer=self.serializer_class(instance=post,data=data)
#           if serializer.is_valid():
#                serializer.save()
#                data={
#                     'message':'Post updated',
#                     'updated':serializer.data
#                }
#                return Response(data=data,status=status.HTTP_200_OK)
#           return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#      def delete(self,request:Request,post_id:int):
#           post=get_object_or_404(Post,pk=post_id)
#           post.delete()
#           data={
#                'message':'Post deleted'
#           }
#           return Response(data=data,status=status.HTTP_204_NO_CONTENT)

class retrievedeleteupdatepost(GenericAPIView,
                              mixins.UpdateModelMixin,
                              mixins.RetrieveModelMixin,
                              mixins.DestroyModelMixin):
     serializer_class = PostSerializer
     queryset = Post.objects.all()
     permission_classes=[AuthorOrReadOnly]
     def get(self,request:Request,*args,**kwargs):
          return self.retrieve(request,*args,**kwargs)
     
     def put(self,request:Request,*args,**kwargs):
          return self.update(request,*args,**kwargs)
     
     def delete(self,request:Request,*args,**kwargs):
          return self.destroy(request,*args,**kwargs)
# "hooks" in mixins refer to predefined methods or functions within the mixin class,These hooks allow developers 
# to inject custom behavior into the mixin's functionality,

@api_view(http_method_names=['GET'])
@permission_classes([IsAuthenticated])
def get_posts_for_current_user(request:Request):
     user=request.user
     serializer=CurrentUserPostsSerializer(instance=user,context={'request':request})
     return Response(data=serializer.data,status=status.HTTP_200_OK)

class ListPostForAuthor(GenericAPIView,mixins.ListModelMixin):
     serializer_class=PostSerializer
     permission_classes=[IsAuthenticated]
     queryset=Post.objects.all()

     # posts by the particular user in accordance with the jwt token
     # def get_queryset(self):
     #      return Post.objects.filter(author=self.request.user)

     #posts by the username as parameter
     def get_queryset(self):
          # username=self.kwargs.get('username')# if we are passing the username as parameter mentioned in url
          username=self.request.query_params.get('username') or None
          if username is not None:
               return Post.objects.filter(author__username=username)
          else:
               return Post.objects.all()

     def get(self,request,*args,**kwargs):
          return self.list(request,*args,**kwargs)
