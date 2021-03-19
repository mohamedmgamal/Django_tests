from .serializers import MovieSerializer,UserSerializer
from Netflix.models import Movies,ApiTest
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated



@api_view(["GET"])
@permission_classes([IsAuthenticated])
def index(request):
    movies = ApiTest.objects.all()
    response = MovieSerializer(instance=movies, many=True)
    return Response(data=response.data, status=status.HTTP_200_OK)
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create(request):
    serializer = MovieSerializer(data=request.data)
    print(serializer)
    if serializer.is_valid():
        serializer.save()
        return Response(data={
            "success": True,
            "message": "New movie added successfully "
        }, status=status.HTTP_201_CREATED)
    return Response(data={
        "success": False,
        "errors": serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)
@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def Update(request,id):
    serializer=MovieSerializer(ApiTest.objects.get(pk=id),data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data={
            "Success":True
            ,"Massage":"Movie updated"
        },status=status.HTTP_200_OK)
    return Response(data={
        "Success": False
        , "Error": serializer.errors
    })
@api_view(["POST"])
def signUp(request):
    serializer = UserSerializer(data=request.data)
    print(serializer)
    if serializer.is_valid():
        serializer.save()
        return Response(data={
            "success": True,
            "message": "New user added successfully "
        }, status=status.HTTP_201_CREATED)
    return Response(data={
        "success": False,
        "errors": serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)