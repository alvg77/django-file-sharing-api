from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import FileUploadParser
from .models import Share
from .serializers import ShareSerializer, ShareRequestSerializer
from users.models import User
from django.db.models import Q
import uuid
import boto3
import os
import datetime

class FileShareView(APIView):
    parser_classes = (FileUploadParser,)
    serializer_class=ShareRequestSerializer
    permission_classes=[IsAuthenticated]
    queryset=Share.objects.all()

    def put(self, request, filename, format=None):
        file_obj = request.FILES['file']
        
        client = boto3.client('s3',
                            region_name='fra1',
                                endpoint_url=os.getenv('AWS_ENDPOINT_URL'),
                                aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
                                aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
        )

        if request.user.id == request.query_params['reciever']:
            return Response(data={'message': 'cannot share to self'}, status=status.HTTP_400_BAD_REQUEST)
        
        unique_filename = uuid.uuid4().hex + filename

        share = Share(
            filename=unique_filename,
            shared_at=datetime.datetime.now(),
            sender=request.user,
            reciever=User.objects.get(id=request.query_params.get('reciever'))
        )

        if share.reciever is None:
            return Response(data={'message': 'user does not exist'}, status=status.HTTP_400_BAD_REQUEST)

        share.save()

        client.put_object(Bucket=os.getenv('AWS_STORAGE_BUCKET_NAME'), Key=request.user.email + '/' + unique_filename, Body=file_obj, ACL='public-read')

        return Response(status=status.HTTP_204_NO_CONTENT)
    
class ListSharesView(generics.GenericAPIView):
    serializer_class=ShareSerializer
    permission_classes=[IsAuthenticated]
    queryset=Share.objects.all()

    def get(self, request: Request):
        user = request.user
        shares=self.get_queryset().filter(reciever=user)
        serializer=self.get_serializer(shares, many=True)
        for share in serializer.data:
            share['url'] = os.getenv('AWS_ENDPOINT_URL') + '/' + os.getenv('AWS_STORAGE_BUCKET_NAME') + '/' + share['reciever'] + '/' + share['filename']
        
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