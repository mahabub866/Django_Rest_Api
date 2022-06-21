from rest_framework import serializers

from watchlist_app.models import Moive, User

class MoiveSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField()
    description=serializers.CharField()
    active=serializers.BooleanField()
    
    def create(self,validated_data):
        return Moive.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.description=validated_data.get('description',instance.description)
        instance.active=validated_data.get('active',instance.active)
        instance.save()
        return instance
    
    
GENDER_CHOICES = (
    ('male','Male'),
    ('female', 'Female'),
    ('others', 'Others'),
)
    
class UserSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField()
    age=serializers.IntegerField()
    gender=serializers.ChoiceField( choices = GENDER_CHOICES)
    active=serializers.BooleanField()
    
    def create(self,validated_data):
        return User.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.age=validated_data.get('age',instance.age)
        instance.gender=validated_data.get('gender',instance.gender)
        instance.active=validated_data.get('active',instance.active)
        instance.save()
        return instance