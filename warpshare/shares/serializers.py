from rest_framework import serializers
# from rest_framework.validators import ValidationError
# from rest_framework.authtoken.models import Token
from users.models import User
from .models import Share


class ShareSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    filename = serializers.CharField(max_length=1000)
    shared_at = serializers.DateTimeField()
    sender = serializers.PrimaryKeyRelatedField(read_only=True)
    reciever = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    
    class Meta:
        model=Share
        fields=['id','filename','shared_at','sender','reciever']

