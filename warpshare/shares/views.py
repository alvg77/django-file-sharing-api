from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Share
from .serializers import ShareSerializer, ShareRequestSerializer
from users.models import User
from django.db.models import Q

# Create your views here.
class CreateShareView(generics.GenericAPIView):
    serializer_class=ShareRequestSerializer
    permission_classes=[IsAuthenticated]
    queryset=Share.objects.all()

    def post(self, request: Request):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
       
        if serializer['reciever'].value==request.user.email:
            return Response(data={'message': 'cannot share to self'}, status=status.HTTP_400_BAD_REQUEST)
        
        share = Share(
            filename=serializer['filename'].value,
            shared_at=serializer['shared_at'].value,
            sender=request.user,
            reciever=User.objects.get(email=serializer['reciever'].value)
        )

        share.save()
        
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
        shares=self.get_queryset().filter(Q(sender=user) | Q(reciever=user)).order_by('shared_at')
        serializer=self.get_serializer(shares, many=True)
        response={
            'message': 'shares fetched',
            'data': serializer.data
        }
        return Response(data=response, status=status.HTTP_200_OK)