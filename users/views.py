from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import AppUser
from .serializers import UserSerializer, UserRegisterSerializer


@api_view(['GET'])
def user_list(request):
    if request.method == 'GET':
        users = AppUser.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    

@api_view(['GET'])
def user_details(request, id):
    if request.method == 'GET':
        user = AppUser.objects.filter(pk=id).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)


@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(request.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
