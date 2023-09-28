from django.shortcuts import render
from .serializer import SignUpSerializer
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.request import Request

# Create your views here.

class SignUpView(GenericAPIView):
    serializer_class=SignUpSerializer
    
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
