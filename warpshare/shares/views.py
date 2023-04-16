from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Share
from .serializers import ShareSerializer
from users.models import User

# Create your views here.
class CreateShareView(generics.GenericAPIView):
    serializer_class=ShareSerializer
    permission_classes=[IsAuthenticated]
    queryset=Share.objects.all()

    def post(self, request: Request):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
       
        if serializer.validated_data['reciever']==request.user:
            return Response(data={'message': 'cannot share to self'}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer.validated_data['sender']=request.user
        serializer.save(sender=request.user)
        response={
            'message': 'share created',
            'data': serializer.data
        }
        return Response(data=response, status=status.HTTP_201_CREATED)
    
class ListSharesView(generics.GenericAPIView):
    serializer_class=ShareSerializer
    permission_classes=[IsAuthenticated]
    queryset=Share.objects.all()

    def get(self, request: Request):
        user = request.user
        shares=self.get_queryset().filter(reciever=user)
        serializer=self.get_serializer(shares, many=True)
        response={
            'message': 'shares fetched',
            'data': serializer.data
        }
        return Response(data=response, status=status.HTTP_200_OK)


class ListSharesHistoryView(generics.GenericAPIView):
    serializer_class=ShareSerializer
    permission_classes=[IsAuthenticated]
    queryset=Share.objects.all()

    def get(self, request: Request):
        user = request.user
        shares=self.get_queryset().filter(sender=user, reciever=user).order_by('shared_at')
        serializer=self.get_serializer(shares, many=True)
        response={
            'message': 'shares fetched',
            'data': serializer.data
        }
        return Response(data=response, status=status.HTTP_200_OK)