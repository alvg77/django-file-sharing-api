from rest_framework import serializers
# from rest_framework.validators import ValidationError
# from rest_framework.authtoken.models import Token
from users.models import User
from .models import Share


class ShareSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    filepath = serializers.CharField(max_length=1000)
    shared_at = serializers.DateTimeField()
    sender = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    reciever = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    
    class Meta:
        model=Share
        fields=['id','filepath','shared_at','sender','reciever']

    def validate(self, attrs):
        reciever_exists=User.objects.filter(email=attrs['reciever']).exists()
        
        if not reciever_exists:
            raise serializers.ValidationError('no user with this email exists')
        
        return super().validate(attrs)
    
    def create(self, validated_data):
        sender_obj = User.objects.get(email=validated_data.pop('sender'))
        reciever_obj = User.objects.get(email=validated_data.pop('reciever'))

        share = super().create(validated_data)
        share.sender = sender_obj
        share.reciever = reciever_obj
        share.save()

        return share

