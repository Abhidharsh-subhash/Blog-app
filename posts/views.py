from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


# def homepage(request:HttpRequest):
#     response = {'message':'Hello world'}
#     return JsonResponse(data=response)

posts=[
    {
        "id":1,
        'title':'is programming difficult ?',
        'description':'Programming is simple because it needs only logic to build something.'
    },
    {
        'id':2,
        'title':'Learn Python',
        'description':'Python is a high level programming language.'
    }
]

@api_view(http_method_names=['GET','POST'])
def homepage(request:Request):

    if request.method == 'POST':
        data=request.data
        response = {'message':'Hello world, POST',"data":data}
        return Response(data=response,status=status.HTTP_201_CREATED)
    
    response = {'message':'Hello world, GET'}
    return Response(data=response,status=status.HTTP_200_OK)

@api_view(http_method_names=['GET'])
def listposts(request:Request):
    return Response(data=posts,status=status.HTTP_200_OK)

@api_view(http_method_names=['GET'])
def postdetail(request:Request,postindex:int):
    try:
        data=posts[postindex-1]
        return Response(data=data,status=status.HTTP_200_OK)
    except:
        return Response(data={'error':'No data found'},status=status.HTTP_404_NOT_FOUND)