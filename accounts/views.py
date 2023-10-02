from django.shortcuts import render
from .serializer import SignUpSerializer
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from .tokens import create_jwt_pair_for_user
from drf_yasg.utils import swagger_auto_schema

# Create your views here.

class SignUpView(GenericAPIView):
    permission_classes=(AllowAny,)
    serializer_class=SignUpSerializer
    
    @swagger_auto_schema(operation_summary='New user signup')
    def post(self,request:Request):
        data=request.data
        serializer=self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            response={
                'message':'User Created successfully',
                'data':serializer.data
            }
            return Response(data=response,status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class LoginView(APIView):
    permission_classes=(AllowAny,)
    @swagger_auto_schema(operation_summary='User login')
    def post(self,request:Request):
        email=request.data.get('email')
        password=request.data.get('password')
        user=authenticate(email=email,password=password)
        if user is not None:
            tokens=create_jwt_pair_for_user(user)
            response={
                'message':'Login Successfull',
                'token':tokens
            }
            return Response(data=response,status=status.HTTP_200_OK)
        else:
            return Response(data={'Invalid Username or Password'},status=status.HTTP_400_BAD_REQUEST)

    def get(self,request:Request):
        content={
            'user':str(request.user),
            'token':str(request.auth)    
        }
        return Response(data=content,status=status.HTTP_200_OK)
