from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status, generics, mixins
from rest_framework.decorators import APIView
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

class PostRetrieveUpdateUserView(
    generics.GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
):
    serializer_class=UserSerializer
    queryset=User.objects.all()
    lookup_field='id'
    permission_classes=[IsAuthenticated]

    def get(self, request: Request):
        user_id = request.user.id
        return self.retrieve(request, user_id)
    
    def put(self, request: Request):
        user_id = request.user.id
        return self.update(request, user_id)
    
    def delete(self, request: Request):
        user_id = request.user.id
        return self.destroy(request, user_id)
    
