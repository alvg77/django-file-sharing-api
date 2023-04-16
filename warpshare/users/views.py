from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status, generics, mixins
from rest_framework.decorators import APIView, api_view
from .models import User
from .serializers import UserSerializer
from django.contrib.auth import authenticate
from .tokens import create_jwt_pair_for_user
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly

class SignUpView(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes=[AllowAny]

    def post(self, request: Request):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():            
            serializer.save()
            tokens=create_jwt_pair_for_user(serializer.instance)
            response = {
                'message': 'user created',
                'data': serializer.data,
                'tokens': tokens
            }

            return Response(data=response, status=status.HTTP_201_CREATED)
        
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes=[AllowAny]

    def post(self, request: Request):
        email=request.data.get('email')
        password=request.data.get('password')

        user=authenticate(email=email, password=password)
        
        if user is not None:
            tokens=create_jwt_pair_for_user(user)
            response = {
                'message': 'user logged in',
                'tokens': tokens
            }

            return Response(data=response, status=status.HTTP_200_OK)
        
        return Response(data={'message': 'invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getUser(self, request: Request, id: int):
        user = User.objects.get(id=id)
        serializer = UserSerializer(user)
        response = {
            'message': 'user fetched',
            'data': serializer.data
        }
        return Response(data=response, status=status.HTTP_200_OK)

class UpdateDeleteUserView(APIView):
    permission_classes=[IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def put(self, request: Request):
        user = request.user
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            response = {
                'message': 'user updated',
                'data': serializer.data
            }

            return Response(data=response, status=status.HTTP_200_OK)
        
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request: Request):
        user = request.user
        user.delete()
        response = {
            'message': 'user deleted',
        }

        return Response(status=status.HTTP_204_NO_CONTENT)
    
