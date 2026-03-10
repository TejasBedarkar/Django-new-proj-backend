from rest_framework import serializers
from .models import Student
from django.contrib.auth.models import User    #built-in authentication model.

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        

class UserSerializer(serializers.ModelSerializer):
    class Meta:                                   #configure serialize
        model = User
        fields = ['id','username','password']
        extra_kwargs = {
            'password': {'write_only': True}          #Password will not appear in API response
        }

    def create(self, validated_data):             #This overrides default creation behavior
        user = User.objects.create_user(          #This is important because it hashes the password. Without this, password would be stored as plain text.
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user