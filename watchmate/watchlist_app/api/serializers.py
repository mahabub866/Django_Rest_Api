from dataclasses import fields
from rest_framework import serializers

from watchlist_app.models import Moive, User

class MoiveSerializer(serializers.ModelSerializer):
    len_name=serializers.SerializerMethodField()
    class Meta:
        model=Moive
        fields="__all__"  #['id','name','descroption']
        # exclude=['active']
    def get_len_name(self,object):
        length=len(object.name)
        return length
    def validate(self, data):
        if data['name']==data['description']:
            raise serializers.ValidationError("Title and description should be different")
        else:
            return data

    def validate_name(self,value):
        if len(value)<2:
            raise serializers.ValidationError("Name is too Short!")
        else:
            return value


# def name_lenth(value):
#     if len(value)<3:
#             raise serializers.ValidationError("Name is too Short!")
#     else:
#         return value

# class MoiveSerializer(serializers.Serializer):
#     id=serializers.IntegerField(read_only=True)
#     name=serializers.CharField(validators=[name_lenth])
#     description=serializers.CharField()
#     active=serializers.BooleanField()
    
#     def create(self,validated_data):
#         return Moive.objects.create(**validated_data)
    
#     def update(self,instance,validated_data):
#         instance.name=validated_data.get('name',instance.name)
#         instance.description=validated_data.get('description',instance.description)
#         instance.active=validated_data.get('active',instance.active)
#         instance.save()
#         return instance

#     def validate(self, data):
#         if data['name']==data['description']:
#             raise serializers.ValidationError("Title and description should be different")
#         else:
#             return data

    # def validate_name(self,value):
    #     if len(value)<3:
    #         raise serializers.ValidationError("Name is too Short!")
    #     else:
    #         return value
            
    
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

   